# -*- codeing = utf-8 -*-
# @Time :2022/7/8 21:35
# @Author:Eric
# @File : demo3.py
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
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'referer': 'https://sf.taobao.com/',
    'cookie': 't=ff25ac54b11addfe155f470545b61874; cna=NBs+Goz8KCoCAXBgQCBeU5dD; tracknick=%5Cu5E78%5Cu5B58%5Cu4F60%5Cu597D%5Cu554A; thw=cn; miid=6135800431818474938; _tb_token_=315be083ebbe7; _samesite_flag_=true; lgc=%5Cu5E78%5Cu5B58%5Cu4F60%5Cu597D%5Cu554A; cancelledSubSites=empty; dnk=%5Cu5E78%5Cu5B58%5Cu4F60%5Cu597D%5Cu554A; enc=e8Z6i2YhprGpJUtkTh%2FUtIEEYM3ZRG%2BaiGit7YM51LH0UrPz4uCFB42NlYD2GCxswVmh9kqDVszDZ3gd4eDV8A%3D%3D; sgcookie=E1005mfLvfgjCSY%2BYDAMfzw1IAKnNe5GKs%2FcTxZET5AxVEaAaPsXa8rszH87eAbZ8Y2amZBHYBcwyeho%2FKkDmZYewyy0FdYJ2EahA6iMG9Jd8V3tTN2LmxNi0Khqc9xlN3eB; uc3=nk2=s1on8EyofRBp6Q%3D%3D&vt3=F8dCvCIZxtorA%2FXkByo%3D&id2=UUGlR2tYaVhSWQ%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; skt=df6c5c73815ae0c3; existShop=MTY1NjMyMDc5Nw%3D%3D; uc4=id4=0%40U2OSUL6Qk24okrwqAEScU%2BKWx%2Fy%2B&nk4=0%40sSWUkfCNa%2BEB%2BrglZQwTo4QF%2FUbD; _cc_=UIHiLt3xSw%3D%3D; cookie2=22d180181859475cabdbb70239ca50cf; xlly_s=1; _m_h5_tk=f3235ce2aceb5494a0253be80ba8ebac_1657271280112; _m_h5_tk_enc=d3d18b9c5255351db99f5b7ec0bcdf3f; uc1=cookie14=UoexNTMyhDja5w%3D%3D; x5sec=7b22617365727665723b32223a223739333239613835616336633334353339333439313163353636343233316338434f69596f4a5947454c6a676b3571566e72534b456a434b7936506642446f43617a453d227d; isg=BDg4V5E-rlOihMLY98jqtS_TCebKoZwrFbgDJnKphHMmjdh3GrFsu06vQYU9xlQD; l=eBT7S5HqLf0qtYVtBOfanurza77OSIRYYuPzaNbMiOCPOL5B5vrNW6A9weL6C3GVh65JR3Wrj_IwBeYBqQAonxvthx53XlHmn; tfstk=czlRB2O6fnxofKJmhDp0Tf0eE5KGwbb8xaZd9X9IwB-SWo1c-fcOX2v78lrJk'

}

def main():
    baseurl = 'https://sf.taobao.com/list/0__1__%B9%E3%B6%AB.htm?spm=a213w.7398504.filter.85.41a04566ymlTVE&auction_source=0&item_biz_type=6&st_param=-1&auction_start_seg=-1'

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "广东诉讼拍卖即将开始.xls"
    print(datalist)
    # 3.保存数据
    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []

    # 2.逐步解析数据
    res = requests.get(url=baseurl, headers=headers).text
    res = re.sub('\s+','', res)

    print(res)
    title = re.findall('"title":"(.*?)",', res)  # re库用来通过正则表达式查找指定的字符串
    itemUrl = re.findall('"itemUrl":"(.*?)",', res)
    currentPrice = re.findall('"currentPrice":(.*?),', res)
    status = re.findall('"status":"(.*?)",', res)
    start = re.findall('"start":(.*?),', res)
    end = re.findall('"end":(.*?),', res)

    print(len(title))
    print(len(itemUrl))

    new_numbers = [];
    for n in end:
        new_numbers.append(int(n));
    end = new_numbers

    new_number = [];
    for n in start:
        new_number.append(int(n));
    start = new_number

    for i in range(len(end)):
        timestamp = end[i]
        time_local = time.localtime(timestamp / 1000)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(dt)
        end[i] = dt

    for i in range(len(start)):
        print(type(start[i]))
        timestamp = start[i]
        time_local = time.localtime(timestamp / 1000)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        print(dt)
        start[i] = dt

    for i in range(len(title)):  # range(len(title)),这里因为知道len(title) = 10，所以也可以写成for i in range(10)
        data = []
        data.append(title[i])
        itemUrl[i] = 'https:' + (itemUrl[i])
        data.append(itemUrl[i])
        data.append(currentPrice[i])
        data.append(status[i])
        data.append(start[i])
        data.append(end[i])

        datalist.append(data)  # 把处理好的一部电影信息放入datalist
    return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('淘宝司法拍卖', cell_overwrite_ok=True)  # 创建工作表
    col = ("商品标题", "详情页链接", "当前拍卖价格/元", "拍卖状态", "拍卖开始时间", "拍卖结束时间")
    for i in range(0, 6):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 48):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 6):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("movietest.db")
    print("爬取完毕！")