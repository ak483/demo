# coding=utf-8
from appium import webdriver
import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


# 延时与检测系统提示
def check_and_delay(ts=10):
    time.sleep(ts)
    # try:
    #     driver.find_element(By.ID,'android:id/button1').click()
    # except: pass

# 获得屏幕坐标x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

# 屏幕向上滑动
def swipeUp(t):
    local = getSize()
    x = int(local[0] * 0.75)
    y1 = int(local[1] * 0.75)
    y2 = int(local[1] * 0.25)
    driver.swipe(x, y1, x, y2, t)


if __name__ == '__main__':
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
      'udid': '576973a2',
      'automationName' : 'UiAutomator2'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    # 点击首页搜索框
    check_and_delay()
    resourceId = 'com.ss.android.ugc.aweme:id/hox'
    driver.find_element(By.ID,resourceId).click()
    check_and_delay()
    # 输入搜索内容
    text = '插画'
    resourceId = 'com.ss.android.ugc.aweme:id/et_search_kw'
    driver.find_element(By.ID,resourceId).send_keys(text)
    check_and_delay()
    # 点击搜索按钮
    resourceId = 'com.ss.android.ugc.aweme:id/r4i'
    driver.find_element(By.ID,resourceId).click()
    check_and_delay()


#点击屏幕
    TouchAction(driver).tap(x=282, y=1237).perform()

    check_and_delay(10)
    for t in range(10):

        # swipeUp(1000)
        # check_and_delay

        action = TouchAction(driver)
        action.press(x=240, y=1830).wait(200).move_to(x=340, y=1430).release()
        action.perform()

        time.sleep(random.randint(8, 30))


    # 关闭抖音
    # driver.quit()