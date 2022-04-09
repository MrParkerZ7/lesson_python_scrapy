# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_currency(value: str):
    return value.replace('฿', '').strip()


class LazadaItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst())
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_currency),
        output_processor=TakeFirst())
    image = scrapy.Field()
