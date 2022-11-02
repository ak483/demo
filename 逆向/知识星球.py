from selenium import webdriver
import json, time
from selenium.webdriver.chrome.options import Options
url = 'https://wx.zsxq.com/dweb2/index/group/28512121211451'

options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=options)
driver.get(url)
driver.maximize_window()

# 使用Cookies登录
driver.delete_all_cookies()
f1 = open('damai_cookies.txt')
cookie =json.loads(f1.read())
f1.close()
for c in cookie:
    driver.add_cookie(c)
driver.refresh()
