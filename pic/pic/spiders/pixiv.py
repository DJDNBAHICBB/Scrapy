import scrapy
from pip._vendor.urllib3.util import Url

from pic.items import PicItem
from scrapy.pipelines.images import ImagesPipeline

class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    allowed_domains = ['pixivacg.com']
    start_urls = ['https://www.pixivacg.com/pzzc/pxvzc/page/44']

    def parse(self, response):
        into = response.xpath('//div[@class = "post-module-thumb"]/a/@href').extract()

        for u in into:
            item1 = PicItem()
            item1['detailed'] = u
            yield scrapy.Request(
                item1['detailed'],
                callback=self.parse_detail,
            )
        ifnxt = response.xpath('//div[@class="btn-pager"]').extract()[0]
        if "empty button" in ifnxt:
            nxt = response.xpath('//div[@class="btn-pager"]/a/@href').extract()[0]
            yield scrapy.Request(
                nxt,
                callback=self.parse
            )
    def parse_detail(self, response):
        urls = response.xpath('//div[@class="entry-content"]/p/img/@src').extract()
        for url in urls:
            url = [url]
            print(url)
            it1 = PicItem()
            it1['image_urls'] = url
            yield it1