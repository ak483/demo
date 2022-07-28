# -*- codeing = utf-8 -*-
# @Time :2022/7/9 15:30
# @Author:Eric
# @File : 结束详情页.py
# @Software: PyCharm
# -*- codeing = utf-8 -*-
# @Time :2022/7/8 23:29
# @Author:Eric
# @File : demo4.py
# @Software: PyCharm
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
    'cookie': 't=ff25ac54b11addfe155f470545b61874; thw=cn; _tb_token_=315be083ebbe7; _samesite_flag_=true; enc=e8Z6i2YhprGpJUtkTh%2FUtIEEYM3ZRG%2BaiGit7YM51LH0UrPz4uCFB42NlYD2GCxswVmh9kqDVszDZ3gd4eDV8A%3D%3D; cookie2=22d180181859475cabdbb70239ca50cf; _m_h5_tk=f3235ce2aceb5494a0253be80ba8ebac_1657271280112; _m_h5_tk_enc=d3d18b9c5255351db99f5b7ec0bcdf3f; sgcookie=E100Fskrp74NBp7D%2BGf7eeE8U%2ByEEH02dK82xCu7%2BtRT42WQh1uOPxlbMtak%2BxnKwHLxB6XlhtKXaAETmbBIHRYWrJ304nrYWhRdzHBM7mM5s2CQBsEZjZpIIsDngUMcPTJ%2F; xlly_s=1; mt=ci=0_0; tracknick=; cna=NBs+Goz8KCoCAXBgQCBeU5dD; x5sec=7b22617365727665723b32223a226464643061643664633034376665623663623631373466363039303765343532434a2b2f705a5947454d2f556a6372307a4c4b334644447a764e32582b2f2f2f2f2f38424f674a724d513d3d227d; uc1=cookie14=UoexNTIugJnOHQ%3D%3D; isg=BGVlUO_Fa62M-49_AqtPGuKAdCGfohk0iOuOAWdKIRyrfoXwL_IpBPOcDOII5THs; tfstk=cE0CBPvxo9XCg9CwhzOwYnmPJQzRwwp_sHwKOdey6BTL5-1cAZyXIPolIzP81; l=eBT7S5HqLf0qtI_2BOfanurza77OSIRYYuPzaNbMiOCPO6CB5fJhW6A1UrL6C3GVh6VeR3Wrj_IwBeYBq7VonxvTPNOwbhkmn'
}

def main():
    baseurl ='https://sf.taobao.com/list/0__2__%B9%E3%B6%AB.htm?spm=a213w.7398504.filter.86.4f224566XLobKu&auction_source=0&item_biz_type=6&st_param=-1&auction_start_seg=-1'

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "广东诉讼拍卖已结束13.xls"
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
    sellOff = re.findall('"sellOff":(.*?),', res)
    bidCount = re.findall('"bidCount":(.*?),', res)
    viewerCount = re.findall('"viewerCount":(.*?),', res)
    applyCount= re.findall('"applyCount":(.*?),', res)

    print(itemUrl)
    print(len(title))
    print(len(itemUrl))

#格式化为int型
    new_numbers = [];
    for n in end:
        new_numbers.append(int(n));
    end = new_numbers

    new_number = [];
    for n in start:
        new_number.append(int(n));
    start = new_number

    new_URl = [];
    for i in range(len(itemUrl)):
        #data = []
        itemUrl[i] = 'https:' + (itemUrl[i])
        #data.append(itemUrl[i])


    for i in range(len(itemUrl)):
        test = []
        reso = requests.get(url=itemUrl[i]).text
        reso = re.sub('\s+', '', reso)
        test[i] = re.findall('<h1class="bid-fail"><s></s>(.*?)</h1><divclass="close-price">', reso)
        print(test)
   # print(test)

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
        #itemUrl[i] = 'https:' + (itemUrl[i])
        data.append(itemUrl[i])
        data.append(currentPrice[i])
        data.append(status[i])
        data.append(start[i])
        data.append(end[i])
        data.append(sellOff[i])
        data.append(bidCount[i])
        data.append(viewerCount[i])
        data.append(applyCount[i])

        datalist.append(data)  # 把处理好的一部电影信息放入datalist
    return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('淘宝司法拍卖', cell_overwrite_ok=True)  # 创建工作表
    col = ("商品标题", "详情页链接", "当前拍卖价格/元", "拍卖状态", "拍卖开始时间", "拍卖结束时间","是否卖出","出价人数","围观人数","报名人数")
    for i in range(0, 10):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 48):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 10):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    # init_db("movietest.db")
    print("爬取完毕！")