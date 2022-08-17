# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:45
# @Author:Eric
# @File : Youku.py
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
  'appPackage': 'com.youku.phone',  # 启动APP Package名称
  'appActivity': '.ActivityWelcome',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}


def Add_Youku_video():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 点击社区
    time.sleep(10)
    driver.find_element('-android uiautomator', 'new UiSelector().text("社区")').click()

    # 点击+按钮
    time.sleep(6)
    resourceId = 'com.youku.phone:id/publishPostIcon'
    driver.find_element(By.ID, resourceId).click()

    # 填写标题
    time.sleep(6)
    text = '真可爱美好'
    resourceId = 'com.youku.phone.UploadManagerAAR:id/edit_video_title'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 点击+按钮选择视频
    time.sleep(10)
    resourceId = 'com.youku.phone.UploadManagerAAR:id/publish_iv_add_image'
    driver.find_element(By.ID, resourceId).click()

    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=200, y=280).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=470, y=280).perform()

    # 确定
    time.sleep(6)
    resourceId = 'com.youku.phone:id/multi_commit'
    driver.find_element(By.ID, resourceId).click()

    # 接受协议
    time.sleep(6)
    resourceId = 'com.youku.phone.UploadManagerAAR:id/video_checkbox'
    driver.find_element(By.ID, resourceId).click()

    # 发布
    time.sleep(6)
    resourceId = 'com.youku.phone.UploadManagerAAR:id/tv_right'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)

    input('优酷执行完成')

if __name__ == '__main__':
    pass