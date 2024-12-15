from scrapy import Spider
from scrapy.http import Request
from bs4 import BeautifulSoup
import socks
import socket

class OnionSpider(Spider):
    name = "onion_spider"
    allowed_domains = ["onion"]
    start_urls = ["http://example.onion"]  # Replace with actual .onion URLs

    def __init__(self, *args, **kwargs):
        super(OnionSpider, self).__init__(*args, **kwargs)
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        self.log(f"Scraping: {response.url}")

        # Extract links
        links = [link.get('href') for link in soup.find_all('a')]
        links = list(filter(None, links))

        onion_links = [l for l in links if "onion" in l]

        for link in onion_links:
            yield {'link': link}

        # Follow pagination or additional links if necessary
        next_page = soup.find('a', text='Next')  # Adjust selector as needed
        if next_page:
            yield Request(url=next_page['href'], callback=self.parse)