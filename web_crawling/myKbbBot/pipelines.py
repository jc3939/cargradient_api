# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from scrapy.exporters import CsvItemExporter

class MykbbbotPipeline:
    '''
        collection_name = 'carspecs'

        def __init__(self, mongo_uri, mongo_db):
            self.mongo_uri = mongo_uri
            self.mongo_db = mongo_db

        @classmethod
        def from_crawler(cls, crawler):
            ## pull in information from settings.py
            return cls(
                mongo_uri=crawler.settings.get('MONGODB_SERVER'),
                mongo_db=crawler.settings.get('MONGO_DATABASE'),
            )

        def open_spider(self, spider):
            ## initializing spider
            ## opening db connection
            self.client = pymongo.MongoClient(self.mongo_uri)
            self.db = self.client[self.mongo_db]

        def close_spider(self, spider):
            ## clean up when spider is closed
            self.client.close()

        def process_item(self, item, spider):
            ## how to handle each post
            self.db[self.collection_name].insert(dict(item))
            logging.debug("Post added to MongoDB")
            return item
    '''
    def __init__(self):
        self.filename = 'kbb2.csv'
    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item