# -*- codeing = utf-8 -*-
# @Time :2022/6/27 16:06
# @Author:Eric
# @File : 淘宝.py
# @Software: PyCharm
from selenium import webdriver
import time
import requests
import re
option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation'])

headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}

browser = webdriver.Chrome()
url = 'https://login.taobao.com/member/login.jhtml'
browser.get(url)
# browser.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()  # 通过这行代码可以自动切换成二维码模式，其实手动点也可以
time.sleep(20)  # 留20秒或者更长的时间来手动进行登录；推荐扫码登陆
cookies = browser.get_cookies()  # 获取Cookie

cookie_dict = {}
for item in cookies:
    cookie_dict[item['name']] = item['value']

# 3.Requests库使用Cookie
url = 'https://s.taobao.com/search?q=大码女装'
res = requests.get(url, headers=headers, cookies=cookie_dict).text

print(res)

# 4.正则表达式提取信息
title = re.findall('"raw_title":"(.*?)"', res)
price = re.findall('"view_price":"(.*?)"', res)
sale = re.findall('"view_sales":"(.*?)人付款"', res)

for i in range(len(title)):
    print(title[i] + '，价格为：' + price[i] + '，销量为：' + sale[i])