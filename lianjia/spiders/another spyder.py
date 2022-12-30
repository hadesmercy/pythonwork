import scrapy
import time
from scrapy.http import Request
from lianjia.items import LianjiaItem
import random


class LianjiaSpider(scrapy.Spider):
    #这个是用来根据不同的城市单独处理的爬虫，仅仅适用于单独的区域
  # 名称
    custom_settings = {
        'ITEM_PIPELINES': {'anotherlianjia.pipelines.LianjiaPipeline': 300, },
    }
    start_urls = ['https://lz.lianjia.com/zufang']  # URL列表

    def __init__(self):
        self.url_num = 0
        self.apartment_num = 0
        self.done_num = 0

    def parse(self, response):
        # 获取各个区的url
        regions = response.css('#filter > ul:nth-child(2) > li.filter__item--level2 > a')
        for region in regions[1:]:
            url = 'https://lz.lianjia.com' + region.attrib['href']
            yield Request(url, callback=self.parse_region)

    # 遍历所有页
    def parse_region(self, response):
        house_num = int(
            response.css('#content > div.content__article > p > span.content__title--hl::text').get())  # 房子数量
        print(house_num)
        a = response.xpath("/html/body/div[3]/div[1]/div[5]/div[1]/p/a[2]/text()").extract()
        if house_num > 3000:
                with open("额外处理.txt", 'w', encoding="utf-8") as f:
                    aa = ''. join(a)
                    f.write(aa + '\n')
                print("该区域租房信息大于3000，需要额外处理")
        else:
            page_num = min(house_num // 30 + 1, 100)  # 每页展示30条
            for i in range(1, page_num + 1):
                url = response.url + 'pg{}'.format(i)
                print(url)
                yield Request(url, callback=self.parse_overview)

    # 爬取房屋概况信息
    def parse_overview(self, response):
        for info in response.xpath("/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[*]"):
                print("成功调用")
                item = LianjiaItem()
                "/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[6]/div/p[2]/a[1]"
                item['title'] = ''.join(info. xpath("div/p[1]/a/text()").extract()).replace('\n',' ').strip()
                item['location1'] = ''.join(info. xpath("div/p[2]/a[1]/text()").extract())
                item['location2'] = ''.join(info. xpath("div/p[2]/a[2]/text()").extract())
                item['location3'] = ''.join(info. xpath("div/p[2]/a[3]/text()").extract())
                item['area'] = ''.join(info.xpath("div/p[2]/text()").extract()).split('\n')[-4].strip()
                item['orientation'] = ''.join(info.xpath("div/p[2]/text()").extract()).split('\n')[-3].strip()
                item['room_type'] = ''.join(info.xpath("div/p[2]/text()").extract()).split('\n')[-2].strip()
                item['price'] = ''.join(info. xpath("div/span/em/text()").extract())

                self.apartment_num += 1
                print(item)
                yield item




# if __name__ == '__main__':
#     scrapy_bug = LianjiaSpider()
#     scrapy_bug.parse()
