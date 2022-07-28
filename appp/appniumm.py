# -*- codeing = utf-8 -*-
# @Time :2022/7/15 21:46
# @Author:Eric
# @File : appniumm.py
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '8.1.0', # 手机安卓版本
  'deviceName': 'ww', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
  'appActivity': '.MainActivityV2', # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'recreateChromeDriverSessions':True,
  'noReset': True,       # 不要重置App
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
  # 'app': r'd:\apk\bili.apk',
}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.quit
# 2.手动登录微信，然后选择一个好友，进入其朋友圈页面

# 3.获取微信朋友圈源代码+解析微信朋友圈
# data_all = ''
# text_all = []  # 1.构造一个空列表，存储页面元素的文本信息
# for i in range(20):
#     data_old = browser.page_source
#     data_all = data_all + data_old
#     a = browser.find_elements_by_id('com.tencent.mm:id/gbx')
#     for i in a:
#         text_all.append(i.text)  # 2.通过append()函数
#
#     browser.swipe(50, 1000, 50, 200)
#     time.sleep(2)
#
#     data_new = browser.page_source
#
#     if data_new == data_old:
#         break
#     else:
#         pass
#
# text_all = set(text_all)  # 3.通过set()函数进行去重
# for i in text_all:  # 4.打印去重后的内容
#     print(i)