# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:44
# @Author:Eric
# @File : Wangyi.py
# @Software: PyCharm
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

# def check_and_delay(ts):
#     time.sleep(ts)

if __name__ == '__main__':
    desired_caps = {
      'platformName': 'Android', # 被测手机是安卓
      'platformVersion': '11', # 手机安卓版本
      'deviceName': '009', # 设备名，安卓手机可以随意填写
      'appPackage': 'com.netease.newsreader.activity',  # 启动APP Package名称
      'appActivity': 'com.netease.nr.biz.ad.newAd.AdActivity',  # 启动Activity名称
      'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
      'resetKeyboard': True, # 执行完程序恢复原来输入法
      'noReset': True,       # 不要重置App
      'skipServerInstallation': True,
      'newCommandTimeout': 6000,
      'automationName' : 'UiAutomator2'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


     # 点击+按钮
    time.sleep(10)
    resourceId = 'com.netease.newsreader.activity:id/anl'
    driver.find_element(By.ID, resourceId).click()

    # 作品描述
    time.sleep(6)
    text = '真可爱\n#美好'
    resourceId = 'com.netease.newsreader.activity:id/bel'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 点击+添加视频
    time.sleep(6)
    TouchAction(driver).tap(x=150, y=650).perform()


    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=500, y=250).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=750, y=270.perform()

    # 继续
    time.sleep(6)
    resourceId = 'com.netease.newsreader.activity:id/l8'
    driver.find_element(By.ID, resourceId).click()

    # 发布
    driver.find_element('-android uiautomator', 'new UiSelector().text("发布")').click()

    time.sleep(6)
    input('确定退出')