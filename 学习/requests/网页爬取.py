# -*- codeing = utf-8 -*-
# @Time :2022/5/24 17:44
# @Author:Eric
# @File : 网页爬取.py
# @Software: PyCharm
import time
import requests
from lxml import etree
import re
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import datetime

headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}


def baidu(company):

    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&ie=utf-8&word='+company
    res = requests.get(url=url, headers=headers).text
    #print(res)
    tree = etree.HTML(res)
    print(tree)
    div_list = tree.xpath('//*[@id="content_left"]/div')

    #print(div_list)
    source = []
    date = []
    for div in div_list[1:]:
        # 来源
        source_t = div.xpath('./div/div/div[2]/div/a[1]/span/text()')
        if len(source_t) == 0:
            source_t = div.xpath('./div/div/div/div/a[1]/span/text()')

        source.append(source_t[0])

        # 时间
        date_t = div.xpath('./div/div/div[2]/span[1]/text()')
        if len(date_t) == 0:
            date_t = div.xpath('./div/div/div/span[1]/text()')
        date.append(date_t[0])

    print(source)

    for i in range(10):
        # 统一日期格式（参考5.1节）
        date[i] = re.sub('年', '-', date[i])
        date[i] = re.sub('月', '-', date[i])
        date[i] = re.sub('日', '', date[i])
        if ('小时前' in date[i])  or ('今天' in date[i]):

            date[i] = time.strftime("%Y-%m-%d")

        elif ('昨天' in date[i]):
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=1)
            print(type(yesterday))
            date[i] = yesterday.strftime("%Y-%m-%d")


        elif ('前天' in date[i]):
            today = datetime.date.today()
            yesterday = today - datetime.timedelta(days=2)
            print(type(yesterday))
            date[i] = yesterday.strftime("%Y-%m-%d")

    score = []
    keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '京东', '互联网']
    for i in range(len(title)):
        num = 0
        try:
            article = requests.get(href[i], headers=headers, timeout=10).text
        except:
            article = '爬取失败'

        try:
            article = article.encode('ISO-8859-1').decode('utf-8')
        except:
            try:
                article = article.encode('ISO-8859-1').decode('gbk')
            except:
                article = article
        p_article = '<p>(.*?)</p>'
        article_main = re.findall(p_article, article)  # 获取<p>标签里的正文信息
        article = ''.join(article_main)  # 将列表转换成为字符串
        for k in keywords:
            if (k in article) or (k in title[i]):
                num -= 5
        score.append(num)


companys = ['阿里巴巴']
for i in companys:
    baidu(i)

    print('成功！')