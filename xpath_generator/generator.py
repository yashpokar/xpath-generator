from lxml import html
import requests

response = requests.get('http://localhost:8000')
response = html.fromstring(response.content)
print response.xpath('//*[@id="product-price"]/text()')
