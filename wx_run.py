#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : wx_run.py
# @Author: sxs
# @Date  : 2018/8/16
# @Desc  :微信今日步数
import requests
import re
import json


class WechatSprot(object):
    def __init__(self, openid):
        self.openid = openid

    def getInfo(self):
        url = "http://hw.weixin.qq.com/steprank/step/personal"
        querystring = {"pass_ticket": self.openid}
        headers = {
            'host': "hw.weixin.qq.com",
            'connection': "keep-alive",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.691.400 QQBrowser/9.0.2524.400",
            'accept-encoding': "gzip, deflate",
            'accept-language': "zh-CN,zh;q=0.8,en-us;q=0.6,en;q=0.5;q=0.4",
            'cookie': "hwstepranksk=eNB0W1ZgkX3awA6SSgyfW5A6pgugzVMykEFxmVtDUm6-HNOG; pass_ticket=iR%2BIoGW1GZeOZ5K3OKTrgoC4cMQdNmfKeYSlmRwQLrzorU3wAqIMR0IED12yg8GQ",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        res = re.findall('window.json = (.+);', response.text)
        print(res[0])
        return json.loads(res[0])


if __name__ == "__main__":
    obj = WechatSprot('iR%2BIoGW1GZeOZ5K3OKTrgoC4cMQdNmfKeYSlmRwQLrzorU3wAqIMR0IED12yg8GQ')
    today = obj.getInfo()
    print(today['rankdesc'])
