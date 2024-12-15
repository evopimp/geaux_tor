import json

class OnionScraperPipeline:
    def open_spider(self, spider):
        self.file = open('scraped_data.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item