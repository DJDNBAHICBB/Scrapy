# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
from pic.items import PicItem
from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter

logger = logging.getLogger(__name__)
class PicPipeline(object):
    def process_item(self, item, spider):
        # pass
        logger.warning(item["image_urls"])
        return item
