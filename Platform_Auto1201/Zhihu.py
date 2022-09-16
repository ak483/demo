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
  'appPackage': 'com.zhihu.android',  # 启动APP Package名称
  'appActivity': '.app.ui.activity.LauncherActivity',  # 启动Activity名称
  'unicodeKeyboard': True, # 使用自带输入法，输入中文时填True
  'resetKeyboard': True, # 执行完程序恢复原来输入法
  'noReset': True,       # 不要重置App
  'skipServerInstallation': True,
  'newCommandTimeout': 6000,
  'udid':'8d81a9d0',
  'automationName' : 'UiAutomator2'
}

def Add_Zhihu_video():

    for i in range(2):
        driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)

        input('检查界面情况')
        # 点击+按钮
        TouchAction(driver).tap(x=540, y=2220).perform()

        # 点击添加视频
        time.sleep(1)
        resourceId = 'com.zhihu.android:id/new_editor_drawee_iv'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)

        if i==0:
        # 选择第一个视频
            TouchAction(driver).tap(x=600, y=320).perform()

        elif i==1:
        # 选择第二个视频
            TouchAction(driver).tap(x=1000, y=320).perform()

        # 下一步
        time.sleep(1)
        resourceId = 'com.zhihu.android:id/select_preview_next'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(1)
        #文本存入剪贴板
        text='你好啊'
        driver.set_clipboard_text(text)

        # 长按屏幕
        action = TouchAction(driver)
        action.long_press(x=50,y=850).perform()
        time.sleep(1)

        # 选择粘贴
        TouchAction(driver).tap(x=50, y=655).perform()

        # 发布
        time.sleep(1)
        resourceId = 'com.zhihu.android:id/publish'
        driver.find_element(By.ID, resourceId).click()

        time.sleep(6)

    input('知乎执行完成')

if __name__ == '__main__':
    Add_Zhihu_video()
    pass
