class CleanDataPipeline:
    def process_item(self, item, spider):
        # Clean and validate the scraped data
        item['title'] = item['title'].strip() if item['title'] else 'No Title'
        item['content'] = ' '.join(item['content']).strip() if item['content'] else 'No Content'
        return item

class SaveToFilePipeline:
    def open_spider(self, spider):
        self.file = open('scraped_data.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = f"{item}\n"
        self.file.write(line)
        return item