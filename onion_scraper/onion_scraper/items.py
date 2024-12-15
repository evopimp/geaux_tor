class OnionScraperItem(scrapy.Item):
    title = scrapy.Field()
    links = scrapy.Field()