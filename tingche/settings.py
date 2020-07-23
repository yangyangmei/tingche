# -*- coding: utf-8 -*-

# Scrapy settings for tingche project
#

BOT_NAME = 'tingche'

SPIDER_MODULES = ['tingche.spiders']
NEWSPIDER_MODULE = 'tingche.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_FILE = "tingche.log"
LOG_LEVEL = "DEBUG"


# 需要使用代理ip的打开
DOWNLOADER_MIDDLEWARES = {
   # 'tingche.middlewares.TingcheDownloaderMiddleware': 543,
}


DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False

FEED_EXPORT_ENCODING = 'utf-8'
# 支持随机下载延迟
RANDOMIZE_DOWNLOAD_DELAY = True

ITEM_PIPELINES = {
   # 'tingche.pipelines.JsonPipeLine':500,
   'tingche.pipelines.TingchePipeline': 300,
}

# 小象代理信息 https://www.xiaoxiangdaili.com/u/tunnel/dynamic
proxyUser = "602446799651098624"
proxyPass = "UIB7hoXi"
proxyHost = "http-dynamic.xiaoxiangdaili.com"
proxyPort = "10030"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}