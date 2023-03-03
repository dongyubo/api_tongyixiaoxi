import requests
import json
import string
import random
import datetime


def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


# 获取token的请求
url_token = "http://172.22.33.111:6061/auth/getToken"
header_token = {'Content-Type': 'application/json'}
data_token = {
    "bizNo": str(random.randint(10000, 99999)),
    "request": {
        "channelCode": "QD000019",
        "channelSecret": "WQGWHPWBELU3PSRR"
    },
    "version": "1"
}

response = requests.post(url_token, headers=header_token, data=json.dumps(data_token))
if response.status_code == 200:
    result = response.json()
    token = result['result']['token']
    print("获取token成功：", token)

for i in range(10):
    print("开始执行测试")
    # 调用batchSendMessage接口
    url_batch = "http://172.22.33.111:6061/sendMessage/batchSendMessage"
    name = str(random.randint(6000, 40000000))
    print(name)
    user_list = []
    for t in range(100):
        user = {
            "appOpenId": "5043a1b7-13a5-1def-0000-0186a0f87d35",
            "extras": {},
            "messageId": "messageId" + random_string(5) + str(t) + str(i),

            # + str(t)
            "phone": "16621109915",
            # "wechatMiniParam": {
            #     "wechatMiniOpenId": "2882171681",
            #     "data": {
            #         "character_string2": {
            #             "value": "HO1111"
            #         },
            #         "character_string4": {
            #             "value": "018115624741"
            #         },
            #         "phrase5": {
            #             "value": "已出票"
            #         },
            #         "thing3": {
            #             "value": "广州——北京"
            #         },
            #         "time1": {
            #             "value": "2023年01月15日 08:40"
            #         }
            #     },
            #     "page": "pages/index/index"
            # },
            "wechatPublicParam": {
                "client_msg_id": "",
                "data": {
                    "first": {
                        "value": "您购买的机票已经出票成功啦！"
                    },
                    "keyword1": {
                        "color": "#173177",
                        "value": "0181156215458"
                    },
                    "keyword2": {
                        "color": "#173177",
                        "value": "HO1117"
                    },
                    "keyword3": {
                        "color": "#173177",
                        "value": "2023年01月12日14:00"
                    },
                    "keyword4": {
                        "color": "#173177",
                        "value": "上海虹桥T2-深圳宝安T3"
                    },
                    "remark": {
                        "color": "#173177",
                        "value": "出票后可优先办理值机选座"
                    }
                },
                # "miniprogram": {
                #     "appid": "wx534a6f359f266888",
                #     "pagepath": "pages/index/index"},

                "url": "https://t-m.hoair.cn/flightSearch/search/index.html?barStyle=0",
                "wechatPublicOpenId": "o-nEn6H5H7WWCpdGd6xcJT-qWwG4"
            }
        }
        user_list.append(user)

        # print(user_list)
    header_batch = {
        "accept": "*/*",
        "Content-Type": "application/json",
        "token": token
    }
    data_batch = {
        "bizNo": name,
        "request": {

            "aisleList": [

                "RMDX",
                "RMGZH",
                "PTDYBAPP"

                # "PTDYBGZH",
                # "PTDYBAPP",
                # "PTDYBDX"

                # "JXDYBAPP",
                # "JXDYBDX",
                # "JXDYBXCX",
                # "JXDYBGZH"
            ],
            "batchId": "batch_dyb_2023_03_02_1" + name,
            "lastSendTime": "2023-03-14 21:00:00",
            "messageType": "URGENT",
            # ORDINARY 一般  URGENT 緊急
            "sendType": "ALL",
            "taskId": name,
            "startSendTime": "",
            # "strategyId": "CL000033",
            # "strategyId": "CL000034",
            "requestMode": "API",
            "userList": user_list,
            "appTemplateCode": "APP000010",
            "smsTemplateCode": "SMS000019",
            "wechatPublicTemplateCode": "WXG000006"
            # "wechatMiniTemplateCode": "WXX000002"
        },
        "version": "1.0"
    }
    batchResponse = requests.post(url_batch, headers=header_batch, json=data_batch)
    if batchResponse.status_code == 200:
        batchResult = batchResponse.json()
        print(datetime.datetime.now(), "第" + str(i + 1) + "次：调用batchSendMessage成功：", batchResult)

    else:
        print("调用batchSendMessage失败：", batchResponse.status_code)
