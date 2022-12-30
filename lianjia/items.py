# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    location1 = scrapy.Field() #区域1
    location2 = scrapy.Field() #区域2
    location3 = scrapy.Field() #区域3
    price = scrapy.Field()  # 价格
    area = scrapy.Field()   # 面积
    orientation = scrapy.Field()  # 朝向
    room_type = scrapy.Field()#信息
    pass
