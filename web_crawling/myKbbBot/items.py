# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MykbbbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #basic info
    query_date = scrapy.Field()
    query_url = scrapy.Field()
    vehicleId = scrapy.Field()
    car_year = scrapy.Field()
    car_make = scrapy.Field()
    car_model = scrapy.Field()
    car_trim = scrapy.Field()
    basic_info = scrapy.Field()
    specs_info = scrapy.Field()