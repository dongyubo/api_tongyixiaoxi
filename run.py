# -*- coding:utf-8 -*-
# @Time:2021/6/21 16:11
# @Author:lucky
# @Email:
# @File:run.py

from unittestreport import TestRunner
import unittest
from common.handle_path import testcases_dir,reports_dir
import time

from unittestreport.core.sendEmail import SendEmail # 定义邮件主题
import os

class RunTest:
    "程序入口函数"
    def run(self):
    # 将测试用例 加载到测试套件

        suite = unittest.defaultTestLoader.discover(testcases_dir)
        # 定义测试报告
        filename = "market_API_report"+"_"+ time.strftime("%Y%m%d%H%M%S")+".html"
        runner=TestRunner(suite, filename=filename,report_dir=reports_dir, title="market_API_report", tester="刘玲",desc="营销接口项目测试生成的报告")
        # 运行测试程序
        runner.run()

        # 发送结果到邮箱

        # runner.send_email(host='smtp.juneyaoair.com',
        #                   port='25',
        #                   user='itqc_notice@juneyaoair.com',
        #                   password='YH5ujjPf',
        #                   to_addrs='liuling2@juneyaoair.com', # 单个人字符串 ，多个地址时[]
        #                   is_file=True)


     # SendEmail类 ，设置邮件的主题，邮件内容
        # from unittestreport.core.sendEmail import SendEmail
        # em = SendEmail(host='',#服务器地址
        #                port='',#端口
        #                user='',#用户名
        #                password=''#密码
        #                )
        #主题，
        # em.send_email(subject='',content='',filename='',to_addrs='')

if __name__ == '__main__':
    test = RunTest()
    test.run()