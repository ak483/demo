# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:46
# @Author:Eric
# @File : Pipixia.py
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
  'appPackage': 'com.sup.android.superb',  # 启动APP Package名称
  'appActivity': 'com.sup.android.base.MainActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}


def Add_Pipixia_video():

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 点击+按钮
    time.sleep(10)
    resourceId = 'com.sup.android.superb:id/bck'
    driver.find_element(By.ID, resourceId).click()

    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=310, y=630).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=680, y=630).perform()

    # 下一步
    time.sleep(6)
    resourceId = 'com.sup.android.superb:id/p6'
    driver.find_element(By.ID, resourceId).click()

    # 完成
    time.sleep(6)
    resourceId = 'com.sup.android.module.mp:id/btn_premiere_finish'
    driver.find_element(By.ID, resourceId).click()

    #输入标题
    time.sleep(6)
    text = '真可爱'
    resourceId = 'com.sup.android.superb:id/a71'
    driver.find_element(By.ID, resourceId).send_keys(text)

    # 发布
    time.sleep(6)
    resourceId = 'com.sup.android.superb:id/bne'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)

    input('皮皮虾执行完成')

if __name__ == '__main__':
    pass
