# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:44
# @Author:Eric
# @File : Qiehao.py
# @Software: PyCharm
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

# def check_and_delay(ts):
#     time.sleep(ts)

if __name__ == '__main__':
    desired_caps = {
      'platformName': 'Android', # 被测手机是安卓
      'platformVersion': '11', # 手机安卓版本
      'deviceName': '009', # 设备名，安卓手机可以随意填写
      'appPackage': 'com.tencent.omapp',  # 启动APP Package名称
      'appActivity': '.ui.activity.SplashActivity',  # 启动Activity名称
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
    resourceId = 'com.tencent.omapp:id/publish_dialog_close'
    driver.find_element(By.ID, resourceId).click()

    # 点击添加视频
    time.sleep(6)
    resourceId = 'com.tencent.omapp:id/publish_dialog_video_ll'
    driver.find_element(By.ID, resourceId).click()

    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=150, y=350).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=500, y=350.perform()

    # 完成
    time.sleep(6)
    resourceId = 'com.tencent.omapp:id/preview_video_finish'
    driver.find_element(By.ID, resourceId).click()

    # 标题（不得少于5个字）
    time.sleep(6)
    text = '真可爱'
    resourceId = 'com.tencent.omapp:id/video_play_title_edit_text'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 选择分类
    time.sleep(6)
    resourceId = 'com.tencent.omapp:id/video_play_catalog_text_hint'
    driver.find_element(By.ID, resourceId).click()

    # 选择分支
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("动漫")').click()

    # 再选择分支
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("宅文化")').click()

    # 发布
    time.sleep(6)
    resourceId = 'com.tencent.omapp:id/video_upload_publish_btn'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)

    input('确定退出')

