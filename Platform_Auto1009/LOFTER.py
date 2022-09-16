# -*- codeing = utf-8 -*-
# @Time :2022/8/15 7:47
# @Author:Eric
# @File : LOFTER.py
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
  'appPackage': 'com.lofter.android',  # 启动APP Package名称
  'appActivity': '.global.splash.HomeActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'udid':'576973a2',
  'automationName' : 'UiAutomator2'
}


def Add_LOFTER_video():

    for i in range(2):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        input('检查界面情况')

        # 点击+号
        resourceId = 'com.lofter.android:id/tab_icon4'
        driver.find_element(By.ID, resourceId).click()

        # 视频
        time.sleep(1)
        resourceId = 'com.lofter.android:id/video_post_icon'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)

        if i==0:
        #选择第一个视频
            TouchAction(driver).tap(x=100, y=300).perform()

        elif i==1:
        #选择第二个视频
            TouchAction(driver).tap(x=400, y=300).perform()

        # 下一步
        time.sleep(1)
        resourceId = 'com.lofter.android:id/video_next'
        driver.find_element(By.ID, resourceId).click()

        # 再下一步
        time.sleep(1)
        resourceId = 'com.lofter.android:id/video_next'
        driver.find_element(By.ID, resourceId).click()

        #点击标题坐标
        time.sleep(1)
        text = '你好啊'
        driver.set_clipboard_text(text)
        TouchAction(driver).tap(x=100, y=280).perform()

        # 输入标题
        time.sleep(1)
        resourceId = 'title'
        driver.find_element(By.ID, resourceId).send_keys(text)

        # 输入正文
        time.sleep(1)
        # 文本存入剪贴板
        text = '你好啊'
        driver.set_clipboard_text(text)

        # 长按弹出粘贴按钮
        action = TouchAction(driver)
        action.long_press(x=100, y=500).perform()
        time.sleep(1)

        # 选择粘贴
        TouchAction(driver).tap(x=50, y=300).perform()

        # 完成
        time.sleep(1)
        resourceId = 'com.lofter.android:id/back_nav_button'
        driver.find_element(By.ID, resourceId).click()

        #发布
        time.sleep(1)
        resourceId = 'com.lofter.android:id/tv_post_fabu'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(6)

    input('LOFTER执行完成')

if __name__ == '__main__':
    Add_LOFTER_video()
    pass
