# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:46
# @Author:Eric
# @File : iQIYI.py
# @Software: PyCharm
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

# def check_and_delay(ts):
#     time.sleep(ts)


desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '11', # 手机安卓版本
  'deviceName': '009', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.qiyi.video',  # 启动APP Package名称
  'appActivity': '.WelcomeActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}


def Add_iQIYI_video():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 点击+按钮
    time.sleep(10)
    TouchAction(driver).tap(x=1000, y=145).perform()

    # 点击添加视频
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("上传/剪辑")').click()

    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=500, y=500).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=850, y=500.perform()

    # 去发布
    time.sleep(6)
    resourceId = 'com.qiyi.video.feature:id/sv_selected_next'
    driver.find_element(By.ID, resourceId).click()

    # 标题（不得少于5个字）
    time.sleep(6)
    text = '真可爱'
    resourceId = 'com.qiyi.video.feature:id/editPublishTitle'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 发布
    time.sleep(6)
    resourceId = 'com.qiyi.video.feature:id/buttonPublishFeed'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)

    input('爱奇艺执行完成')

if __name__ == '__main__':
    pass