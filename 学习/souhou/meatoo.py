# coding=utf-8
import requests,re,xlwt,threading
import pandas as pd
# FILE_PATH_DICT = {
#     '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
#     '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
# }
# from My_code.Toolbox.Selenium import seleniumClass
# browser = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
# browser.implicitly_wait(5)

mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\学习\souhou\meatoo_url2.xlsx',sheet_name=[
        '第一段'
    ])
All_url = (mainExcelDict['第一段'])['url'].to_list()

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'referer': 'https://www.sogou.com/'
}
titilelist = []

t1 = threading.Thread

def titlee():

    for i in range(len(All_url)):

        print(i)
        print(All_url[i])
        url = All_url[i]
        res = requests.get(url, headers=headers).text
        # print(res)
        title = re.findall('<title>(.*?)</title>',res)

        titilelist.append(title[0])
    return titilelist


def test1():


    pass

def test2():
    pass


def save1(All_datalist):#保存账号数据
    savepath = r'D:\untitled1\demo\学习\souhou\title.xlsx'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('七麦', cell_overwrite_ok=True)
    col = ("信息")

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        # print("第%d条" % (i + 1))
        # data = All_datalist[i]
        # for j in range(0, len(data)):
        sheet.write(i + 1, 0, All_datalist[i])
    book.save(savepath)  # 保存





if __name__ == '__main__':
    All_datalist= titlee()
    save1(All_datalist)
