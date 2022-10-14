# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, pyperclip, sys, re, logging, MySQLdb, random, os, xlwt
from lxml import html
etree = html.etree
sys.path.append(r'D:\untitled1')
from My_code.Toolbox.Selenium import seleniumClass

day = '2022/10/6'
savepath1 = r"D:\untitled1\demo\mingdongman\短视频Excel\统计视频7.xlsx"
FILE_PATH_DICT = {

    # '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',#实验账号
    # '浏览器个人配置': r'G:\Selenium_UserData\ZhiHu\one',#账号一
    # '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Artstation\one',#账号二
    # '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Pixiv\one',  # 账号三
    # '浏览器个人配置': r'G:\Selenium_UserData\BaiDu',#账号四 B站有数据
    # '浏览器个人配置': r'G:\Selenium_UserData\Bcy\one',#账号五 B站有数据
    # '浏览器个人配置': r'G:\Selenium_UserData\GuangWen',#账号六
    '浏览器个人配置': r'G:\Selenium_UserData\MooYoo',#账号七
    # '浏览器个人配置': r'G:\Selenium_UserData\SaiGao\one',#账号八
    # '浏览器个人配置': r'G:\Selenium_UserData\Tao_Bao',#账号九
    # '浏览器个人配置': r'G:\Selenium_UserData\Taobao_QingKeTang',#账号十
    # '浏览器个人配置': r'G:\Selenium_UserData\wangyi',#账号十一
    # '浏览器个人配置': r'G:\Selenium_UserData\WeiBo\one',#账号十二

    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '抖音url': r'https://creator.douyin.com/creator-micro/home',
    '快手url': r'https://cp.kuaishou.com/profile',
    '小红书url': r'https://creator.xiaohongshu.com/login',
    '视频号url': r'https://channels.weixin.qq.com/platform',
    'b站url': r'https://member.bilibili.com/platform/home',
}
All_datalist = []
All_datalist1 = []
browser = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
browser.implicitly_wait(5)

def douyin():

    browser.get('https://member.bilibili.com/platform/home')
    browser.maximize_window()
    time.sleep(1)
    name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
    platform = '抖音'
    browser.find_element(By.XPATH, '//span[text()="作品管理"]').click()
    while True:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(text(),"没有更多视频")]')))
            time.sleep(3)
            break
        except Exception:
            continue

    title = browser.find_elements(By.XPATH, '//div[@class="info-title-text--kEYth info-title-small-desc--tW-Ce"]')
    play = browser.find_elements(By.XPATH, '//div[@class="info-row--1OQ3-"]/div[1]/span')
    comment = browser.find_elements(By.XPATH, '//div[@class="info-row--1OQ3-"]/div[2]/span')
    approve = browser.find_elements(By.XPATH, '//div[@class="info-row--1OQ3-"]/div[3]/span')
    times = browser.find_elements(By.XPATH, '//div[@class="info-time--1PtPa"]')


    for i in range(len(title)):
        datalist = []
        datalist.append(day)
        datalist.append(title[i].text)    #标题
        datalist.append(name)
        datalist.append(platform)

        douyin_public_time = times[i].text
        douyin_public_time = re.sub('年', '/', douyin_public_time)
        douyin_public_time = re.sub('月', '/', douyin_public_time)
        douyin_public_time = re.sub('日.*$', '', douyin_public_time)

        datalist.append(douyin_public_time)  # 发布时间
        # 发布天数
        datalist.append('')
        #播放数据
        j = play[i].text
        if "w" in j:
            j = re.sub('w', '', j)
            j = float(j) * 10000
        datalist.append(int(j))      #播放

        datalist.append('') #完播率

        datalist.append('')#均播
        datalist.append(int(approve[i].text))  # 点赞

        if j == '0':
            approve_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve[i].text) / int(j)
            comment_rate = int(comment[i].text) / int(j)

        datalist.append(approve_rate)  # 点赞率
        datalist.append(int(comment[i].text))
        datalist.append(comment_rate)
        datalist.append('')#分享
        datalist.append('')#分享率
        datalist.append('')#视频带粉


        All_datalist.append(datalist)

def douyin_video():

    browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()

    time.sleep(1)
    name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
    platform = '抖音'

    browser.find_element(By.XPATH, '//span[text()="作品数据"]').click()

    Publish_time = browser.find_elements(By.XPATH, '//div[@class="date-text--2Aa6v"]')
    title = browser.find_elements(By.XPATH, '//div[@class="title-text--37-P9 first-text--2S8h2"]')
    play = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[3]//div[@class="number-text--1NhF0"]')
    finish_play = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[9]//div[@class="number-text--1NhF0"]')
    ave_time = ''
    approve = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[4]//div[@class="number-text--1NhF0"]')
    # approve_rate = '无法获取'
    comment = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[6]//div[@class="number-text--1NhF0"]')
    # comment_rate = "无法获取"
    share = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[5]//div[@class="number-text--1NhF0"]')
    # share_rate = "无法获取"
    Fans_raise = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[8]//div[@class="number-text--1NhF0"]')

    for i in range(len(title)):
        datalist = []
        datalist.append(day)
        datalist.append(title[i].text)
        datalist.append(name)
        datalist.append(platform)

        # 清洗发布时间
        douyin_public_time = Publish_time[i].text
        douyin_public_time = re.sub('年', '/', douyin_public_time)
        douyin_public_time = re.sub('月', '/', douyin_public_time)
        douyin_public_time = re.sub('日.*$', '', douyin_public_time)
        datalist.append(douyin_public_time)

        # 发布天数
        datalist.append('')

        # 播放数据
        j = play[i].text
        if "w" in j:
            j = re.sub('w', '', j)
            j = float(j) * 10000

        datalist.append(int(j))
        datalist.append(finish_play[i].text)
        datalist.append(ave_time)
        datalist.append(int(approve[i].text))
        if j == '0':
            approve_rate = 0
            share_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve[i].text) / int(j)
            share_rate = int(share[i].text) / int(j)
            comment_rate = int(comment[i].text) / int(j)

        datalist.append(approve_rate)  # 点赞率
        datalist.append(int(comment[i].text))
        datalist.append(comment_rate)
        datalist.append(int(share[i].text))
        datalist.append(share_rate)
        datalist.append(int(Fans_raise[i].text))
        All_datalist1.append(datalist)

def save1():
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('抖音', cell_overwrite_ok=True)
    col = ("数据日期", "视频标题", "所属账号", "所属平台", "发布日期", "发布天数", "播放量（总）", "完播率", "平均播放时长(s)", "点赞量（总）", "点赞率（点赞/播放）", "评论量（总）", "评论率（评论/播放）", "转发量（总）", "转发率（准发/播放）", "视频带粉数（总）")

    for i in range(0, 16):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        # print("第%d条" % (i + 1))
        data = All_datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath1)  # 保存

def save2():
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('抖音', cell_overwrite_ok=True)
    col = ("数据日期", "视频标题", "所属账号", "所属平台", "发布日期", "发布天数", "播放量（总）", "完播率", "平均播放时长(s)", "点赞量（总）", "点赞率（点赞/播放）", "评论量（总）", "评论率（评论/播放）", "转发量（总）", "转发率（准发/播放）", "视频带粉数（总）")

    for i in range(0, 16):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist1)):
        # print("第%d条" % (i + 1))
        data = All_datalist1[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath1)  # 保存


def shipinhao_video1():

    browser.get('https://channels.weixin.qq.com/platform')
    browser.maximize_window()

    browser.find_element(By.XPATH, '//span[text()="内容管理"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="动态管理"]').click()
    time.sleep(2)

    page = browser.find_elements(By.XPATH, '//span[@class="weui-desktop-pagination__num__wrp spread"]/label')#判断有多少页

    page_text = browser.page_source
    tree = etree.HTML(page_text)

    for l in range(len(page)+1):
        # title = browser.find_elements(By.CLASS_NAME, "post-title")
        # play = browser.find_elements(By.XPATH, '//div[@class="post-data"]/div[1]/span[2]').is_displayed()
        # print(play[1].is_displayed())
        # comment = browser.find_elements(By.XPATH, '//div[@class="post-data"]/div[3]/span[2]')
        # approve = browser.find_elements(By.XPATH, '//div[@class="post-data"]/div[2]/span[2]')
        # share = browser.find_elements(By.XPATH, '//div[@class="post-data"]/div[4]/span[2]')
        # times = browser.find_elements(By.XPATH, '//div[@class="post-time"]/span')

        title = tree.xpath('//div[@class="post-title"]')
        play = tree.xpath('//div[@class="post-data"]/div[1]/span[2]')
        comment = tree.xpath('//div[@class="post-data"]/div[3]/span[2]')
        approve = tree.xpath('//div[@class="post-data"]/div[2]/span[2]')
        share = tree.xpath('//div[@class="post-data"]/div[4]/span[1]')
        times = tree.xpath('//div[@class="post-time"]/span')


        for i in range(len(title)):
            datalist = []
            datalist.append(title[i].text)
            j = play[i].text
            if "w" in j:
                j = re.sub('w', '', j)
                j = float(j) * 10000
            datalist.append(int(j))
            datalist.append(int(comment[i].text))
            datalist.append(int(approve[i].text))
            datalist.append(int(share[i].text))
            datalist.append(times[i].text)
            All_datalist.append(datalist)
            # browser.find_element(By.XPATH, '//a[text()="下一页"]').click()
            time.sleep(1)
    print(All_datalist)



if __name__ == '__main__':

    # douyin()
    # douyin_video()
    shipinhao()
    # for i in range(len(All_datalist1)):
    #     All_datalist[i]=All_datalist1[i]
    # save1()
    print(All_datalist)
    # print(All_datalist1)