# -*- codeing = utf-8 -*-
# @Time :2022/7/24 19:00
# @Author:Eric
# @File : 王玉涛.py
# @Software: PyCharm
from appium import webdriver
import time
import os

desired_caps = {
    'newCommandTimeout': 3600,
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'udid': '127.0.0.1:62001',
    'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
    'appActivity': '.MainActivityV2',  # 启动Activity名称
}



browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)