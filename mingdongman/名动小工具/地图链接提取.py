# coding=utf-8
from lxml import html
etree = html.etree
import requests
import re
import xlwt
import pandas as pd

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}
savepath = "地图url.xls"
def getData():

    url = 'https://www.meatoo.com/sitemap.xml'

    res = requests.get(url, headers=headers).text

    re_url = '<loc>(.*?)</loc>'
    url_list = re.findall(re_url,res)
    print(url_list)
    return url_list


def saveData(url_list,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('url',cell_overwrite_ok=True)    #创建工作表
    col = "url"
    for i in range(0, 1):
        sheet.write(0, i, col)  # 列名
    for i in range(0,len(url_list)):
        print("第%d条" %(i+1))
        data = url_list[i]
        for j in range(0,1):
            sheet.write(i+1,j,data)
    book.save(savepath)       #保存



if __name__ == "__main__":  # 当程序执行时
    #调用函数
    url_list = getData()
    saveData(url_list,savepath)

    # print(datalist)
