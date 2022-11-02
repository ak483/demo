from selenium import webdriver
import time
import requests
import re
from My_code.Toolbox.Selenium import seleniumClass
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])

headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}

browser = webdriver.Chrome()
url = 'https://channels.weixin.qq.com/platform/post/list'
browser.get(url)
# browser.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()  # 通过这行代码可以自动切换成二维码模式，其实手动点也可以
time.sleep(20)  # 留20秒或者更长的时间来手动进行登录；推荐扫码登陆

def switch_(url):#url转换
    browser.switch_to.default_content()
    # 获取所有窗口句柄集合
    handles = browser.window_handles
    # 创建页面
    handles = seleniumClass().Create_New_Page(browser=browser, newPageUrl=url)

switch_(r'https://channels.weixin.qq.com/platform/post/list')
time.sleep(5)
cookies = browser.get_cookies()  # 获取Cookie
print(cookies)
cookie_dict = {}
for item in cookies:
    cookie_dict[item['name']] = item['value']

# 3.Requests库使用Cookie
url = 'https://channels.weixin.qq.com/platform/post/list'
res = requests.get(url, headers=headers, cookies=cookie_dict).text

print(res)