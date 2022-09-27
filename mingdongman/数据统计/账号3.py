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
savepath = r"D:\untitled1\demo\mingdongman\日报Excel\220926统计账号7.xlsx"
day = '2022/09/25'
FILE_PATH_DICT = {

    # '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',#实验账号
    # '浏览器个人配置': r'G:\Selenium_UserData\ZhiHu\one',#账号一
    # '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Artstation\one',#账号二
    '浏览器个人配置': r'G:\Selenium_UserData\Artstation_Pixiv\Pixiv\one',#账号三
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
    switch_(FILE_PATH_DICT['b站url'])
    bilibili()

    print(All_datalist)
    browser.quit()


    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('知乎', cell_overwrite_ok=True)
    col = ("数据日期","账号","所属平台","发布量","播放量","点赞量","点赞率","评论量","评论率","转发量","转发率","关注量")

    for i in range(0, 12):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条" % (i + 1))
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
    name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
    browser.find_element(By.XPATH, '//span[text()="数据总览"]').click()
    time.sleep(2)
    Play = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[1]/div[2]').text
    # Douyin_views = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[2]/div[2]').text
    approve = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[3]/div[2]').text
    share = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[4]/div[2]').text
    comment = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[5]/div[2]').text
    Fans_raise = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[6]/div[2]').text
    platform = '抖音'

    if "," in Play:
        Play = re.sub(',', '', Play)
    elif "," in Fans_raise:
        Fans_raise = re.sub(',', '', Fans_raise)
    elif "," in comment:
        comment = re.sub(',', '', comment)
    elif "," in approve:
        approve = re.sub(',', '', approve)
    elif "," in share:
        share = re.sub(',', '', share)

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
    datalist.append('')
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    All_datalist.append(datalist)

def kuaishou():
    datalist = []
    # browser.get('https://cp.kuaishou.com/profile')
    # browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(text(),"发布视频")]')))
            time.sleep(3)
            break
        except Exception:
            continue

    div_list = browser.find_elements(By.XPATH, '//div[@class="tooltip"]/span')
    name = browser.find_element(By.XPATH, '//div[@class="detail__name"]').text
    Play = div_list[0].text
    # Kuaishou_Completion_rate = div_list[1].text
    Fans_raise = div_list[2].text
    comment = div_list[3].text
    approve = div_list[4].text
    share = div_list[5].text
    platform = "快手"

    if "," in Play:
        Play = re.sub(',', '', Play)
    elif "," in Fans_raise:
        Fans_raise = re.sub(',', '', Fans_raise)
    elif "," in comment:
        comment = re.sub(',', '', comment)
    elif "," in approve:
        approve = re.sub(',', '', approve)
    elif "," in share:
        share = re.sub(',', '', share)

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
    datalist.append('')
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    All_datalist.append(datalist)

def bilibili():
    datalist = []
    # browser.get('https://member.bilibili.com/platform/home')
    # browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
            time.sleep(3)
            break
        except Exception:
            continue
    browser.find_element(By.XPATH, '// a[contains(text(), "电磁力")]').click()
    time.sleep(1)
    name = browser.find_element(By.XPATH, '//span[@class="up-info-name"]').text
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="近7天"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//ul[@class="options-box"]//li[1]').click()
    time.sleep(1)

    div_list=browser.find_elements(By.XPATH,'//div[@class="value xx-bin-bold"]/span')
    Play = div_list[0].text
    # bilibili_Space_view=div_list[1].text
    Fans_raise = div_list[2].text
    approve = div_list[3].text
    # bilibli_Collection = div_list[4].text
    # bilibili_Coin = div_list[5].text
    comment = div_list[6].text
    # bilibli_Bullet_chat = div_list[7].text
    share = div_list[8].text
    platform = "b站"

    if "," in Play:
        Play = re.sub(',', '', Play)
    elif "," in Fans_raise:
        Fans_raise = re.sub(',', '', Fans_raise)
    elif "," in comment:
        comment = re.sub(',', '', comment)
    elif "," in approve:
        approve = re.sub(',', '', approve)
    elif "," in share:
        share = re.sub(',', '', share)

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
    datalist.append('')
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    All_datalist.append(datalist)

def xiaohongshu():

    datalist = []
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
    time.sleep(2)
    browser.find_element(By.XPATH, '//div[contains(text(),"笔记数据")]').click()
    time.sleep(1)
    div_list = browser.find_elements(By.XPATH, '//div[@class="block-line"]//span[2]')

    Play = div_list[0].text
    # xiaohongshu_All_view_time = div_list[1].text
    approve = div_list[2].text
    # xiaohongshu_Collection = div_list[3].text
    comment = div_list[4].text
    # xiaohongshu_Bullet_chat = div_list[5].text
    Fans_raise = div_list[6].text
    platform = '小红书'
    share = '无法获取'

    if "," in Play:
        Play = re.sub(',', '', Play)
    elif "," in Fans_raise:
        Fans_raise = re.sub(',', '', Fans_raise)
    elif "," in comment:
        comment = re.sub(',', '', comment)
    elif "," in approve:
        approve = re.sub(',', '', approve)
    elif "," in share:
        share = re.sub(',', '', share)

    if Play == '0':
        approve_rate = 0
        share_rate = "无法获取"
        comment_rate = 0
    else:
        approve_rate = int(approve) / int(Play)
        share_rate = '无法获取'
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
    All_datalist.append(datalist)
def shipinhao():
    datalist = []
    # browser.get('https://channels.weixin.qq.com/platform')
    # browser.maximize_window()
    while True:
        try:
            WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
            time.sleep(3)
            break
        except Exception:
            continue
    name = browser.find_element(By.XPATH, '//h2').text
    time.sleep(2)
    browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="关注者数据"]').click()
    time.sleep(1)
    #获取关注数据
    div_list = browser.find_elements(By.XPATH, '//div[@class="value"]')
    # shipinhao_Fans_raises = div_list[0].text
    Fans_raise = div_list[1].text
    # shipinhao_Fans_drop = div_list[2].text

    time.sleep(1)
    browser.find_element(By.XPATH, '//span[text()="动态数据"]').click()
    time.sleep(1)
    #获取动态数据
    div_list = browser.find_elements(By.XPATH, '//div[@class="value"]')
    Play = div_list[0].text
    approve = div_list[1].text
    comment = div_list[2].text
    share = div_list[3].text
    # shipinhao_Collection = div_list[4].text
    platform = '视频号'

    if "," in Play:
        Play = re.sub(',', '', Play)
    elif "," in Fans_raise:
        Fans_raise = re.sub(',', '', Fans_raise)
    elif "," in comment:
        comment = re.sub(',', '', comment)
    elif "," in approve:
        approve = re.sub(',', '', approve)
    elif "," in share:
        share = re.sub(',', '', share)

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
    datalist.append('')
    datalist.append(Play)
    datalist.append(approve)
    datalist.append(approve_rate)
    datalist.append(comment)
    datalist.append(comment_rate)
    datalist.append(share)
    datalist.append(share_rate)
    datalist.append(Fans_raise)
    All_datalist.append(datalist)
if __name__ == '__main__':
    MAXINDEX = 5

    Selenium_Login()
    # douyin()
    # kuaishou()
    # bilibili()
    # xiaohongshu()
    # shipinhao()
    pass
