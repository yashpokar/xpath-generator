import os
from xpath_generator import XPATHGenerator


class SpiderGenerator(object):
	_spider = {}
	_website = ''

	def __init__(self):
		self._generator = XPATHGenerator()

	def look_inside(self, website):
		self._website = website
		return self

	def find(self, **kwargs):
		for key, value in kwargs.items():
			self._spider[key] = self._generator.want(value).refer(self._website).generate()
		return self

	def generate(self):
		XPATHS = ''

		for key, xpaths in self._spider.items():
			for xpath in xpaths:
				XPATHS += "il.add_xpath('{key}', '{value}')\n\t\t".format(key=key, value=xpath)

		with open(os.path.join(os.path.dirname(__file__), 'templates/spider.tmp'), 'r') as f:
			result = f.read().format(XPATHS=XPATHS, URL=self._website)

			return result


# if __name__ == '__main__':
# 	generator = SpiderGenerator()
# 	generator.look_inside('https://www.amazon.com/dp/B071YV88D9')
# 	spider = generator.find(
# 		price='$16.99 - $23.80',
# 		description='Material: 95% Rayon , 5% Spandex.Stretchy,soft and comfy.',
# 		reviews='1,044 customer reviews',
# 	)
# 	print(spider.generate())
