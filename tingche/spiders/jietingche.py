# -*- coding: utf-8 -*-
import scrapy
from ..common import *
import json
import os
from tingche.items import TingcheItem


class JieTingSpider(scrapy.Spider):
    name = 'jieting'
    allowed_domains = ['sytgate.jslife.com.cn']

    jieting_url =  'https://sytgate.jslife.com.cn/core-gateway/order/carno/pay/appindex'
    jieting_header = {
            "user-agent": getrandom_useragent(),
            "cookie": jieting_cookie(),
            "content-type": "application/json;charset=utf-8",
            "method": "POST",
            "scheme": "https",
            "path": "/core-gateway/order/carno/pay/appindex",
            "authority": "sytgate.jslife.com.cn",
        }




    def start_requests(self):
        jieting_data = {
            "carNo": "粤-B82EZ8",
            "privacyOption": 1,
            "nonce": "2EF08C4B-AE7B-44E5-9082-"+get_upper_12str(),
            "timestamp": current_timestr13(),
            "longitude": "0.000000",
            "applictionVersion": "40101",
            "latitude": "0.000000",
            "isNewReport": 1,
            "applictionType": "APP",
            "signType": "MD5",
            "sign": get_upper_32str()
        }

        module_path = os.path.abspath(os.curdir)
        with open(module_path+'/chepai3.txt') as f:
            chepai_list = f.readlines()
            for chepai in chepai_list:
                jieting_no = chepai.strip()
                jieting_no = jieting_no[0] + '-' + jieting_no[1:]
                # jieting_data = {"carNo": "皖-K228H1", "userId": ""}
                jieting_data["carNo"] = jieting_no
                print(jieting_no)
                # time.sleep(1)

                yield scrapy.Request(
                    url=self.jieting_url,
                    method="POST",
                    headers=self.jieting_header,
                    body=json.dumps(jieting_data),
                    callback=self.parse,
                    dont_filter=True,
                )

    def parse(self, response):
        print(response.text)
        res = json.loads(response.text)
        if(res.get("resultCode")=="0"):
            item = TingcheItem()
            parkInfos = res.get("obj")
            item["car_name"] = parkInfos.get("carNo")
            item["enter_time"] = parkInfos.get("startTime")
            item["park_name"] = parkInfos.get("businesserName")
            item["from_where"] = '捷停车'
            item["other_info"] = parkInfos.get("retmsg")
            print(item)
            yield item