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



desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '11', # 手机安卓版本
  'deviceName': '009', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.sohu.sohuvideo',  # 启动APP Package名称
  'appActivity': '.ui.homepage.MainActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'udid':'576973a2',
  'automationName' : 'UiAutomator2'
}


def Add_Sohu_video():

    for i in range(2):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        input('检查界面情况')

        # 点击+按钮
        resourceId = 'com.sohu.sohuvideo:id/ib_publish'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)
        if i==0:
        # 选择第一个视频
            TouchAction(driver).tap(x=150, y=800).perform()
        elif i==1:
        # 选择第二个视频
            TouchAction(driver).tap(x=550, y=400).perform()

        # 下一步
        time.sleep(1)
        resourceId = 'com.sohu.sohuvideo:id/tv_next'
        driver.find_element(By.ID, resourceId).click()

        # 再次下一步
        time.sleep(1)
        TouchAction(driver).tap(x=900, y=1900).perform()

        #填写标题
        time.sleep(1)
        text = '真可爱美好'
        resourceId = 'com.sohu.sohuvideo:id/et_title'
        driver.find_element(By.ID, resourceId).send_keys(text)

        # 发布
        time.sleep(1)
        resourceId = 'com.sohu.sohuvideo:id/view_upload_text'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(6)

    input('搜狐执行完成')

if __name__ == '__main__':
    Add_Sohu_video()
    pass

