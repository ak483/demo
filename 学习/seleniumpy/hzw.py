# -*- codeing = utf-8 -*-
# @Time :2022/7/12 23:30
# @Author:Eric
# @File : hzw.py
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
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
# browser.get("https://www.baidu.com/")
browser.get("https://pixiviz.pwp.app/")
data = browser.page_source
print(data)
