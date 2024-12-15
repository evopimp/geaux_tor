import scrapy
from onion_scraper.items import OnionScraperItem
from datetime import datetime
import socks
import socket

class OnionSpider(scrapy.Spider):
    name = 'onion_spider'
    allowed_domains = [
        'example.onion',
        'anotherexample.onion',
    ]
    start_urls = [
        # Add your .onion URLs here
        'http://example.onion'
    ]

    def __init__(self, *args, **kwargs):
        super(OnionSpider, self).__init__(*args, **kwargs)
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket

    def parse(self, response):
        item = OnionScraperItem()
        item['url'] = response.url
        item['title'] = response.css('title::text').get()
        item['content'] = response.css('body::text').getall()
        item['timestamp'] = datetime.now().isoformat()
        yield item