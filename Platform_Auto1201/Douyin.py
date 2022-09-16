# coding=utf-8

# -*- codeing = utf-8 -*-
# @Time :2022/8/14 20:00
# @Author:Eric
# @File : Douyin.py
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
  'appPackage': 'com.ss.android.ugc.aweme',  # 启动APP Package名称
  'appActivity': '.splash.SplashActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'udid':'8d81a9d0',
  'automationName' : 'UiAutomator2'
}


def Add_Douyin_video():

    for i in range(2):
        driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)


        input('检查页面情况')

        # TouchAction(driver).tap(x=282, y=1237).perform()
        #点击+按钮
        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/pw2'
        driver.find_element(By.ID, resourceId).click()

        #TouchAction(driver).tap(x=960, y=2250).perform()

        #点击相册
        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/bh2'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)
        if i == 0:
        #选择第一个视频
            TouchAction(driver).tap(x=200, y=500).perform()
        elif i ==1:
            TouchAction(driver).tap(x=600, y=500).perform()

        #下一步
        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/k_q'
        driver.find_element(By.ID, resourceId).click()

        #作品描述
        time.sleep(1)
        text = '真可爱\n#美好'
        resourceId = 'com.ss.android.ugc.aweme:id/ept'
        driver.find_element(By.ID,resourceId).send_keys(text)

        # 返回编辑
        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/a8'
        driver.find_element(By.ID, resourceId).click()

        # 下一步
        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/k_q'
        driver.find_element(By.ID, resourceId).click()

        #发布
        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/mzo'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)
        #点击我
        resourceId = 'com.ss.android.ugc.aweme:id/pxb'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)
        resourceId = 'com.ss.android.ugc.aweme:id/s5-'
        fans = driver.find_element(By.ID, resourceId).text
        print('粉丝为：')
        print(fans)

        #播放量
        resourceId = 'com.ss.android.ugc.aweme:id/r45'
        play = driver.find_element(By.ID, resourceId).text
        print('播放量：',play)

    input('抖音执行完成')


if __name__ == '__main__':

    Add_Douyin_video()
    pass
