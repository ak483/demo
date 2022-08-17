# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:46
# @Author:Eric
# @File : AcFun.py
# @Software: PyCharm
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

# def check_and_delay(ts):
#     time.sleep(ts)

if __name__ == '__main__':
    desired_caps = {
      'platformName': 'Android', # 被测手机是安卓
      'platformVersion': '11', # 手机安卓版本
      'deviceName': '009', # 设备名，安卓手机可以随意填写
      'appPackage': 'tv.acfundanmaku.video',  # 启动APP Package名称
      'appActivity': 'tv.acfun.core.module.splash.SplashActivity',  # 启动Activity名称
      'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
      'resetKeyboard': True, # 执行完程序恢复原来输入法
      'noReset': True,       # 不要重置App
      'skipServerInstallation': True,
      'newCommandTimeout': 6000,
      'automationName' : 'UiAutomator2'
    }


    def Add_video():
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        #点击我的
        time.sleep(10)
        driver.find_element('-android uiautomator', 'new UiSelector().text("我的")').click()

        # 点击发布
        time.sleep(6)
        resourceId = 'tv.acfundanmaku.video:id/mineContributionView'
        driver.find_element(By.ID, resourceId).click()

        # 点击视频
        time.sleep(6)
        TouchAction(driver).tap(x=190, y=1842).perform()

        # 选择第一个视频
        time.sleep(6)
        TouchAction(driver).tap(x=160, y=264).perform()

        # 选择第二个视频
        # TouchAction(driver).tap(x=680, y=630).perform()

        # 下一步
        time.sleep(6)
        resourceId = 'tv.acfundanmaku.video:id/tvNextStep'
        driver.find_element(By.ID, resourceId).click()

        # 再下一步
        time.sleep(6)
        resourceId = 'tv.acfundanmaku.video:id/tvNextStep'
        driver.find_element(By.ID, resourceId).click()

        # 确定
        time.sleep(6)
        resourceId = 'tv.acfundanmaku.video:id/tvConfirm'
        driver.find_element(By.ID, resourceId).click()

        # 输入标题
        time.sleep(6)
        text = '真可爱'
        resourceId = 'tv.acfundanmaku.video:id/uploadVideoNameEdit'
        driver.find_element(By.ID, resourceId).send_keys(text)

        # 发布
        time.sleep(6)
        resourceId = 'tv.acfundanmaku.video:id/tvUpload'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(6)
        driver.find_element('-android uiautomator', 'new UiSelector().text("动画综合")').click()

        # 发布
        time.sleep(6)
        resourceId = 'tv.acfundanmaku.video:id/tvUpload'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(6)

        input('AcFun执行完成')
