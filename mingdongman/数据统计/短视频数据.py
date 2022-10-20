from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, pyperclip, sys, re, logging, MySQLdb, random, os,xlwt
import pyautogui as pag
import pandas as pd

sys.path.append(r'D:\untitled1')
from My_code.Toolbox.Selenium import seleniumClass
All_datalist = []

savepath = r"D:\untitled1\demo\mingdongman\短视频Excel\短视频账号6.xlsx"
day='2022/09/27'
FILE_PATH_DICT = {

    # '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',#实验账号
    # '浏览器个人配置': r'G:\Selenium_UserData\ZhiHu\one',#账号一
    # '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Artstation\one',#账号二
    # '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Pixiv\one',#账号三
    # '浏览器个人配置': r'G:\Selenium_UserData\BaiDu',#账号四
    # '浏览器个人配置': r'G:\Selenium_UserData\Bcy\one',#账号五
    '浏览器个人配置': r'G:\Selenium_UserData\GuangWen',#账号六
    # '浏览器个人配置': r'G:\Selenium_UserData\MooYoo',#账号七
    # '浏览器个人配置': r'G:\Selenium_UserData\SaiGao\one',#账号八
    # '浏览器个人配置': r'G:\Selenium_UserData\Tao_Bao',#账号九
    # '浏览器个人配置': r'G:\Selenium_UserData\Taobao_QingKeTang',#账号十
    # '浏览器个人配置': r'G:\Selenium_UserData\wangyi',#账号十一
    # '浏览器个人配置': r'G:\Selenium_UserData\WeiBo\one',#账号十二

    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '发布窗口': '',
    '编辑器': '',
    '抖音url': r'https://creator.douyin.com/creator-micro/home',
    '快手url': r'https://cp.kuaishou.com/profile',
    '小红书url': r'https://creator.xiaohongshu.com/login',
    '视频号url': r'https://channels.weixin.qq.com/platform',
    'b站url':  r'https://member.bilibili.com/platform/home',
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-知乎.xlsx',
    '封面图片路径': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\微信图片_20220518142115.png',
    '标题保存': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\标题2.xlsx',
    '外链列表': r'C:\Users\Adminitrator03\Desktop\短视频日报.xlsx',
}
browser = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
browser.implicitly_wait(5)

def Selenium_Login():
    # 实例化浏览器
    douyin()
    switch_(FILE_PATH_DICT['快手url'])
    kuaishou()
    switch_(FILE_PATH_DICT['小红书url'])
    xiaohongshu()
    switch_(FILE_PATH_DICT['视频号url'])
    shipinhao()
    # switch_(FILE_PATH_DICT['b站url'])
    # bilibili()

    # print(All_datalist)
    browser.quit()


    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('抖音', cell_overwrite_ok=True)
    col = ("数据日期","视频标题","所属账号","所属平台","发布日期","发布天数","播放量（总）","完播率","平均播放时长(s)","点赞量（总）","点赞率（点赞/播放）","评论量（总）","评论率（评论/播放）","转发量（总）","转发率（准发/播放）","视频带粉数（总）")

    for i in range(0, 16):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        # print("第%d条" % (i + 1))
        data = All_datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

    # (pd.DataFrame({
    #     '文章标题': bilibiliTitleList, '文章链接：': bilibiliUrlList
    # })).to_excel(FILE_PATH_DICT['标题保存'], index=False)

def switch_(url):
    browser.switch_to.default_content()
    # 获取所有窗口句柄集合
    handles = browser.window_handles
    # 创建页面
    handles = seleniumClass().Create_New_Page(browser=browser, newPageUrl=url)
        # # 获取发布页面的窗口ID
        # FILE_PATH_DICT['发布窗口'] = handles[0]
        # FILE_PATH_DICT['编辑器'] = handles[1]



def douyin():

    browser.get('https://creator.douyin.com/creator-micro/home')
    browser.maximize_window()

    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="发布视频"]')))
            time.sleep(3)
            break
        except Exception:
            continue
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

        #清洗发布时间
        douyin_public_time = Publish_time[i].text
        douyin_public_time = re.sub('年', '/', douyin_public_time)
        douyin_public_time = re.sub('月', '/', douyin_public_time)
        douyin_public_time = re.sub('日.*$', '', douyin_public_time)
        datalist.append(douyin_public_time)

        #发布天数
        datalist.append('')

        #播放数据
        j = play[i].text
        if "w" in j:
            j = re.sub('w','',j)
            j = float(j)*10000

        datalist.append(int(j))
        datalist.append(finish_play[i].text)
        datalist.append(ave_time)
        datalist.append(int(approve[i].text))
        datalist.append(int(approve[i].text)/int(j))#点赞率
        datalist.append(int(comment[i].text))
        datalist.append(int(comment[i].text)/int(j))
        datalist.append(int(share[i].text))
        datalist.append(int(share[i].text)/int(j))
        datalist.append(int(Fans_raise[i].text))
        All_datalist.append(datalist)


def kuaishou():

    # browser.get('https://cp.kuaishou.com/profile')
    # browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(text(),"发布视频")]')))
            time.sleep(3)
            break
        except Exception:
            continue
    platform = "快手"
    name = browser.find_element(By.XPATH, '//div[@class="detail__name"]').text

    time.sleep(1)
    # browser.find_element(By.XPATH, '//span[contains(text(),"数据中心")]').click()
    # time.sleep(1)
    browser.find_element(By.XPATH, '//li[contains(text(),"视频数据")]').click()
    time.sleep(1)

    Publish_time = browser.find_elements(By.XPATH, '//div[@class="video-item__info__detail__date"]')
    title = browser.find_elements(By.XPATH, '//div[@class="video-item__info__detail__title__content"]')
    play = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[1]/div[2]')
    finish_play = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[2]/div[2]')
    ave_time = ''
    approve = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[5]/div[2]')
    # approve_rate = int(approve)/int(play)
    comment = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[4]/div[2]')
    # comment_rate = int(comment)/int(play)
    share = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[6]/div[2]')
    # share_rate = int(share)/int(play)
    Fans_raise = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[3]/div[2]')

    for i in range(len(title)):
        datalist = []
        datalist.append(day)
        datalist.append(re.sub(' ','',title[i].text))
        datalist.append(name)
        datalist.append(platform)

        #清洗发布时间
        kuaishou_public_time = Publish_time[i].text
        kuaishou_public_time = re.sub('发布于 ', '', kuaishou_public_time)
        kuaishou_public_time = re.sub('-', '/', kuaishou_public_time)
        kuaishou_public_time = re.sub(' .*$', '', kuaishou_public_time)

        datalist.append(kuaishou_public_time)
        #发布天数
        datalist.append('')
        j = play[i].text
        if "万" in j:
            j = re.sub('万', '', j)
            j = int(float(j) * 10000)
        j = re.sub(',', '', str(j))

        datalist.append(int(j))
        datalist.append(finish_play[i].text)
        datalist.append(ave_time)
        a = approve[i].text
        if "万" in a:
            a = re.sub('万', '', a)
            a = int((float(a),) * 10000)
        a = re.sub(',', '', str(a))

        datalist.append(int(a))
        datalist.append(int(a) / int(j))  # 点赞率
        b = (comment[i].text)
        if "万" in b:
            b = re.sub('万', '', b)
            b = int(float(b) * 10000)
        b = re.sub(',', '', (b))

        datalist.append(int(b))
        datalist.append(int(b) / int(j))
        c = (share[i].text)
        if "万" in c:
            c = re.sub('万', '', c)
            c = int(float(c) * 10000)
        c = re.sub(',', '', str(c))

        datalist.append(int(c))
        datalist.append(int(c) / int(j))
        d = Fans_raise[i].text
        if "万" in d:
            d = re.sub('万', '', d)
            d = int(float(d) * 10000)
        d = re.sub(',', '', str(d))
        datalist.append(int(d))

        All_datalist.append(datalist)


def bilibili():

    # browser.get('https://member.bilibili.com/platform/home')
    # browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
            time.sleep(3)
            break
        except Exception:
            continue

    platform = "b站"
    browser.find_element(By.XPATH, '// a[contains(text(), "电磁力")]').click()
    time.sleep(1)
    name = browser.find_element(By.XPATH, '//span[@class="up-info-name"]').text
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[contains(text(),"内容管理")]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[contains(text(),"稿件管理")]').click()
    time.sleep(1)

    Publish_time = browser.find_elements(By.XPATH, '//div[@class="pubdate is-success"]/span')
    title = browser.find_elements(By.XPATH, '//div[@class="meta-title"]/a')
    play = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[1]//span')
    finish_play = ''
    ave_time = ''
    approve = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[6]//span')
    # approve_rate = int(approve) / int(play)
    comment = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[3]//span')
    # comment_rate = int(comment) / int(play)
    share = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[7]//span')
    # share_rate = int(share) / int(play)
    Fans_raise = ''

    for i in range(len(title)):
        datalist = []
        datalist.append(day)
        datalist.append(title[i].text)
        datalist.append(name)
        datalist.append(platform)

        #发布时间清洗
        bilibili_public_time = Publish_time[i].text
        bilibili_public_time = re.sub('-', '/', bilibili_public_time)
        bilibili_public_time = re.sub(' .*$', '', bilibili_public_time)
        bilibili_public_time = '20'+ bilibili_public_time

        datalist.append(bilibili_public_time)
        datalist.append('')
        j = play[i].text
        if "w" in j:
            j = re.sub('w', '', j)

            j = float(j) * 10000

        datalist.append(int(j))
        datalist.append(finish_play)
        datalist.append(ave_time)
        datalist.append(int(approve[i].text))
        datalist.append(int(approve[i].text) / int(j))  # 点赞率
        datalist.append(int(comment[i].text))
        datalist.append(int(comment[i].text) / int(j))
        datalist.append(int(share[i].text))
        datalist.append(int(share[i].text) / int(j))
        datalist.append(Fans_raise)
        All_datalist.append(datalist)

def xiaohongshu():

    #抓取的是近7日的
    # browser.get('https://creator.xiaohongshu.com/login')
    # browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//a[text()="发布笔记"]')))
            time.sleep(3)
            break
        except Exception:
            continue

    # time.sleep(1)
    # browser.find_element(By.XPATH, '//div[text()="数据看板"]').click()
    name = browser.find_element(By.XPATH, '//span[@class="name-box"]').text
    platform = '小红书'
    time.sleep(2)
    browser.find_element(By.XPATH, '//div[contains(text(),"笔记数据")]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//input[@readonly]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//div[contains(text(),"48条")]').click()
    time.sleep(1)

    Publish_time = browser.find_elements(By.XPATH, '//span[@class="publish-time"]')
    title = browser.find_elements(By.XPATH, '//span[@class="title"]')
    play = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[1]/b')
    finish_play = ''
    ave_time = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[2]/b')
    approve = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[3]/b')
    # approve_rate = int(approve) / int(play)
    comment = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[1]/b')
    # comment_rate = int(comment) / int(play)
    share = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[3]/b')
    # share_rate = int(share) / int(play)
    Fans_raise = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[4]/b')

    for i in range(len(title)):
        datalist = []
        datalist.append(day)
        datalist.append(title[i].text)
        datalist.append(name)
        datalist.append(platform)
        xiaohongshu_public_time = Publish_time[i].text
        xiaohongshu_public_time = re.sub('发布于 ', '', xiaohongshu_public_time)
        xiaohongshu_public_time = re.sub('-', '/', xiaohongshu_public_time)

        datalist.append(xiaohongshu_public_time)
        datalist.append('')
        j = play[i].text
        if "w" in j:
            j = re.sub('w', '', j)

            j = float(j) * 10000
        datalist.append(int(j))#播放量
        datalist.append(finish_play)
        ave_times = ave_time[i].text
        ave_times = re.sub('s', '', ave_times)
        if 'min' in ave_times:
            ave_times = re.sub('min', '', ave_times)
            ave_times = int(ave_times) * 60
        datalist.append(int(ave_times))
        datalist.append(int(approve[i].text))
        datalist.append(int(approve[i].text) / int(j))  # 点赞率
        datalist.append(int(comment[i].text))
        datalist.append(int(comment[i].text) / int(j))
        datalist.append(int(share[i].text))
        datalist.append(int(share[i].text) / int(j))
        datalist.append(int(Fans_raise[i].text))
        All_datalist.append(datalist)

def shipinhao():

    browser.get('https://channels.weixin.qq.com/platform')
    browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
            time.sleep(3)
            break
        except Exception:
            continue
    platform = '视频号'
    name = browser.find_element(By.XPATH, '//h2').text

    # time.sleep(2)
    # browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
    # time.sleep(2)
    # browser.find_element(By.XPATH, '//span[text()="动态数据"]').click()
    # time.sleep(2)
    # browser.find_element(By.XPATH, '//a[contains(text(),"单篇动态")]').click()
    # time.sleep(2)
    # browser.find_element(By.XPATH, '//span[contains(text(),"近30天数据")]').click()

    browser.find_element(By.XPATH, '//span[text()="内容管理"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="动态管理"]').click()
    time.sleep(2)
    page = browser.find_elements(By.XPATH, '//span[@class="weui-desktop-pagination__num__wrp spread"]/label')  # 判断有多少页

    # browser.switch_to.(browser.find_element(By.XPATH,'//div[@class="post-view router-view"]'))


    play = browser.find_elements('//div[@class="post-data"]/div[1]/span[2]')
    comment = browser.find_elements('//div[@class="post-data"]/div[3]/span[2]')
    approve = browser.find_elements('//div[@class="post-data"]/div[2]/span[2]')
    share = browser.find_elements('//div[@class="post-data"]/div[4]/span[1]')
    Publish_time = browser.find_elements('//div[@class="post-time"]/span')



    Publish_time = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[2]')
    title = browser.find_elements(By.XPATH, '//div[@class="post-wrap"]/span')
    play = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[5]')
    finish_play = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[3]')
    ave_time = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[4]')
    approve = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[6]')
    # approve_rate = int(approve) / int(play)
    comment = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[7]')
    # comment_rate = int(comment) / int(play)
    share = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[8]')
    # share_rate = int(share) / int(play)
    Fans_raise = ''
    for i in range(len(title)):
        datalist = []
        datalist.append(day)
        datalist.append(title[i].text)
        datalist.append(name)
        datalist.append(platform)
        datalist.append(Publish_time[i].text)
        datalist.append('')
        j = play[i].text
        if "w" in j:
            j = re.sub('w', '', j)

            j = float(j) * 10000

        datalist.append(int(j))
        datalist.append(finish_play[i].text)
        ave_times = ave_time[i].text
        ave_times = re.sub('\..*$','',ave_times)
        ave_times = re.sub('-', '0', ave_times)
        datalist.append(int(ave_times))
        datalist.append(int(approve[i].text))

        if j == '0':
            datalist.append(0)  # 点赞率
            datalist.append(int(comment[i].text))
            datalist.append(0)
            datalist.append(int(share[i].text))
            datalist.append(0)
        else:
            datalist.append(int(approve[i].text) / int(j))  # 点赞率
            datalist.append(int(comment[i].text))
            datalist.append(int(comment[i].text) / int(j))
            datalist.append(int(share[i].text))
            datalist.append(int(share[i].text) / int(j))
        datalist.append(Fans_raise)
        All_datalist.append(datalist)


if __name__ == '__main__':
    MAXINDEX = 5

    # Selenium_Login()
    # douyin()
    # kuaishou()
    # bilibili()
    # xiaohongshu()
    shipinhao()
    pass
