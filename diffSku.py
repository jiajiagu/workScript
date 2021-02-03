#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/1 11:35 下午
# @Author  : jiajia.gu

import requests

cloudPathList = {
    "邀请年课": "/xxx-yyy/input/upc_course_category.json",
    "短信": "/xxx-yyy/input/join_code_sms_push_config.json",
    "抽奖": "/xxx-yyy/input/raffle_upc_config.json"
}


def diffSku(sku):
    for key, value in cloudPathList.items():
        prodUrl = "https://xxx/api/storage/shared/json?path=" + value
        headers = {
            'accesstoken': 'xxxxx-f459-4254-8d1f-ada749f74887'
        }
        response = requests.request("GET", prodUrl, headers=headers, verify=False)
        # print(response.text)
        f = open("./resultSkuInfo", 'w', encoding='UTF-8')
        if sku not in response.text:
            print (key + "无sku：" + sku,file = f)
        f.close()


file = open("./skuList", 'r', encoding='UTF-8')
skuList = []
for line in file:
    # 将空格作为分隔符按行分割
    skuList.extend([str(i) for i in line.split()])
file.close()

for sku in skuList:
    diffSku(sku)
