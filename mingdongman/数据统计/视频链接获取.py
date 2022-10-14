# coding=utf-8
FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
}

from My_code.Toolbox.Selenium import seleniumClass
driver = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
driver.implicitly_wait(5)
import pandas as pd
import requests,re,time,xlwt
from lxml import html
etree = html.etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "cookie":"_did=web_14536971838C87B8; language=zh-CN; ud=22256115; account_id=15032681; soft_did=1619580708547; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3; did=web_7858a2eb4853800d3e4273f895c8cb55; client_key=65890b29; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABiRCdFGwSJdc4ky7QF_eZ_R3CeDYby5Qmp_pPj3sQnlCxbnAAnh1fzO7O5Y6UmcGjBUvIt-Fae_RdjUj_VgGXlr9X2flehC640HJOdR4wdp1s-U0nrDGwsZIQ2pQJfN38dXsb7gH_ReHi31W6_B4bpXOGFfl8IuMJT9qlwNUsg3t_xE8BXYSmB6a7K9W7t-V51p_k8-3ErFFZKXJPA0sq_hoSdWlbobCW6oJxuQLJTUr9oj_uIiACKYeactlSXNS5KT-13xVz_o0b-ptK3VAQu66nfQaM4ygFMAE; kuaishou.server.web_ph=a4e8f2ec4f33528f4b6b732e6e4f1f1106c6"
}

kuaishou_All_video_url = []  # 存储所有账号的url
All_kuaishou_url=[]

All_video_detaillist=[]
savepath = r"D:\untitled1\demo\mingdongman\数据统计\日报_短视频数据\抖音详情.xlsx"


def save1():#保存短视频数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('快手', cell_overwrite_ok=True)
    col = ("视频url", "作者id")

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(kuaishou_All_video_url)):
        print("第%d条视频" % (i + 1))
        data = kuaishou_All_video_url[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

def save2():#保存短视频数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('抖音', cell_overwrite_ok=True)
    col = ("视频标题", "所属账号", "所属平台","视频链接")

    for i in range(0, 4):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_video_detaillist)):
        print("第%d条视频" % (i + 1))
        data = All_video_detaillist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

def switch_(url):#url转换
    driver.switch_to.default_content()
    # 获取所有窗口句柄集合
    handles = driver.window_handles
    # 创建页面
    handles = seleniumClass().Create_New_Page(browser=driver, newPageUrl=url)

#获取视频链接
# def kuaishou_url():
#     # 读取模板
#     mainExcelDict = pd.read_excel(
#         r'\\Win-pp19bi8ic9t\g\流量部\自媒体矩阵\短视频\数据分析\日报\账号、视频链接.xls', sheet_name=[
#             '账号链接'
#         ]
#     )
#     mainExcelData = mainExcelDict['账号链接']
#     kuaishou_mainExcelData = mainExcelData[(mainExcelData['所属平台'] == '快手')]
#     kuaishou_Space_Url = kuaishou_mainExcelData['账号主页链接'].to_list()
#
#     #获取快手视频链接
#     driver.get("https://www.zhihu.com/people/6-81-43-43/posts")
#     driver.maximize_window()
#
#     for i in range(len(kuaishou_Space_Url)):
#         switch_(kuaishou_Space_Url[i])#转换不同主页
#         input("滑块验证")
#         driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#向下滚动
#         url_data = driver.page_source#获取网页内容
#         video_url = re.findall('clientCacheKey=(.*?)\.jpg', url_data)#获取改账号所有url
#         authorId = (kuaishou_Space_Url[i])  # 获取改账号所有url
#
#         for i in range(len(video_url)):
#             kaishou_All_video_ = []
#             kaishou_All_video_.append(video_url[i])  # 存储所有账号的url
#             kaishou_All_video_.append(authorId)
#             kuaishou_All_video_url.append(kaishou_All_video_)
#     print(kuaishou_All_video_url)
#     # prin
#     # #清洗存储后的url
#     # for i in range(len(kuaishou_All_video_url)):
#     #     data = kuaishou_All_video_url[i]  # 提取出列中列
#     #     for j in range(len(data)):  # 循环列
#     #         All_kuaishou_url.append(data[j])
#     save1()


def kuaishou_title():
    # 获取视频标题
    mainExcelDict = pd.read_excel(
        r'D:\untitled1\demo\mingdongman\数据统计\日报_短视频数据\快手url_作者详情.xlsx', sheet_name=[
            '快手'
        ]
    )
    mainExcelData = mainExcelDict['快手']
    kuaishou_All_video_url = mainExcelData['视频url'].to_list()
    kuaishou_All_video_author = mainExcelData['作者id'].to_list()

    for i in range(len(kuaishou_All_video_url)):
        video_detaillist = []
        video_url = f'https://www.kuaishou.com/short-video/{kuaishou_All_video_url[i]}?authorId={kuaishou_All_video_author[i]}&streamSource=profile&area=profilexxnull'

        page_text = requests.get(url=video_url, headers=headers).text
        print(page_text)
        print(i)
        platform = '快手'
        title = re.findall('<title>(.*?)</title>', page_text,re.S)
        counter = re.findall('"name":"(.*?)","following', page_text,re.S)

        video_detaillist.append(title[0])
        video_detaillist.append(counter[0])
        video_detaillist.append(platform)
        video_detaillist.append(video_url)
        All_video_detaillist.append(video_detaillist)
    print(All_video_detaillist)
    save2()

def douyin():

    mainExcelDict = pd.read_excel(
        r'\\Win-pp19bi8ic9t\g\流量部\自媒体矩阵\短视频\数据分析\日报\账号、视频链接.xls', sheet_name=[
            '账号链接'
        ]
    )
    mainExcelData = mainExcelDict['账号链接']
    kuaishou_mainExcelData = mainExcelData[(mainExcelData['所属平台'] == '抖音')]
    kuaishou_Space_Url = kuaishou_mainExcelData['账号主页链接'].to_list()

    #获取快手视频链接
    driver.get("https://www.zhihu.com/people/6-81-43-43/posts")
    driver.maximize_window()
    for i in range(len(kuaishou_Space_Url)):
        switch_(kuaishou_Space_Url[i])#转换不同主页
        input("滑块验证")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")#向下滚动
        url_data = driver.page_source#获取网页内容

        print(url_data)
        platform = '抖音'
        video_url = re.findall('class="ECMy_Zdt"><a href="//(.*?)"', url_data, re.S)#获取改账号所有url
        authorId = re.findall('"name": "(.*?)",', url_data, re.S)
        title = re.findall('<p class="iQKjW6dr">(.*?)</p>', url_data, re.S)

        try:
        #将单个账号的数据存入汇总列表中
            for i in range(len(video_url)):
                kaishou_All_video_ = []

                kaishou_All_video_.append(title[i])
                kaishou_All_video_.append(authorId[1])
                kaishou_All_video_.append(platform)
                kaishou_All_video_.append(video_url[i])
                All_video_detaillist.append(kaishou_All_video_)
        except:
            continue
        print(All_video_detaillist)
    print(All_video_detaillist)
    # prin
    # #清洗存储后的url
    # for i in range(len(kuaishou_All_video_url)):
    #     data = kuaishou_All_video_url[i]  # 提取出列中列
    #     for j in range(len(data)):  # 循环列
    #         All_kuaishou_url.append(data[j])
    save2()
pass



if __name__ == '__main__':

    # kuaishou_url()#获取url
    # kuaishou_title()
    douyin()

