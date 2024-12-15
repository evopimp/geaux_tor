# Contents of /onion_scraper/onion_scraper/settings.py

BOT_NAME = 'onion_scraper'

SPIDER_MODULES = ['onion_scraper.spiders']
NEWSPIDER_MODULE = 'onion_scraper.spiders'

USER_AGENT = 'onion_scraper (+http://www.yourdomain.com)'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
    'onion_scraper.pipelines.YourPipelineName': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

# Configure the proxy settings for Tor
HTTP_PROXY = 'socks5://localhost:9050'

# Additional settings
DOWNLOAD_TIMEOUT = 30
RETRY_TIMES = 3

# Enable or disable extensions
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}