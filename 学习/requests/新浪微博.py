# -*- codeing = utf-8 -*-
# @Time :2022/6/30 2:07
# @Author:Eric
# @File : 新浪微博.py
# @Software: PyCharm
from selenium import webdriver
import time
import re

# 1.访问网址
url = "https://weibo.com/"
browser = webdriver.Chrome()
browser.get(url)  # 访问微博官网
browser.maximize_window()  # 需要全屏后才能显示那个登录框
time.sleep(30)  # 休息30秒，进行手动登录

# 2.访问环球时报官微
url = 'https://weibo.com/huanqiushibaoguanwei?is_all=1'  # 必须登录，直接访问是访问不了的，这里加上参数is_all=1，查看全部微博
browser.get(url)

data = (browser.page_source).encode('GBK', 'ignore')

print(data)

# 5.正则表达式提取所需内容
p_title = '<div class="WB_text W_f14" node-type="feed_list_content" nick-name="环球时报">(.*?)</div>'
title = re.findall(p_title, data_all, re.S)  # 这里用的是上面汇总的源代码data_all

# 6.打印结果
for i in range(len(title)):
    title[i] = title[i].strip()
    title[i] = re.sub('<.*?>', '', title[i])
    print(title[i])
