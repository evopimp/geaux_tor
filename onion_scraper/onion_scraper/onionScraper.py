defining a Scrapy spider that uses the existing scraping logic to extract data from .onion sites.

import scrapy
import socks
import socket
from bs4 import BeautifulSoup

class OnionSpider(scrapy.Spider):
    name = 'onion_spider'
    start_urls = ['http://example.onion']  # Replace with actual .onion URLs

    def __init__(self, *args, **kwargs):
        super(OnionSpider, self).__init__(*args, **kwargs)
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        self.log(soup.prettify())

        title = soup.title.string if soup.title else 'No title'
        self.log(f'Title: {title}')

        links = [link.get('href') for link in soup.find_all('a')]
        links = list(filter(None, links))

        onion_links = [l for l in links if "onion" in l]
        for link in onion_links:
            yield {'onion_link': link}