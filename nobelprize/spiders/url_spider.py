import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class UrlSpider(scrapy.Spider):
    name = "url_spider"
    start_urls = [
        'http://www.nobelprize.org/nomination/archive/list.php?prize=4&year=%d' %(n) for n in range (1901, 1967)
    ]
    count = 0
    def parse(self, response):
        path = response.selector.xpath('//tr//td[3]/a[contains(@href, "php")]/@href').extract()
       	count =+ len(path)
        for i in range (0, len(path)):
	        string = "http://www.nobelprize.org/nomination/archive/" + str(response.selector.xpath('//tr//td[3]/a[contains(@href, "php")]/@href')[i].extract())
	        print(string)
