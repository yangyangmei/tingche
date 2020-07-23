# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter

class JsonPipeLine(object):
    def __init__(self):
        self.file = open('data.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self,spider):
        self.exporter.fields_to_export()
        self.file.close()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

class TingchePipeline(object):
    def process_item(self, item, spider):
        return item
