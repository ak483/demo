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


# def check_and_delay(ts):
#     time.sleep(ts)

if __name__ == '__main__':
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
      'automationName' : 'UiAutomator2'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 点击+号
    time.sleep(6)
    resourceId = 'com.banciyuan.bcywebview:id/aix'
    driver.find_element(By.ID, resourceId).click()

    #发视频
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("发视频")').click()

    # 选择第一个视频
    time.sleep(6)
    TouchAction(driver).tap(x=200, y=450).perform()

    # 选择第二个视频
    # TouchAction(driver).tap(x=550, y=450).perform()

    # 下一步
    time.sleep(6)
    resourceId = 'com.bcy.plugin.bve:id/bve_next'
    driver.find_element(By.ID, resourceId).click()

    # 再下一步
    time.sleep(6)
    resourceId = 'com.bcy.plugin.bve:id/bve_next'
    driver.find_element(By.ID, resourceId).click()

    # 输入标题
    time.sleep(6)
    text = '真可爱'
    resourceId = 'com.banciyuan.bcywebview:id/avm'
    driver.find_element(By.ID, resourceId).send_keys(text)

    time.sleep(30)
    driver.find_element('-android uiautomator', 'new UiSelector().text("自制")').click()

    # 再下一步
    time.sleep(6)
    resourceId = 'com.banciyuan.bcywebview:id/asz'
    driver.find_element(By.ID, resourceId).click()

    #标签
    time.sleep(6)
    driver.find_element('-android uiautomator', 'new UiSelector().text("请输入标签，多个标签用换行分割")').click()


    time.sleep(6)
    # driver.find_element('-android uiautomator', 'new UiSelector().text("添加标签")').send_keys(text)

    # code = 'new UiSelector().className("android.view.ViewGroup").childSelector(new UiSelector().className("android.widget.TextView"))'
    #
    # # code = 'new UiSelector().className("android.widget.TextView")'
    # ele = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, code)
    # ele.send_keys(text)

    #输入标签
    time.sleep(6)
    # 文本存入剪贴板
    text = '你好啊'
    driver.set_clipboard_text(text)

    # 长按弹出粘贴按钮
    action = TouchAction(driver)

    action.long_press(x=80, y=280, duration=2000).release().perform()
    time.sleep(6)

    # 选择粘贴
    TouchAction(driver).tap(x=50, y=204).perform()

    # 发布
    time.sleep(6)
    resourceId = 'com.banciyuan.bcywebview:id/asz'
    driver.find_element(By.ID, resourceId).click()

    time.sleep(6)

    input('确定退出')
