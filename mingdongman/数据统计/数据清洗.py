# import re
#
# douyin_data = '2022年09月05日 19:37'
# kuaishou_data = '发布于 2022-09-05 19:37:47'
# xiaohongshu_data = '发布于 2022-09-05'
# shipinhao_data = '2022/09/09'
# bilibili_data = '20-02-29 02:40:30'
#
# douyin_data = re.sub('年','/',douyin_data)
# douyin_data = re.sub('月','/',douyin_data)
# douyin_data = re.sub('日.*$','',douyin_data)
# print(douyin_data)
#
# kuaishou_data = re.sub('发布于 ','',kuaishou_data)
# kuaishou_data = re.sub('-','/',kuaishou_data)
# kuaishou_data = re.sub(' .*$','',kuaishou_data)
# print(kuaishou_data)
#
# xiaohongshu_data = re.sub('发布于 ','',xiaohongshu_data)
# xiaohongshu_data = re.sub('-','/',xiaohongshu_data)
# print(xiaohongshu_data)
#
#
# bilibili_data = re.sub('-','/',bilibili_data)
# bilibili_data = re.sub(' .*$','',bilibili_data)
# print(bilibili_data)
#
#
# shipinhao_time = '2.81秒'
# shipinhao = re.sub('\..*$','',shipinhao_time)
# print(shipinhao)
#
# xiaohongshu_time = '4min'
# xiaohongshu_time = re.sub('s','',xiaohongshu_time)
# if 'min' in xiaohongshu_time:
#     xiaohongshu_time = re.sub('min','',xiaohongshu_time)
#     xiaohongshu_time = int(xiaohongshu_time)*60
#
# print(xiaohongshu_time)
#
#
# kuaishou='+15'
# kuaishou = re.sub('\+','',kuaishou)
# print(kuaishou)
#
# a = '11.62%'
# print(a.strip("%"))
#

# coding=utf-8
FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
}

import pandas as pd
import requests,re,time
from lxml import html
etree = html.etree
from selenium.webdriver.common.by import By
from My_code.Toolbox.Selenium import seleniumClass
driver = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "cookie":"_did=web_14536971838C87B8; language=zh-CN; ud=22256115; account_id=15032681; soft_did=1619580708547; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_7858a2eb4853800d3e4273f895c8cb55; client_key=65890b29; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABiRCdFGwSJdc4ky7QF_eZ_R3CeDYby5Qmp_pPj3sQnlCxbnAAnh1fzO7O5Y6UmcGjBUvIt-Fae_RdjUj_VgGXlr9X2flehC640HJOdR4wdp1s-U0nrDGwsZIQ2pQJfN38dXsb7gH_ReHi31W6_B4bpXOGFfl8IuMJT9qlwNUsg3t_xE8BXYSmB6a7K9W7t-V51p_k8-3ErFFZKXJPA0sq_hoSdWlbobCW6oJxuQLJTUr9oj_uIiACKYeactlSXNS5KT-13xVz_o0b-ptK3VAQu66nfQaM4ygFMAE; kuaishou.server.web_ph=a4e8f2ec4f33528f4b6b732e6e4f1f1106c6"
}
driver.implicitly_wait(5)
kuaishou_All_video_url = []  # 存储所有账号的url
video_detaillist=[]


if __name__ == '__main__':

    for i in range(1):
        video_url = f'https://www.kuaishou.com/short-video/3xqzjrg65quj262?authorId=3xrtpifufrhwuii&streamSource=profile&area=profilexxnull'

        page_text = requests.get(url=video_url, headers=headers).text
        print(page_text)
        platform = '快手'
        title = re.findall('<title>(.*?)</title>', page_text)
        counter = re.findall('<title>(.*?)</title>', page_text)

        video_detaillist.append(title)
        video_detaillist.append(counter)
        video_detaillist.append(platform)
        video_detaillist.append(video_url)



        print(title)
    print(video_detaillist)

