# -*- coding: utf-8 -*-
import scrapy
from ..common import *
import json
from tingche.items import TingcheItem
import os

class TingSpider(scrapy.Spider):
    name = 'suting'
    allowed_domains = ['cloud.keytop.cn']

    def start_requests(self):

        logId = get8randomstr()
        # pp_user_id = '40717578466763915'
        pp_user_id = '40718527654542491'

        su_post_header = {
            "Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-cn", "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "cloud.keytop.cn", "Origin": "https://cloud.keytop.cn",
            "User-Agent": getrandom_useragent(),
            "Cookie": "_region_code_=000; logId=" + logId + "; pp_user_id=" + pp_user_id,

        }
        su_post_url = 'https://cloud.keytop.cn/service/front/parking/query?_=' + current_timestr13()

        module_path = os.path.abspath(os.curdir)
        with open(module_path+'/chepai3.txt') as f:
            chepai_list = f.readlines()
            for lpn in chepai_list:
            # lpn = '鄂B68118'
                lpn = lpn.strip()
                print(lpn)
                su_data = {"lpn": lpn}
                yield scrapy.Request(
                    url=su_post_url,
                    method="POST",
                    headers=su_post_header,
                    body=json.dumps(su_data),
                    callback=self.parse,
                    dont_filter=True,
                    meta={'logId': logId, "pp_user_id": pp_user_id}
                )

        # 单个车牌调用测试
        # lpn = '鄂B68118'
        # su_data = {"lpn": lpn}
        # yield scrapy.Request(
        #     url=su_post_url,
        #     method="POST",
        #     headers=su_post_header,
        #     body=json.dumps(su_data),
        #     callback=self.parse,
        #     dont_filter=True,
        #     meta={'logId':logId,"pp_user_id":pp_user_id}
        # )


    def parse(self, response):
        print(response.text)

        res  = json.loads(response.text)
        if(str(res.get("code"))=='2000'):
            data = res.get('data')
            url = data.get('url')
            p = url.split('p=')[1]
            logId = response.meta.get("logId")
            pp_user_id = response.meta.get('pp_user_id')
            url_detail = 'https://cloud.keytop.cn/service/front/payment/confirm/card?_='+current_timestr13()+'&p='+p
            su_detail_head = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-cn",
                "Connection": "keep-alive",
                "Cookie": "regionId=000; _region_code_=000; logId="+logId+"; pp_user_id="+pp_user_id,
                "Host": "cloud.keytop.cn",
                "User-Agent":getrandom_useragent(),
            }
            yield scrapy.Request(
                url=url_detail,
                headers=su_detail_head,
                body=json.dumps({}),
                callback=self.parse_detail,
                dont_filter=True,
            )

    def parse_detail(self,response):
        print(response.text)
        res = json.loads(response.text)
        if(str(res.get("code")) =='2000'):
            car_info = res.get("data").get("orderConfirmInfo")
            item = TingcheItem()
            item["car_name"] = car_info.get("carPlateNum")
            item["enter_time"] = car_info.get("comeTime")
            item["park_name"] = car_info.get("lotName")
            item["from_where"] = '速停车'
            print(item)
            yield item
