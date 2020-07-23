# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


from tingche.settings import proxyMeta

import time

class TingcheDownloaderMiddleware(object):
    def process_request(self, request, spider):

        request.meta["proxy"] = proxyMeta

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        print(response.text)
        if str(response.status).strip() != '200':
            print(response.text)
            print('异常状态码==' + str(response.status))
            time.sleep(10)
            request.meta["proxy"] = proxyMeta
            return request


        return response

    def process_exception(self, request, exception, spider):
        request.meta["proxy"] = proxyMeta

        return request
