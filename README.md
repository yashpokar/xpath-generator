# xpath-generator
> Dynamic xpath building, goal is to automate the web scraping


git clone this repo
``` pip install -e . ```

Type into your command line
``` genxpath want="\$6.56 - \$57.17" refer="https://www.amazon.com/Champion-Classic-T-Shirt-Oatmeal-Heather/dp/B073R2C868/" ```

``` genxpath want="{The text you want from web page}" refer="{ url }" ```


> Auto generate spider

```
from xpath_generator import SpiderGenerator

generator = SpiderGenerator()

generator.look_inside('https://www.amazon.com/dp/B071YV88D9')

spider = generator.find(
	price='$16.99 - $23.80',
	description='Material: 95% Rayon , 5% Spandex.Stretchy,soft and comfy.',
	reviews='1,044 customer reviews',
)

print(spider.generate())
```

*Note: Just started developing, It's 0.0.1-dev version.
