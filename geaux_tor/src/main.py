def main():
    from utils.tor_connection import connect_to_tor
    from scraper.image_scraper import ImageScraper
    from scraper.document_scraper import DocumentScraper

    # Establish connection to the Tor network
    if connect_to_tor():
        print("Connected to the Tor network.")

        # Initialize scrapers
        image_scraper = ImageScraper()
        document_scraper = DocumentScraper()

        # Example URLs (these should be replaced with actual URLs)
        image_url = "http://example.com/images"
        document_url = "http://example.com/documents"

        # Scrape images and documents
        image_scraper.scrape_images(image_url)
        document_scraper.scrape_documents(document_url)

    else:
        print("Failed to connect to the Tor network.")

if __name__ == "__main__":
    main()