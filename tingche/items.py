# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TingcheItem(scrapy.Item):
    # define the fields for your item here like:

    car_name = scrapy.Field()  #车牌
    enter_time = scrapy.Field() # 入场时间
    park_name = scrapy.Field()  # 停车场名称
    from_where = scrapy.Field()  # 哪个平台
    other_info = scrapy.Field() #其他信息，捷停车月卡用户无入场时间



