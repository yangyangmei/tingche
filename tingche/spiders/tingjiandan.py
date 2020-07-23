# -*- coding: utf-8 -*-
import scrapy
from ..common import *
import json
from tingche.items import TingcheItem
import os

class TingJianDanSpider(scrapy.Spider):
    name = 'tingjiandan'
    allowed_domains = ['open.tingjiandan.com']
    tingjiandan_header = {
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Connection": "keep-alive",
        "Host": "open.tingjiandan.com",
        "Referer": "https://servicewechat.com/wx6945d1bda68d7993/21/page-frame.html",
        "User-Agent":getrandom_useragent(),
        "content-type": "application/json",
    }

    tingjiandan_data = {
        "method": "insideGetOrder",
        "carNum": "苏D335SA",
        "deviceId": "",
        "prePayType": "7",
        "command": "order",
        "platform": "weixin",
        "version": "1.1.8", "channel": "77",
        "userId":get32str(),
        "unionId": "o5ZYJuJOWnFksNWDzYP2nfyde6DY",
        "phone": None,
        "openId": "oobDH5YaxtFuYrXx4CZ03CU1iLsU"}
    tingjiandan_url = 'https://open.tingjiandan.com/tcserver/gateway'

    def start_requests(self):
        # module_path = os.path.abspath(os.curdir)
        # with open(module_path+'/chepai3.txt') as f:
        #     chepai_list = f.readlines()
        #
        # for chepai in chepai_list:
        #     print(chepai.strip())
        #     # time.sleep(1)
        #     self.tingjiandan_data["carNum"] = chepai.strip()
        #     yield scrapy.Request(
        #         url=self.tingjiandan_url,
        #         method="POST",
        #         headers=self.tingjiandan_header,
        #         body=json.dumps(self.tingjiandan_data),
        #         callback=self.parse,
        #         dont_filter=True,
        #     )
        # 单个车牌调用
        self.tingjiandan_data["carNum"] = '苏D335SA'
        yield scrapy.Request(
            url=self.tingjiandan_url,
            method="POST",
            headers=self.tingjiandan_header,
            body=json.dumps(self.tingjiandan_data),
            callback=self.parse,
            dont_filter=True,
        )


    def parse(self, response):
        print(response.text)
        res = json.loads(response.text)
        # orderInfo
        parkInfos = res.get("parkInfos")
        if(parkInfos):
            for park in parkInfos:
                print('jin-------')
                item = TingcheItem()
                start = park.get("startDate")
                start_time = park.get("startTime")
                time = ' '+start_time[:2]+":"+start_time[2:4]+":"+start_time[4:] if start_time else  ''

                item["car_name"] = park.get("carNum")
                item["enter_time"] = start[:4]+"-"+start[4:6]+"-"+start[6:]+time if start else ''
                item["park_name"] = park.get("parkName")
                item["from_where"] = '停简单'
                print(item)
                yield item


# 苏D335SA


