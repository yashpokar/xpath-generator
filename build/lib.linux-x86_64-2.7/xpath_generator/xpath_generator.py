import requests
from lxml import html


class HTTPResponseError(Exception):
	pass


class XPATHGenerator(object):

	TRIALS = [
		{ 'xpath': '//*[contains(text(), "{need}")]', 'accessor': '{xpath}/text()', },
	]

	headers = {
		'Connection': 'keep-alive',
		'Accept': 'text/html,*/*',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9,mt;q=0.8',
	}

	MAX_RETRY = 10

	def __init__(self):
		self._need = ''
		self._webpage = ''
		self._content = ''
		self._results = []

	def want(self, need):
		self._need = need
		return self

	def refer(self, webpage):
		self._webpage = webpage
		return self

	def using(self, headers={}):
		self.headers.update(headers)
		return self

	def generate(self):
		self._content = self._fetch_web_page()
		self._start_trials()
		results = self._results
		self._results = []
		return results

	@property
	def selector(self):
		return html.fromstring(self._content)

	def _start_trials(self):
		for trial in self.TRIALS:
			xpath = trial['xpath'].format(need=self._need)

			possibilities = self.selector.xpath(xpath)

			for possibility in possibilities:
				self._results.append(self._build_xpath(possibility, trial))

	def _build_xpath(self, possibility, trial, path='./', history=[], retry=0):
		current_xpath = '{path}self::*'.format(path=path)

		# We have check weather this goes down
		# Defence this list instead of asking for
		# the first element available
		possibility = possibility.xpath(current_xpath)[0]
		attributes = dict(possibility.items())

		history.append({
			'attributes': attributes,
			'tag_name': possibility.tag,
		})

		id_ = attributes.get('id', '')

		if retry > self.MAX_RETRY:
			# Replace this by convinient signification
			return 'Maximum tries attempted.'

		if id_:
			way = '/'.join(reversed([moment['tag_name'] for moment in history][:-1]))
			way = '/{way}'.format(way=way) if way else way
			xpath = '//*[@id="{id}"]{way}'.format(id=id_, way=way)
			return trial['accessor'].format(xpath=xpath)

		path += '../'
		retry += 1
		return self._build_xpath(possibility, trial, path, history, retry)

	def _fetch_web_page(self):
		response = requests.get(self._webpage, headers=self.headers)

		if response.status_code != 200:
			raise HTTPResponseError('Page content could not fetch. HTTP STATUS CODE {code}'.format(
				code=response.status_code
			))

		return response.content
