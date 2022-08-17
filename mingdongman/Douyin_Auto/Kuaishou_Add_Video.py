# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:42
# @Author:Eric
# @File : Kuaishou_Add_Video.py
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
  'appPackage': 'com.smile.gifmaker',  # 启动APP Package名称
  'appActivity': 'com.yxcorp.gifshow.HomeActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'automationName' : 'UiAutomator2'
}


def Add_Bilibili_video():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(6)

    #点击屏幕
    TouchAction(driver).tap(x=282, y=1237).perform()

    #点击+按钮
    time.sleep(10)
    resourceId = 'com.smile.gifmaker:id/btn_shoot_white'
    driver.find_element(By.ID, resourceId).click()

    #点击相册
    time.sleep(6)
    resourceId = 'com.smile.gifmaker:id/button_album_frame'
    driver.find_element(By.ID, resourceId).click()
    time.sleep(6)

    #选择视频
    TouchAction(driver).tap(x=220, y=420).perform()


    # 下一步
    time.sleep(6)
    resourceId = 'com.smile.gifmaker:id/next_step'
    driver.find_element(By.ID, resourceId).click()

    # 再下一步
    time.sleep(6)
    resourceId = 'com.smile.gifmaker:id/next_step_button_text'
    driver.find_element(By.ID, resourceId).click()

    # 作品描述
    time.sleep(6)
    text = '真可爱\n#美好'
    resourceId = 'com.smile.gifmaker:id/editor'
    driver.find_element(By.ID, resourceId).send_keys(text)

    #发送
    time.sleep(6)
    resourceId = 'com.smile.gifmaker:id/publish_button'
    driver.find_element(By.ID, resourceId).click()
    time.sleep(6)

    input('半次元执行完成')

if __name__ == '__main__':
    pass