import requests
import json
import random
import threading

# 获取token的请求
url_token = "http://172.22.33.111:6061/auth/getToken"
header_token = {'Content-Type': 'application/json'}
data_token = {
    "bizNo": str(random.randint(10000, 99999)),
    "request": {
        "channelCode": "IOXDELPC",
        "channelSecret": "LAD82PAYYCV3L9NK"
    },
    "version": "1"
}

response = requests.post(url_token, headers=header_token, data=json.dumps(data_token))
if response.status_code == 200:
    result = response.json()
    token = result['result']['token']
    print("获取token成功：", token)

for i in range(50):
    print("开始执行测试")
    # 调用batchSendMessage接口
    url_batch = "http://172.22.33.111:6061/sendMessage/batchSendMessage"
    name = str(random.randint(500, 4000))
    user_list = []

    for t in range(1000):
        user = {
            "appOpenId": "2882235392",
            "extras": {},
            "messageId": "messageId" + str(t),
            "phone": "13103838059",

            "wechatPublicParam": {
                "client_msg_id": "",
                "data": {
                    "character_string2": {
                        "value": "HO1111"
                    },
                    "character_string4": {
                        "value": "018115624741"
                    },
                    "phrase5": {
                        "value": "已出票"
                    },
                    "thing3": {
                        "value": "广州——北京"
                    },
                    "time1": {
                        "value": "2023年01月15日 08:40"
                    }
                },

                "url": "https://t-m.hoair.cn/flightSearch/search/index.html?barStyle=0",
                "wechatPublicOpenId": "o-nEn6H5H7WWCpdGd6xcJT-qWwG4"
            }
        }
        user_list.append(user)
    header_batch = {
        "accept": "*/*",
        "Content-Type": "application/json",
        "token": token
    }
    data_batch = {
        "bizNo": name,
        "request": {

            "aisleList": [

                "JXDYBGZH",
                "JXAPPDYB",
                "JXDYB"
            ],
            "batchId": "batch_2023_02_12_1" + name,
            "lastSendTime": "2023-02-12 21:00:00",
            "messageType": "ORDINARY",
            # ORDINARY 一般  URGENT 緊急
            "sendType": "ALL",
            "taskId": name,
            "requestMode": "API",
            "userList": user_list,
            "wechatPublicTemplateCode": "EhXP366nWXtol-cwyM4JJvEFmIdQPVZC9wfQKziLkkU",
            "appTemplateCode": "105769314346471424",
            "smsTemplateCode": "JYV5MKAA"
        },
        "version": "1.0"
    }
    batchResponse = requests.post(url_batch, headers=header_batch, json=data_batch)
    if batchResponse.status_code == 200:
        batchResult = batchResponse.json()
        print("第" + str(i+1) + "次：调用batchSendMessage成功：", batchResult)
    else:
        print("调用batchSendMessage失败：", batchResponse.status_code)
