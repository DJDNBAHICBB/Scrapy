# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PicItem(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field()  # 即 Item里面 url 信息设置为 image_urls
    images = scrapy.Field()  # 图片名称信息 设置为images
    detailed = scrapy.Field()
