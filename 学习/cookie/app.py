# -*- codeing = utf-8 -*-
# @Time :2022/6/30 19:47
# @Author:Eric
# @File : app.py
# @Software: PyCharm
from appium import webdriver
import time

desired_caps = {
    'newCommandTimeout': 3600,
    'platformName': 'Android',
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',
    'udid': '127.0.0.1:62001',
    'appPackage': 'com.tencent.mm',
    'appActivity':'.plugin.account.ui.LoginPasswordUI'
}

browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)