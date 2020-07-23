from scrapy import cmdline


# cmdline.execute("scrapy crawl tingjiandan -o info.csv -t csv".split())

# cmdline.execute("scrapy crawl suting -o info.csv -t csv".split())

cmdline.execute("scrapy crawl jieting -o info.csv -t csv".split())