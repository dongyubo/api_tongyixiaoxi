import requests
import json
import random
import threading


def est_api(url, headers, data, i):
    print(data)
    batchresponse = requests.post(url_batch, headers=header_batch, json=data_batch)
    data2 = batchresponse.json()
    if batchresponse.status_code == 200:
        batchResult = batchresponse.json()
        # print('当前执行的请求数据：', data_batch)
        print("第"+str(i)+"次：调用batchSendMessage成功：", batchResult)

    else:
        print("调用batchSendMessage失败：", batchresponse.status_code)


# # 获取token的请求
# url_token = "http://172.22.33.111:6061/auth/getToken"
# header_token = {'Content-Type': 'application/json'}
# data_token = {
#     "bizNo": str(random.randint(10000, 99999)),
#     "request": {
#         "channelCode": "IOXDELPC",
#         "channelSecret": "LAD82PAYYCV3L9NK"
#     },
#     "version": "1"
# }
#
# response = requests.post(url_token, headers=header_token, data=json.dumps(data_token))
# if response.status_code == 200:
#     result = response.json()
#     token = result['result']['token']
#
#     print("获取token成功：", token)
# # print('当前获取token执行的请求数据：', data_token)
for i in range(1):

    # response = requests.post(url_batch, headers=header_batch, data=json.dumps(data_batch))
    # print('当前执行的请求数据：', data_token)
    # print('当前执行的请求数据：', data_batch)

    print("开始执行测试")
    # for t in range(1):
    #     threads = []
    for i in range(1):
        # 调用batchSendMessage接口
        url_batch = "http://172.22.33.111:6061/sendMessage/batchSendMessage"
        name = str(random.randint(500, 4000))
        user_list = []

        for i in range(1000):
            user = {
                "appOpenId": "2882235392",
                "extras": {},
                "messageId": "messageId" + str(i),
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
            "token": "CCJj2rQTvc4nYhnmG2hse9WUFR8Z6Y3ySZOtJDOzf6onWzYlIiG8MXevD1toGPnbqrzoLe8guuZfdTS6I1G4ChH9O0OEcxzLzjO93Lb8kpiXOnVPu4GPhfDo66eQDUUy"
        }
        data_batch = {
            "bizNo": name,
            "request": {

                "aisleList": [

                    "JXDYBGZH",
                    "JXAPPDYB",
                    "JXDYB"
                ],
                "batchId": "batch_2023_02_11_" + name,
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
        thread = threading.Thread(target=est_api, args=(url_batch, header_batch, data_batch,i))
        #     threads.append(thread)
        # for t in threads:
        #     t.start()
        # for t in threads:
        #     t.join()

    # def est_api(url, data):
    #     response = requests.post(url, data=data)
    #     data2 = response.json()
    #     print(data)
    #     print(data2)
    #
    #
    # if __name__ == '__main__':
    #     url = 'http://172.22.33.111:6061/sendMessage/batchSendMessage'
    #     name = str(random.randint(1000, 10000))
    #     for t in range(1):
    #         threads = []
    #         for i in range(1):
    #             data = {{
    #                 "bizNo": "name",
    #                 "request": {
    #                     "strategyId": "name",
    #                     "aisleList": [
    #
    #                         "HO_SMS"
    #                     ],
    #                     "batchId": "batch_2023_02_06_+name",
    #                     "lastSendTime": "2023-02-10 21:00:00",
    #                     "messageType": "URGENT",
    #                     "sendType": "ALL",
    #                     "userList": [
    #                         {
    #                             "appOpenId": "H9OauXj7i2HZ9Z4DLv6T2_cs7_qHN0s",
    #                             "extras": {
    #                                 "flightDate": "2022-12-17",
    #                                 "flightNo": "HO1112",
    #                                 "name": "huang"
    #                             },
    #                             "messageId": "name",
    #                             "phone": "13103838059"
    #                         }
    #                     ],
    #                     "smsTemplateCode": "2QYLUNWP"
    #                 },
    #                 "version": "1.0"
    #             }}
    #             t = threading.Thread(target=est_api, args=(url, data))
    #             threads.append(t)
    #         for t in threads:
    #             t.start()
    #         for t in threads:
    #             t.join()
