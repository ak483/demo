# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:47
# @Author:Eric
# @File : Banciyuan.py
# @Software: PyCharm
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '11', # 手机安卓版本
  'deviceName': '009', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.banciyuan.bcywebview',  # 启动APP Package名称
  'appActivity': 'com.bcy.biz.stage.main.MainActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'udid':'576973a2',
  'automationName' : 'UiAutomator2'
}


def Add_Banciyuan_video():


    for i in range(2):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        input('检查页面情况')
        # 点击+号
        time.sleep(1)
        resourceId = 'com.banciyuan.bcywebview:id/aix'
        driver.find_element(By.ID, resourceId).click()

        #发视频
        time.sleep(1)
        driver.find_element('-android uiautomator', 'new UiSelector().text("发视频")').click()

        time.sleep(1)
        if i == 0:
        # 选择第一个视频
            TouchAction(driver).tap(x=200, y=450).perform()

        if i == 1:
        # 选择第二个视频
            TouchAction(driver).tap(x=550, y=450).perform()

        # 下一步
        time.sleep(1)
        resourceId = 'com.bcy.plugin.bve:id/bve_next'
        driver.find_element(By.ID, resourceId).click()

        # 再下一步
        time.sleep(1)
        resourceId = 'com.bcy.plugin.bve:id/bve_next'
        driver.find_element(By.ID, resourceId).click()

        # 输入标题
        time.sleep(1)
        text = '真可爱'
        resourceId = 'com.banciyuan.bcywebview:id/avm'
        driver.find_element(By.ID, resourceId).send_keys(text)

        time.sleep(1)
        driver.find_element('-android uiautomator', 'new UiSelector().text("自制")').click()

        # 再下一步
        time.sleep(20)
        resourceId = 'com.banciyuan.bcywebview:id/asz'
        driver.find_element(By.ID, resourceId).click()

        #标签
        time.sleep(1)
        driver.find_element('-android uiautomator', 'new UiSelector().text("请输入标签，多个标签用换行分割")').click()

        #输入标签
        time.sleep(1)

        # 文本存入剪贴板
        text = '你好啊'
        driver.set_clipboard_text(text)

        # 长按弹出粘贴按钮
        action = TouchAction(driver)
        action.long_press(x=80, y=280, duration=2000).release().perform()
        time.sleep(1)

        # 选择粘贴
        TouchAction(driver).tap(x=50, y=204).perform()

        # 发布
        time.sleep(1)
        resourceId = 'com.banciyuan.bcywebview:id/asz'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)
    input('半次元执行完成')

if __name__ == '__main__':

    Add_Banciyuan_video()

