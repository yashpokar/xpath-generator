from xpath_generator import SpiderGenerator

generator = SpiderGenerator()

generator.look_inside('https://www.amazon.com/dp/B071YV88D9')

spider = generator.find(
	price='$16.99 - $23.80',
	description='Material: 95% Rayon , 5% Spandex.Stretchy,soft and comfy.',
	reviews='1,044 customer reviews',
)

print(spider.generate())
