# Onion Scraper Project

This project is a Scrapy-based web scraper designed to extract data from .onion websites. It utilizes the Tor network to access hidden services and scrape content.

## Project Structure

```
onion_scraper
├── scrapy.cfg
├── README.md
└── onion_scraper
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    ├── spiders
    │   ├── __init__.py
    │   └── onion_spider.py
    └── onionScraper.py
```

## Setup Instructions

1. **Install Dependencies**: Ensure you have Python and pip installed. Then, install Scrapy and other required libraries:
   ```
   pip install scrapy beautifulsoup4 requests pysocks
   ```

2. **Tor Setup**: Make sure you have Tor installed and running on your machine. The default SOCKS5 proxy should be set to `localhost:9050`.

3. **Run the Spider**: Navigate to the project directory and run the spider using the following command:
   ```
   scrapy crawl onion_spider
   ```

## Usage Examples

- The spider will start scraping from the specified .onion URLs defined in `onion_spider.py`.
- Scraped data will be processed through the pipelines defined in `pipelines.py`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.