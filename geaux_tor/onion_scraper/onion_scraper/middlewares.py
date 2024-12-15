from scrapy import signals

class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta['proxy'] = 'socks5://localhost:9050'

class OnionScraperMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)