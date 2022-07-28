# -*- codeing = utf-8 -*-
# @Time :2022/7/7 21:57
# @Author:Eric
# @File : 淘宝司法3.py
# @Software: PyCharm
import requests
from lxml import etree
import re
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import datetime
import xlwt
headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}

def main():
    baseurl = "https://sf.taobao.com/"
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "淘宝司法拍卖3.xls"
    print(datalist)
    #3.保存数据
    saveData(datalist, savepath)

def getData(baseurl):
    datalist = []


    #2.逐步解析数据
    res = requests.get(url=baseurl, headers=headers).text

    #data = [] #保存一部电影的所有信息
    # 影片详情的链接
    title = re.findall('"title":"(.*?)",',res) # re库用来通过正则表达式查找指定的字符串
    #data.append(title)  # 添加链接

    itemUrl = re.findall('"itemUrl":"(.*?)",', res)
   # data.append(itemUrl)  # 添加链接
    currentPrice = re.findall('"currentPrice":(.*?),', res)
   # data.append(currentPrice)  # 添加链接
    status = re.findall('"status":"(.*?)",', res)
   # data.append(status)  # 添加链接
    end = re.findall('"end":(.*?),', res)
    #将end列表的改为数字类型
    new_numbers = [];
    for n in end:
        new_numbers.append(int(n));
    end = new_numbers

    for i in range(len(end)):
        print(type(end[i]))
        timestamp = end[i]
        print(timestamp)
        print(type(timestamp))
        timestamp = timestamp
        print(timestamp)
        # 转换成localtime
        time_local = time.localtime(timestamp/1000)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(dt)
        end[i] = dt



   # data.append(end)  # 添加链接

    #datalist.append(data)  # 把处理好的一部电影信息放入datalist

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        data = []
        data.append(title[i])
        itemUrl[i] = 'https:'+(itemUrl[i])
        data.append(itemUrl[i])
        data.append(currentPrice[i])
        data.append(status[i])
        # print(type(end[i]))
        # timestamp = end[i]
        # print(timestamp)
        # print(type(timestamp))
        # timestamp =timestamp
        # print(timestamp)
        #
        # #转换成localtime
        # time_local = time.localtime(timestamp)
        # # 转换成新的时间格式(2016-05-05 20:28:54)
        # dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
        # print(dt)
        # end[i] = dt

        data.append(end[i])

        datalist.append(data)  # 把处理好的一部电影信息放入datalist
    return datalist

def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('淘宝司法拍卖',cell_overwrite_ok=True)    #创建工作表
    col = ("商品标题","详情页链接","当前拍卖价格/元","拍卖状态","拍卖结束时间")
    for i in range(0, 5):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0,34):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])
    book.save(savepath)       #保存

if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    #init_db("movietest.db")
    print("爬取完毕！")

# tree = etree.HTML(res)
# print(tree)


# li_list = tree.xpath('//*[@id="car-data-list"]/ul')
# print(li_list)


# title = []
# price = []
# state = []
# time =[]
# for li in li_list[1:]:
#     # 来源
#     title = li.xpath('./a/div[1]/p/text()')
#     price = li.xpath('./a/div[2]/p[2]/span[2]/em[2]/text()')
#     state = li.xpath('./a/div[4]/div[2]/text()')
#     time = li.xpath('./a/div[2]/p[6]/span[2]/text()')
# print(title, price, state, time)



