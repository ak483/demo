
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import By
import time


class run():

  def __init__(self, i, b):
    self.i = i
    self.b = b

    # 链接移动设备必须的参数
    desired_caps = {}

    # 当前要测试的设备名称
    desired_caps["deviceName"] = "ww"

    # 系统
    desired_caps["platformName"] = "Android"

    # 系统的版本
    desired_caps["platformVersion"] = "11"

    # 要启动的app的名称（包名）
    desired_caps["appPackage"] = "com.ss.android.ugc.aweme"

    # 要启动app的那个界面
    desired_caps["appActivity"] = ".splash.SplashActivity"

    self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

  def __del__(self):
    print("完成，再见")

  # 滑动页面使可以找到其它元素
  def dianji(self):
    time.sleep(2)
    # 点击桌面抖音
    self.driver.find_element(By.XPATH, '//*[@text = "抖音"]').click()
    # 等待2秒打开时间
    time.sleep(3)

    action = TouchAction(self.driver)
    action.tap(x=200, y=550, count=1)
    action.perform()

    self.b = b
    # 点击搜索元素
    self.driver.find_element(By.XPATH, '//*[@resource-id = "com.ss.android.ugc.aweme:id/c0="]').click()
    time.sleep(1)
    # 点击输入框，并输入文字
    self.driver.find_element(By.XPATH, '//*[@resource-id = "com.ss.android.ugc.aweme:id/et_search_kw"]').send_keys(b)
    time.sleep(1)
    # 输入成功后点击搜索
    self.driver.find_element(By.XPATH, '//*[@resource-id = "com.ss.android.ugc.aweme:id/k4g"]').click()
    time.sleep(2)

    action.tap(x=200, y=550, count=1)
    action.perform()
    self.huadon()

  def huadon(self):
    self.i = i
    a = 0
    while i > a:
      a += 1
      print(f"运行次数{a}")

      time.sleep(3)
      action = TouchAction(self.driver)
      action.press(x=240, y=630).wait(200).move_to(x=266, y=200).release()
      action.perform()
      time.sleep(2)
      action.tap(x=505, y=616, count=1).perform()

  # # 关闭app
  # def guanbi(self):
  #     self.driver.close_app()
  #
  #     time.sleep(2)
  #     self.driver.quit()

  def main(self):
    print("正在运行，请稍等....")
    self.dianji()


if __name__ == '__main__':
  i = eval(input("输入刷视频次数："))
  b = input("输入要看的视频：")
  a = run(i, b)
  a.main()
