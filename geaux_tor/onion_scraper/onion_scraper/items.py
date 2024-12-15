from scrapy import Item, Field

class OnionScraperItem(Item):
    url = Field()
    title = Field()
    content = Field()
    timestamp = Field()