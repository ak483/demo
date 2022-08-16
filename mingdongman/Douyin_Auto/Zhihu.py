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
      'appPackage': 'com.zhihu.android',  # 启动APP Package名称
      'appActivity': '.app.ui.activity.LauncherActivity',  # 启动Activity名称
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
    TouchAction(driver).tap(x=540, y=2220).perform()

    # 点击添加视频
    time.sleep(6)
    resourceId = 'com.zhihu.android:id/new_editor_drawee_iv'
    driver.find_element(By.ID, resourceId).click()


    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=600, y=320).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=1000, y=320.perform()

    # 下一步
    time.sleep(6)
    resourceId = 'com.zhihu.android:id/select_preview_next'
    driver.find_element(By.ID, resourceId).click()


    #点击屏幕
    time.sleep(6)
    text = '真可爱'

    # driver.press_keycode('9')
    driver.tap([(50,850)])

    time.sleep(6)
    driver.set_clipboard_text('你好呀')
    driver.get_clipboard_text()
    driver.send_sms()

    # 编辑想法
    # time.sleep(6)
    # text = '真可爱'
    # resourceId = 'com.zhihu.android:id/editorViewContainer'
    # driver.find_element(By.ID, resourceId).send_keys(text)



    # 发布
    time.sleep(6)
    resourceId = 'com.zhihu.android:id/publish'
    driver.find_element(By.ID, resourceId).click()


    input('确定退出')
