# coding=utf-8
import re

from scrapy import Request
from scrapy import Spider

from htk_crawl.items import HtkCrawlItem


class SoufangSpider(Spider):

    name = 'soufang_spider'
    url = 'http://nanjing.fang.com/'

    def start_requests(self):
        """发送请求"""
        yield Request(self.url)

    def parse(self, response):
        content = response.xpath('//a').extract()
        for row in content:
            item = HtkCrawlItem()
            content = re.sub('(.+>)(.+)(<.*)', '\g<2>', row)
            href = re.sub('(.+?href=")(.+?)(".*)', '\g<2>', row)
            if re.findall('<img', row):
                image_url = re.sub('(.+<img src=")(.+?)(".*)', '\g<2>', row)
            else:
                image_url = ''
            item['content'] = content
            item['href'] = href
            item['image_url'] = image_url
            yield item
