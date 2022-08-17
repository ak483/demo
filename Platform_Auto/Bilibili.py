# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:43
# @Author:Eric
# @File : Bilibili.py
# @Software: PyCharm
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

# def check_and_delay(ts):
#     time.sleep(ts)


desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '11', # 手机安卓版本
  'deviceName': '009', # 设备名，安卓手机可以随意填写
  'appPackage': 'tv.danmaku.bili',  # 启动APP Package名称
  'appActivity': '.MainActivityV2',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}


def Add_Bilibili_video():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #点击+按钮
    time.sleep(10)
    resourceId = 'tv.danmaku.bili:id/publish_remote_iv'
    driver.find_element(By.ID, resourceId).click()

    # 点击视频
    time.sleep(6)
    text = '视频'
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, text).click()
    time.sleep(6)

    # 选择第一个视频
    TouchAction(driver).tap(x=200, y=600).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=500, y=600.perform()

    # 去发布
    time.sleep(6)
    resourceId = 'tv.danmaku.bili:id/upper_material_preview_publish'
    driver.find_element(By.ID, resourceId).click()

    # 标题
    time.sleep(6)
    text = '真可爱'
    resourceId = 'tv.danmaku.bili:id/et_title'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 选择分区和标签
    time.sleep(6)
    resourceId = 'tv.danmaku.bili:id/tv_part'
    driver.find_element(By.ID, resourceId).click()

    #选择自定义标签
    # find_element_by_android_uiautomator
    driver.find_element('-android uiautomator', 'new UiSelector().text("自定义标签")').click()


    # 填写标签
    time.sleep(6)
    text = '美好'
    resourceId = 'tv.danmaku.bili:id/et_desc'
    driver.find_element(By.ID, resourceId).send_keys(text)

    #确定
    time.sleep(6)
    resourceId = 'tv.danmaku.bili:id/upper_tv_confirm'
    driver.find_element(By.ID, resourceId).click()

    # 再次点击确定
    time.sleep(6)
    resourceId = 'tv.danmaku.bili:id/upper_tv_confirm'
    driver.find_element(By.ID, resourceId).click()

    #选择自制类型
    TouchAction(driver).tap(x=620, y=1600).perform()


    # 发布
    time.sleep(6)
    resourceId = 'tv.danmaku.bili:id/tv_submit'
    driver.find_element(By.ID, resourceId).click()
    time.sleep(6)

    input('半次元执行完成')

if __name__ == '__main__':
    pass

