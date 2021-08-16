# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Flipkart1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Product_Name = scrapy.Field()
    Rating = scrapy.Field()
    Num_Rating = scrapy.Field()
    Num_Reviews = scrapy.Field()
    Price = scrapy.Field()
    Product_Specs = scrapy.Field()
    Discount = scrapy.Field()