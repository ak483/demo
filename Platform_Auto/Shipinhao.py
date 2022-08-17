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


desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '11', # 手机安卓版本
  'deviceName': '009', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.tencent.mm',  # 启动APP Package名称
  'appActivity': '.ui.LauncherUI',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}


def Add_Shipinhao_video():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    # 点击发现
    time.sleep(10)
    driver.find_element('-android uiautomator', 'new UiSelector().text("发现")').click()

    # 点击视频号
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("视频号")').click()

    # 点击个人主页
    time.sleep(6)
    resourceId = 'com.tencent.mm:id/huj'
    driver.find_element(By.ID, resourceId).click()

    #滑动屏幕
    time.sleep(6)
    action = TouchAction(driver)
    action.press(x=240, y=1830).wait(200).move_to(x=340, y=1430).release()
    action.perform()

    # 发表视频
    time.sleep(6)
    resourceId = 'com.tencent.mm:id/e43'
    driver.find_element(By.ID, resourceId).click()

    # 从相册选择
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("从相册选择")').click()

    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=210, y=260).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=480, y=260).perform()

    # 下一步
    time.sleep(6)
    resourceId = 'com.tencent.mm:id/en'
    driver.find_element(By.ID, resourceId).click()

    # 完成
    time.sleep(6)
    resourceId = 'com.tencent.mm:id/kl6'
    driver.find_element(By.ID, resourceId).click()

    # 添加描述
    time.sleep(6)
    text = '真可爱'
    resourceId = 'com.tencent.mm:id/i02'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 发表
    time.sleep(6)
    resourceId = 'com.tencent.mm:id/e4b'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)

    input('视频号执行完成')

if __name__ == '__main__':
    pass

