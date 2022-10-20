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

All_datalist = []#抖音账号日报
All_datalist1 = []#短视频数据
Douyin_All_datalist = []
Douyin_All_datalist1 = []
Shipinhao_All_datalist = []
Shipinhao_All_datalist1 = []

savepath = r"D:\untitled1\demo\mingdongman\日报Excel\统计账号2.xlsx"
savepath1 = r"D:\untitled1\demo\mingdongman\短视频Excel\统计视频2.xlsx"
day = '2022/10/18'
video_day = '2022/10/19'
FILE_PATH_DICT = {

    # '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',#实验账号
    # '浏览器个人配置': r'G:\Selenium_UserData\ZhiHu\one',#账号一
    '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Artstation\one',#账号二
    # '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Pixiv\one',  # 账号三
    # '浏览器个人配置': r'G:\Selenium_UserData\BaiDu',#账号四
    # '浏览器个人配置': r'G:\Selenium_UserData\Bcy\one',#账号五
    # '浏览器个人配置': r'G:\Selenium_UserData\GuangWen',#账号六
    # '浏览器个人配置': r'G:\Selenium_UserData\MooYoo',#账号七
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
    'b站个人主页': r'https://space.bilibili.com/'
}
browser = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
browser.implicitly_wait(5)

def Selenium_Login():
    # 实例化浏览器
    douyin()
    if douyin_video1():#获取所有抖音作品
        douyin_video()#获取抖音最近30天
    switch_(FILE_PATH_DICT['快手url'])
    if kuaishou():
        kuaishou_video()
    switch_(FILE_PATH_DICT['小红书url'])
    xiaohongshu()
    xiaohongshu_video()
    switch_(FILE_PATH_DICT['视频号url'])
    shipinhao()
    if shipinhao_video1():#获取视频号所有视频
        shipinhao_video()

    # 获取名称
    global bili_name
    global bili_fans

    # switch_(FILE_PATH_DICT['b站个人主页'])
    # bili_name = browser.find_element(By.XPATH, '//span[@id="h-name"]').text
    # bili_fans = browser.find_element(By.XPATH, '//p[@class="n-data-v space-fans"]').text
    #
    # switch_(FILE_PATH_DICT['b站url'])
    # bilibili()
    # bilibili_video()
    print(All_datalist)
    print(All_datalist1)
    browser.quit()

def save1():#保存账号数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('知乎', cell_overwrite_ok=True)
    col = ("数据日期", "账号", "所属平台", "发布量", "播放量", "点赞量", "点赞率", "评论量", "评论率", "转发量", "转发率", "关注量", "累计关注量")

    for i in range(0, 13):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条" % (i + 1))
        data = All_datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

def save2():#保存短视频数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('抖音', cell_overwrite_ok=True)
    col = ("数据日期", "视频标题", "所属账号", "所属平台", "发布日期", "发布天数", "播放量（总）", "完播率", "平均播放时长(s)", "点赞量（总）", "点赞率（点赞/播放）", "评论量（总）", "评论率（评论/播放）", "转发量（总）", "转发率（准发/播放）", "视频带粉数（总）")

    for i in range(0, 16):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist1)):
        print("第%d条视频" % (i + 1))
        data = All_datalist1[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath1)  # 保存

def switch_(url):#url转换
    browser.switch_to.default_content()
    # 获取所有窗口句柄集合
    handles = browser.window_handles
    # 创建页面
    handles = seleniumClass().Create_New_Page(browser=browser, newPageUrl=url)

def douyin():#抖音账号日报
    datalist = []
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
    fans = browser.find_element(By.XPATH, '//div[@class="info--3nLbr"]/div[2]/div[1]/div[3]/span').text #粉丝数
    name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text #平台账户名称
    browser.find_element(By.XPATH, '//span[text()="数据总览"]').click()
    time.sleep(2)
    try:  #没有数据直接退出
        Play = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[1]/div[2]').text
    except:
        return False
    approve = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[3]/div[2]').text
    share = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[4]/div[2]').text
    comment = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[5]/div[2]').text
    Fans_raise = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[6]/div[2]').text
    platform = '抖音'

    # 清洗数据
    Play = re.sub(',', '', Play)
    Fans_raise = re.sub(',', '', Fans_raise)
    comment = re.sub(',', '', comment)
    approve = re.sub(',', '', approve)
    share = re.sub(',', '', share)
    fans = re.sub(',', '', fans)

    if Play == '0':
        approve_rate = 0
        share_rate = 0
        comment_rate = 0
    else:
        approve_rate = int(approve) / int(Play)
        share_rate = int(share) / int(Play)
        comment_rate = int(comment) / int(Play)

    datalist.append(day)
    datalist.append(name)
    datalist.append(platform)
    datalist.append('')#发布量
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    datalist.append(fans)
    All_datalist.append(datalist)

def douyin_video1():#获取抖音所有作品
    browser.get('https://creator.douyin.com/creator-micro/home')
    browser.maximize_window()
    time.sleep(1)
    name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
    platform = '抖音'
    browser.find_element(By.XPATH, '//span[text()="作品管理"]').click()
    time.sleep(1)
    if len(browser.find_elements(By.XPATH, '//div[@class="info-title-text--kEYth info-title-small-desc--tW-Ce"]'))==0:#如果账号没有数据则退出
        return False

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
        douyin_public_time = times[i].text
        douyin_public_time = re.sub('年', '/', douyin_public_time)
        douyin_public_time = re.sub('月', '/', douyin_public_time)
        douyin_public_time = re.sub('日.*$', '', douyin_public_time)
        #播放数据
        j = play[i].text
        if "w" in j:
            j = re.sub('w', '', j)
            j = float(j) * 10000
        if j == '0':
            approve_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve[i].text) / int(j)
            comment_rate = int(comment[i].text) / int(j)

        datalist.append(video_day)
        datalist.append(title[i].text)  # 标题
        datalist.append(name)
        datalist.append(platform)
        datalist.append(douyin_public_time)  # 发布时间
        datalist.append('')  # 发布天数
        datalist.append(int(j)) #播放
        datalist.append('') #完播率
        datalist.append('')#均播
        datalist.append(int(approve[i].text))  # 点赞
        datalist.append(approve_rate)  # 点赞率
        datalist.append(int(comment[i].text))
        datalist.append(comment_rate)
        datalist.append('')#分享
        datalist.append('')#分享率
        datalist.append('')#视频带粉
        All_datalist1.append(datalist)
    return True

def douyin_video():#获取抖音最近30天发布的作品
    browser.find_element(By.XPATH, '//span[text()="关注管理"]').click()
    browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()

    time.sleep(1)
    name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
    platform = '抖音'
    browser.find_element(By.XPATH, '//span[text()="作品数据"]').click()
    Publish_time = browser.find_elements(By.XPATH, '//div[@class="date-text--2Aa6v"]')
    if len(Publish_time) == 0: #判断是否存在最近30天作品
        print(name,'没有最近30天作品')
    else:
        title = browser.find_elements(By.XPATH, '//div[@class="title-text--37-P9 first-text--2S8h2"]')
        play = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[3]//div[@class="number-text--1NhF0"]')
        finish_play = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[9]//div[@class="number-text--1NhF0"]')
        ave_time = ''
        approve = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[4]//div[@class="number-text--1NhF0"]')
        comment = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[6]//div[@class="number-text--1NhF0"]')
        share = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[5]//div[@class="number-text--1NhF0"]')
        Fans_raise = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[8]//div[@class="number-text--1NhF0"]')

        for i in range(len(title)):
            datalist = []
            #清洗发布时间
            douyin_public_time = Publish_time[i].text
            douyin_public_time = re.sub('年', '/', douyin_public_time)
            douyin_public_time = re.sub('月', '/', douyin_public_time)
            douyin_public_time = re.sub('日.*$', '', douyin_public_time)

            j = play[i].text    #播放数据
            if "w" in j:
                j = re.sub('w','',j)
                j = float(j)*10000
            if j == '0':
                approve_rate = 0
                share_rate = 0
                comment_rate = 0
            else:
                approve_rate = int(approve[i].text) / int(j)
                share_rate = int(share[i].text) / int(j)
                comment_rate = int(comment[i].text) / int(j)

            datalist.append(video_day)#0
            datalist.append(title[i].text)#1
            datalist.append(name)#2
            datalist.append(platform)#3
            datalist.append('')  # 发布天数#4
            datalist.append(douyin_public_time)#5
            datalist.append(int(j))#6
            datalist.append(finish_play[i].text)#7#完播
            datalist.append(ave_time)#8
            datalist.append(int(approve[i].text))#9
            datalist.append(approve_rate)#点赞率#10
            datalist.append(int(comment[i].text))#11
            datalist.append(comment_rate)#12
            datalist.append(int(share[i].text))#13
            datalist.append(share_rate)#14
            datalist.append(int(Fans_raise[i].text))#15
            Douyin_All_datalist.append(datalist)
        for i in range(len(Douyin_All_datalist)):
            All_datalist1[i][7]=Douyin_All_datalist[i][7]#完播率
            All_datalist1[i][13] = Douyin_All_datalist[i][13]#分享
            All_datalist1[i][14] = Douyin_All_datalist[i][14]#分享率
            All_datalist1[i][15] = Douyin_All_datalist[i][15]#带粉数

def kuaishou():
    datalist = []
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(text(),"发布视频")]')))
            time.sleep(3)
            break
        except Exception:
            continue

    div_list = browser.find_elements(By.XPATH, '//div[@class="tooltip"]/span')
    if len(div_list)==0:
        return False
    name = browser.find_element(By.XPATH, '//div[@class="detail__name"]').text
    fans = browser.find_element(By.XPATH, '//div[@class="detail__row"]/div[1]/div[1]').text
    Play = div_list[0].text
    Fans_raise = div_list[2].text
    comment = div_list[3].text
    approve = div_list[4].text
    share = div_list[5].text
    platform = "快手"

    Play = re.sub(',', '', Play)
    Fans_raise = re.sub(',', '', Fans_raise)
    comment = re.sub(',', '', comment)
    approve = re.sub(',', '', approve)
    share = re.sub(',', '', share)
    Play = re.sub('\+', '', Play)
    Fans_raise = re.sub('\+', '', Fans_raise)
    comment = re.sub('\+', '', comment)
    approve = re.sub('\+', '', approve)
    share = re.sub('\+', '', share)
    fans = re.sub(',', '', fans)

    if Play == '0':
        approve_rate = 0
        share_rate = 0
        comment_rate = 0
    else:
        approve_rate = int(approve) / int(Play)
        share_rate = int(share) / int(Play)
        comment_rate = int(comment) / int(Play)
    datalist.append(day)
    datalist.append(name)
    datalist.append(platform)
    datalist.append('')#发布量
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    datalist.append(fans)
    All_datalist.append(datalist)
    return True

def kuaishou_video():

    browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()
    time.sleep(1)
    platform = "快手"
    name = browser.find_element(By.XPATH, '//div[@class="detail__name"]').text

    time.sleep(1)
    # browser.find_element(By.XPATH, '//span[contains(text(),"数据中心")]').click()
    # time.sleep(1)
    browser.find_element(By.XPATH, '//li[contains(text(),"视频数据")]').click()
    time.sleep(1)

    Publish_time = browser.find_elements(By.XPATH, '//div[@class="video-item__info__detail__date"]')
    if len(Publish_time)==0:
        return
    title = browser.find_elements(By.XPATH, '//div[@class="video-item__info__detail__title__content"]')
    play = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[1]/div[2]')
    finish_play = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[2]/div[2]')
    ave_time = ''
    approve = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[5]/div[2]')
    comment = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[4]/div[2]')
    share = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[6]/div[2]')
    Fans_raise = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[3]/div[2]')

    for i in range(len(title)):
        datalist = []
        datalist.append(video_day)
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
        datalist.append(int(j))#播放量

        if finish_play[i].text=='--':
            datalist.append('0%')
        else:
            datalist.append(finish_play[i].text)
        datalist.append(ave_time)#均播

        a = approve[i].text
        b = (comment[i].text)
        c = (share[i].text)
        d = Fans_raise[i].text

        a = re.sub(',', '', str(a))
        if "万" in a:
            a = re.sub('万', '', a)
            a = int((float(a),) * 10000)
        elif "--" in a:
            a = 0

        b = re.sub(',', '', (b))
        if "万" in b:
            b = re.sub('万', '', b)
            b = int(float(b) * 10000)
        elif "--" in b:
            b = 0

        c = re.sub(',', '', str(c))
        if "万" in c:
            c = re.sub('万', '', c)
            c = int(float(c) * 10000)
        elif "--" in c:
            c = 0

        d = re.sub(',', '', str(d))
        if "万" in d:
            d = re.sub('万', '', d)
            d = int(float(d) * 10000)
        elif "--" in d:
            d = 0


        if j == '0':
            approve_rate = 0
            share_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(a) / int(j)
            share_rate = int(c) / int(j)
            comment_rate = int(b) / int(j)

        datalist.append(int(a))#点赞量
        datalist.append(approve_rate) #点赞率
        datalist.append(int(b))#评论量
        datalist.append(share_rate)#评论率
        datalist.append(int(c))#转发量
        datalist.append(comment_rate)#转发率
        datalist.append(int(d))#增粉数

        All_datalist1.append(datalist)

def bilibili():
    datalist = []
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
            time.sleep(3)
            break
        except Exception:
            continue
    time.sleep(1)
    # browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
    # time.sleep(1)
    # browser.find_element(By.XPATH, '//span[text()="近7天"]').click()
    # time.sleep(1)
    # browser.find_element(By.XPATH, '//ul[@class="options-box"]//li[1]').click()
    # time.sleep(1)
    # div_list = browser.find_elements(By.XPATH, '//div[@class="value xx-bin-bold"]/span')
    # Play = div_list[0].text
    # Fans_raise = div_list[2].text
    # approve = div_list[3].text
    # comment = div_list[6].text
    # share = div_list[8].text

    Play = browser.find_element(By.XPATH, '//*[@id="cc-body"]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div/div/div[2]/span').text
    Fans_raise = browser.find_element(By.XPATH, '//*[@id="cc-body"]/div[2]/div[3]/div/div[2]/div[1]/div[1]/div/div/div[2]/span').text
    approve = browser.find_element(By.XPATH, '//*[@id="cc-body"]/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div/div[2]/span').text
    comment = browser.find_element(By.XPATH, '//*[@id="cc-body"]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div/div[2]/span').text
    share = browser.find_element(By.XPATH, '//*[@id="cc-body"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/span').text
    fans = bili_fans

    platform = "b站"
    Play = re.sub(',', '', Play)
    Fans_raise = re.sub(',', '', Fans_raise)
    comment = re.sub(',', '', comment)
    approve = re.sub(',', '', approve)
    share = re.sub(',', '', share)
    fans = re.sub(',', '', fans)
    if Play == '0万':
        Play = '0'
    if Fans_raise == '0万':
        Fans_raise = 0
    if comment == '0万':
        comment = 0
    if approve == '0万':
        approve = 0
    if share == '0万':
        share = 0
    if fans == '0万':
        fans = 0

    if Play == '0':
        approve_rate = 0
        share_rate = 0
        comment_rate = 0
    else:
        approve_rate = int(approve) / int(Play)
        share_rate = int(share) / int(Play)
        comment_rate = int(comment) / int(Play)
    datalist.append(day)
    datalist.append(bili_name)
    datalist.append(platform)
    datalist.append('')#发布量
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    datalist.append(fans)
    All_datalist.append(datalist)

def bilibili_video():

    browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()
    time.sleep(1)
    platform = "b站"
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[contains(text(),"内容管理")]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[contains(text(),"稿件管理")]').click()
    time.sleep(1)

    Publish_time = browser.find_elements(By.XPATH, '//div[@class="pubdate is-success"]/span[1]')
    if len(Publish_time)==0:
        return
    title = browser.find_elements(By.XPATH, '//div[@class="meta-title"]/a')
    play = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[1]//span')
    finish_play = ''
    ave_time = ''
    approve = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[6]//span')
    comment = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[3]//span')
    share = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[7]//span')
    Fans_raise = ''

    #获取名称
    # switch_(FILE_PATH_DICT['b站个人主页'])
    # name = browser.find_element(By.XPATH, '//span[@id="h-name"]').text

    for i in range(len(title)):
        datalist = []
        datalist.append(video_day)
        datalist.append(title[i].text)
        datalist.append(bili_name)
        datalist.append(platform)

        # 发布时间清洗
        bilibili_public_time = Publish_time[i].text
        bilibili_public_time = re.sub('-', '/', bilibili_public_time)
        bilibili_public_time = re.sub(' .*$', '', bilibili_public_time)
        bilibili_public_time = '20' + bilibili_public_time

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
        if j =='0':
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
        All_datalist1.append(datalist)

def xiaohongshu():
    datalist = []
    # 抓取的是近7日的
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
    fans = browser.find_element(By.XPATH, '//p[@class="detail"]/span[2]/label').text
    time.sleep(2)
    browser.find_element(By.XPATH, '//div[contains(text(),"笔记数据")]').click()
    time.sleep(1)
    div_list = browser.find_elements(By.XPATH, '//div[@class="block-line"]//span[2]')

    Play = div_list[0].text
    approve = div_list[2].text
    comment = div_list[4].text
    Fans_raise = div_list[6].text
    platform = '小红书'
    share = ''

    Play = re.sub(',', '', Play)
    Fans_raise = re.sub(',', '', Fans_raise)
    comment = re.sub(',', '', comment)
    approve = re.sub(',', '', approve)
    share = re.sub(',', '', share)
    fans = re.sub(',', '', fans)

    if Play == '0':
        approve_rate = 0
        share_rate = ''
        comment_rate = 0
    else:
        approve_rate = int(approve) / int(Play)
        share_rate = ''
        comment_rate = int(comment) / int(Play)
    datalist.append(day)
    datalist.append(name)
    datalist.append(platform)
    datalist.append('')
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    datalist.append(fans)
    All_datalist.append(datalist)

def xiaohongshu_video():

    browser.find_element(By.XPATH, '//div[contains(text(),"首页")]').click()
    time.sleep(1)
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
    if len(Publish_time)==0:
        return
    title = browser.find_elements(By.XPATH, '//span[@class="title"]')
    play = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[1]/b')
    finish_play = ''
    ave_time = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[2]/b')
    approve = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[3]/b')
    comment = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[1]/b')
    share = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[3]/b')
    Fans_raise = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[4]/b')

    for i in range(len(title)):
        datalist = []
        datalist.append(video_day)
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
        All_datalist1.append(datalist)

def shipinhao():
    datalist = []
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
            time.sleep(3)
            break
        except Exception:
            continue
    name = browser.find_element(By.XPATH, '//h2').text
    fans = browser.find_element(By.XPATH, '//div[@class="finder-info"]/div[2]/span[2]').text

    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="关注者数据"]').click()
    time.sleep(1)
    # 获取关注数据
    div_list = browser.find_elements(By.XPATH, '//div[@class="value"]')
    Fans_raise = div_list[1].text
    browser.find_element(By.XPATH, '//span[text()="动态数据"]').click()
    time.sleep(1)
    # 获取动态数据
    div_list = browser.find_elements(By.XPATH, '//div[@class="value"]')
    Play = div_list[0].text
    approve = div_list[1].text
    comment = div_list[2].text
    share = div_list[3].text
    platform = '视频号'

    Play = re.sub(',', '', Play)
    Fans_raise = re.sub(',', '', Fans_raise)
    comment = re.sub(',', '', comment)
    approve = re.sub(',', '', approve)
    share = re.sub(',', '', share)
    fans = re.sub(',', '', fans)

    if Play == '0':
        approve_rate = 0
        share_rate = 0
        comment_rate = 0
    elif "万" in Play:
        Play = re.sub('万', '', Play)
        Play = int(float(Play) * 10000)
        Play = re.sub(',', '', str(Play))
        approve_rate = int(approve) / int(Play)
        share_rate = int(share) / int(Play)
        comment_rate = int(comment) / int(Play)
    else:
        approve_rate = int(approve) / int(Play)
        share_rate = int(share) / int(Play)
        comment_rate = int(comment) / int(Play)
    datalist.append(day)
    datalist.append(name)
    datalist.append(platform)
    datalist.append('')#发布量
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    datalist.append(fans)
    All_datalist.append(datalist)

def shipinhao_video1():

    # browser.get('https://channels.weixin.qq.com/platform')

    browser.maximize_window()
    platform = '视频号'
    browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()
    name = browser.find_element(By.XPATH, '//h2').text
    browser.find_element(By.XPATH, '//span[text()="内容管理"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="动态管理"]').click()
    time.sleep(2)
    page = browser.find_elements(By.XPATH, '//span[@class="weui-desktop-pagination__num__wrp spread"]/label')#判断有多少

    if len(page)==0:
        page = [1]
    for l in range(len(page)):

        page_text = browser.page_source
        tree = etree.HTML(page_text)

        title = tree.xpath('//div[@class="post-title"]')
        if len(title)==0:
            return False
        play = tree.xpath('//div[@class="post-data"]/div[1]/span[2]')
        comment = tree.xpath('//div[@class="post-data"]/div[3]/span[2]')
        approve = tree.xpath('//div[@class="post-data"]/div[2]/span[2]')
        share = tree.xpath('//div[@class="post-data"]/div[4]/span[1]')
        Publish_time = tree.xpath('//div[@class="post-time"]/span')

        for i in range(len(title)):
            datalist = []
            datalist.append(video_day)
            datalist.append(title[i].text)
            datalist.append(name)
            datalist.append(platform)
            shipinhao_public_time = Publish_time[i].text
            shipinhao_public_time = re.sub('年', '/', shipinhao_public_time)
            shipinhao_public_time = re.sub('月', '/', shipinhao_public_time)
            shipinhao_public_time = re.sub('日.*$', '', shipinhao_public_time)
            datalist.append(shipinhao_public_time)
            datalist.append('')#发布天数
            j = play[i].text
            if "万" in j:
                j = re.sub('万', '', j)
                j = float(j) * 10000
            datalist.append(int(j))#播放量
            datalist.append('')#完播率
            datalist.append('')#平均播放时长
            datalist.append(int(approve[i].text))#点赞量
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
            datalist.append('')  # 视频带粉

            Shipinhao_All_datalist.append(datalist)
        if len(page)!=1:
            input('点击下一页')
        #     browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #     input('滑到底部')
        #     browser.find_element(By.XPATH, '//a[text()="下一页"]').click()
        # time.sleep(1)

    return True

def shipinhao_video():

    browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()

    platform = '视频号'
    name = browser.find_element(By.XPATH, '//h2').text

    time.sleep(1)
    # browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
    # time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="动态数据"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//a[contains(text(),"单篇动态")]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[contains(text(),"近30天数据")]').click()

    Publish_time = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[2]')
    if len(Publish_time)!=0:
        title = browser.find_elements(By.XPATH, '//div[@class="post-wrap"]/span')
        play = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[5]')
        finish_play = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[3]')
        ave_time = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[4]')
        approve = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[6]')
        comment = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[7]')
        share = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[8]')
        Fans_raise = ''
        for i in range(len(title)):
            datalist = []

            j = play[i].text
            if "万" in j:
                j = re.sub('万', '', j)

                j = float(j) * 10000

            ave_times = ave_time[i].text
            ave_times = re.sub('\..*$', '', ave_times)
            ave_times = re.sub('-', '0', ave_times)

            datalist.append(video_day)
            datalist.append(title[i].text)
            datalist.append(name)
            datalist.append(platform)
            datalist.append(Publish_time[i].text)
            datalist.append('')
            datalist.append(int(j))
            if finish_play[i].text == '0':
                datalist.append('0%')
            else:
                datalist.append(finish_play[i].text)  #8
            datalist.append(int(ave_times))#9
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
            Shipinhao_All_datalist1.append(datalist)#最近30天的视频
            for i in range(len(Shipinhao_All_datalist1)):#将最近30天的作品并入所有作品中
                #判断最近30天的视频是否在作品列表里
                for j in range(len(Shipinhao_All_datalist)):
                    if Shipinhao_All_datalist1[i][1]==Shipinhao_All_datalist[j][1]:
                        Shipinhao_All_datalist[j]=Shipinhao_All_datalist1[i]

                # Shipinhao_All_datalist[i]=Shipinhao_All_datalist1[i]

            for i in range(len(Shipinhao_All_datalist)):#将视频号所有作品纳入总数据中
                All_datalist1.append(Shipinhao_All_datalist[i])
    else:#单独将30天外数据存入
        for i in range(len(Shipinhao_All_datalist)):  # 将视频号所有作品纳入总数据中
            All_datalist1.append(Shipinhao_All_datalist[i])


if __name__ == '__main__':
    MAXINDEX = 5

    Selenium_Login()
    save1()
    save2()
    pass
