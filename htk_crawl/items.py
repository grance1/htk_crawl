from scrapy import Item, Field


class HtkCrawlItem(Item):
    content = Field()
    href = Field()
    image_url = Field()
