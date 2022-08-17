# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:43
# @Author:Eric
# @File : Zhihu.py
# @Software: PyCharm
from appium import webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy


if __name__ == '__main__':
    desired_caps = {
      'platformName': 'Android', # 被测手机是安卓
      'platformVersion': '11', # 手机安卓版本
      'deviceName': '009', # 设备名，安卓手机可以随意填写
      'appPackage': 'com.ss.android.article.video',  # 启动APP Package名称
      'appActivity': '.activity.SplashActivity',  # 启动Activity名称
      'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
      'resetKeyboard': True, # 执行完程序恢复原来输入法
      'noReset': True,       # 不要重置App
      'skipServerInstallation': True,
      'newCommandTimeout': 6000,
      'automationName' : 'UiAutomator2'
    }


def Add_Bilibili_video():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 点击+按钮
    time.sleep(10)
    driver.find_element('-android uiautomator', 'new UiSelector().text("发视频")').click()

    # 点击添加视频
    time.sleep(6)
    resourceId = 'com.ss.android.article.video:id/f61'
    driver.find_element(By.ID, resourceId).click()


    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=150, y=500).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=500, y=500).perform()

    # 导入
    time.sleep(6)
    resourceId = 'com.ss.android.article.video:id/d4c'
    driver.find_element(By.ID, resourceId).click()

    # 下一步
    time.sleep(6)
    resourceId = 'com.ixigua.createbiz:id/media_edit_next'
    driver.find_element(By.ID, resourceId).click()

    # 填写标题
    time.sleep(6)
    text = '真可爱美好'
    resourceId = 'com.ixigua.createbiz:id/video_edit_title'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 发布
    time.sleep(6)
    resourceId = 'com.ixigua.createbiz:id/video_edit_publish'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)
    input('半次元执行完成')

if __name__ == '__main__':
    pass