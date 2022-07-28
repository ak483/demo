# -*- codeing = utf-8 -*-
# @Time :2022/7/20 21:04
# @Author:Eric
# @File : 页面详情.py
# @Software: PyCharm
import requests
import re
from lxml import etree
import xlwt

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

def yutu():
    url = 'https://www.yutu.cn/question/tiwen_160155.html'
    print(url)
    r = requests.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    res=r.text
    print(res)
   #  title = re.findall('<p class="h2-tite">(.*?)</p>',res)
   #  href = re.findall('<a class="comm-item" target="_blank" href="(.*?)">',res)
   #  print(title)
   #  print(href)
    print('----------')

yutu()