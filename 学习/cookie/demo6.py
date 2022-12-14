# -*- codeing = utf-8 -*-
# @Time :2022/7/9 19:38
# @Author:Eric
# @File : demo6.py
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
    'cookie': 't=ff25ac54b11addfe155f470545b61874; thw=cn; _tb_token_=315be083ebbe7; _samesite_flag_=true; enc=e8Z6i2YhprGpJUtkTh%2FUtIEEYM3ZRG%2BaiGit7YM51LH0UrPz4uCFB42NlYD2GCxswVmh9kqDVszDZ3gd4eDV8A%3D%3D; cookie2=22d180181859475cabdbb70239ca50cf; _m_h5_tk=f3235ce2aceb5494a0253be80ba8ebac_1657271280112; _m_h5_tk_enc=d3d18b9c5255351db99f5b7ec0bcdf3f; sgcookie=E100Fskrp74NBp7D%2BGf7eeE8U%2ByEEH02dK82xCu7%2BtRT42WQh1uOPxlbMtak%2BxnKwHLxB6XlhtKXaAETmbBIHRYWrJ304nrYWhRdzHBM7mM5s2CQBsEZjZpIIsDngUMcPTJ%2F; xlly_s=1; mt=ci=0_0; tracknick=; cna=NBs+Goz8KCoCAXBgQCBeU5dD; uc1=cookie14=UoexNTIvC40YBA%3D%3D; x5sec=7b22676f7661756374696f6e3b32223a226461616536316336346662326366653965353738616532313934386334363130434c7630705a5947454c66456a65623637736d7778514561444449354e7a6b324d7a63354e4455374d5443307236764642773d3d222c22617365727665723b32223a223566383362653464326334623139383332363237323063613065313462663061434f5476705a5947454a6a5932752b62394f4c6e7241457738377a646c2f762f2f2f2f2f41546f43617a453d227d; isg=BE9Pkup6cY9XxnX9hN0FOEzO3uNZdKOW1nXUA2Fc677FMG8yaUQz5k2iNmCOU3sO; l=eBT7S5HqLf0qtIzSBOfanurza77OSIRYYuPzaNbMiOCP_55B5W8hW6A1oZY6C3GVh6qXR3Wrj_IwBeYBq7Vonxvt9w7lqgDmn; tfstk=cDf5BdqOs0m7scg4fBa4UocotQddwkEXo8tRPoKHbbLeNh1mNf-_mIWnmB8pl'
}

def main():
    baseurl ='https://sf.taobao.com/list/0__5__%B9%E3%B6%AB.htm?spm=a213w.7398504.filter.88.173845665EnKVa&auction_source=0&st_param=-1&auction_start_seg=-1'
    # 1.????????????
    datalist = getData(baseurl)
    savepath = "???????????????????????????.xls"
    print(datalist)
    # 3.????????????
    saveData(datalist, savepath)


def getData(baseurl):
    datalist = []

    # 2.??????????????????
    res = requests.get(url=baseurl, headers=headers).text
    res = re.sub('\s+','', res)

    print(res)
    title = re.findall('"title":"(.*?)",', res)  # re??????????????????????????????????????????????????????
    itemUrl = re.findall('"itemUrl":"(.*?)",', res)
    currentPrice = re.findall('"currentPrice":(.*?),', res)
    status = re.findall('"status":"(.*?)",', res)
    start = re.findall('"start":(.*?),', res)
    end = re.findall('"end":(.*?),', res)
    sellOff = re.findall('"sellOff":(.*?),', res)
    bidCount = re.findall('"bidCount":(.*?),', res)
    viewerCount = re.findall('"viewerCount":(.*?),', res)
    applyCount= re.findall('"applyCount":(.*?),', res)

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

    for i in range(len(title)):  # range(len(title)),??????????????????len(title) = 10????????????????????????for i in range(10)
        data = []
        data.append(title[i])
        itemUrl[i] = 'https:' + (itemUrl[i])
        data.append(itemUrl[i])
        data.append(currentPrice[i])
        data.append(status[i])
        data.append(start[i])
        data.append(end[i])
        data.append(sellOff[i])
        data.append(bidCount[i])
        data.append(viewerCount[i])
        data.append(applyCount[i])

        datalist.append(data)  # ???????????????????????????????????????datalist
    return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # ??????workbook??????
    sheet = book.add_sheet('??????????????????', cell_overwrite_ok=True)  # ???????????????
    col = ("????????????", "???????????????", "??????????????????/???", "????????????", "??????????????????", "??????????????????","????????????","????????????","????????????","????????????")
    for i in range(0, 10):
        sheet.write(0, i, col[i])  # ??????
    for i in range(0, 48):
        print("???%d???" % (i + 1))
        data = datalist[i]
        for j in range(0, 10):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # ??????


if __name__ == "__main__":  # ??????????????????
    # ????????????
    main()
    # init_db("movietest.db")
    print("???????????????")