# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:43
# @Author:Eric
# @File : Xiaohongshu.py
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
  'appPackage': 'com.xingin.xhs',  # 启动APP Package名称
  'appActivity': '.index.v2.IndexActivityV2',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'udid':'576973a2',
  'automationName' : 'UiAutomator2'
}


def Add_Xiaohongshu_video():

    for i in range(2):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        input('检查界面情况')
        #点击+按钮
        resourceId = 'com.xingin.xhs:id/cdv'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)

        if i==0:
        # 选择第一个视频
            TouchAction(driver).tap(x=300, y=450).perform()

        elif i==1:
        #选择第二个视频
            TouchAction(driver).tap(x=300, y=450).perform()

        # 下一步
        time.sleep(1)
        resourceId = 'com.xingin.xhs:id/zo'
        driver.find_element(By.ID, resourceId).click()

        # 再下一步
        time.sleep(6)
        resourceId = 'com.xingin.xhs:id/bms'
        driver.find_element(By.ID, resourceId).click()

        # 标题
        time.sleep(1)
        text = '真可爱\n#美好'
        resourceId = 'com.xingin.xhs:id/b5f'
        driver.find_element(By.ID, resourceId).send_keys(text)

        # 正文
        time.sleep(1)
        text = '真可爱\n#美好'
        resourceId = 'com.xingin.xhs:id/b4_'
        driver.find_element(By.ID, resourceId).send_keys(text)

        #发送
        time.sleep(1)
        resourceId = 'com.xingin.xhs:id/a7l'
        driver.find_element(By.ID, resourceId).click()
        time.sleep(6)

    input('小红书执行完成')

if __name__ == '__main__':
    Add_Xiaohongshu_video()
    pass