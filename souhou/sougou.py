
import time# -*- codeing = utf-8 -*-
# @Time :2022/7/11 17:04
# @Author:Eric
# @File : sougou.py
# @Software: PyCharm
from lxml import html
etree = html.etree
import requests
import re
import xlwt

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'referer': 'https://www.sogou.com/'
}



def getData(p):
    url = 'https://www.sogou.com/sogou?query=素描%20线稿%20设计&pid=sogou-wsse-a9e18cb5dd9d3ab4&duppid=1&cid=&s_from=result_up&insite=wenwen.sogou.com&page='+str(p)+'&ie=utf8&w=01029901&dr=1'
    res = requests.get(url, headers=headers).text
    ti= '<h3 class="vr-title  "  vrcid="title.89eaeb8">.*?>(.*?)</a>.*?</h3>'
    title = re.findall(ti,res,re.S)
    print(title)
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
    print(title)

    hr = '<h3 class="vr-title  "  vrcid="title.89eaeb8">.*?<a class=" " target="_blank" href="(.*?)".*?</h3>'
    href =re.findall(hr,res,re.S)
    for i in range(len(href)):
        href[i] = 'https://www.sogou.com'+href[i]
    print(href)

    hrefss=[]
    for i in range(len(href)):
        ress = requests.get(url=href[i],headers=headers).text
        hrefs = re.findall('replace\("(.*?)"\)', ress)
        hrefss.append(hrefs[0])
    print(hrefss)


    imgss=[]
    detailss=[]
    replayss=[]

    datalist = []
    for i in range(len(hrefss)):

        data = []
        reso = requests.get(url=hrefss[i],headers=headers).text
        img = '<a class="pic-w queImg">.*?s-src="(.*?)"'
        imgs = re.findall(img,reso,re.S)
        imgsl = ['null']#imgs元素列表化
        if  len(imgs) == 0:
            imgs = imgsl
        #print(imgs)
        #imgss.append(imgs[0])

        detail = '<h1 id="question_title" class="detail-tit-box">.*?class="detail-tit-info">(.*?)</pre>'
        details = re.findall(detail,reso,re.S)
        detaill = ['null']#元素列表化
        if  len(details) == 0:
            details = detaill
        #print(details)
        #detailss.append(details[0])

        replay = '<pre class="replay-info-txt answer_con">(.*?)</pre>'
        replays = re.findall(replay, reso, re.S)
        for s in range(len(replays)):
            replays[s] = replays[s].strip()
            replays[s] = re.sub('[.*?]', '', replays[s])
            replays[s] = re.sub('\r\n\r\n', '', replays[s])
            replays[s] = re.sub('\r\n', '', replays[s])
            replays[s] = re.sub('\n\n\w', '', replays[s])
            replays[s] = re.sub('\u3000\u3000', '', replays[s])
            replays[s] = re.sub('&nbsp;', '', replays[s])
            replays[s] = re.sub('\n', '', replays[s])
            replays[s] = re.sub('<br>', '', replays[s])

        #print(replays)
        data.append(hrefss[i])
        data.append(title[i])
        data.append(imgs[0])
        data.append(details[0])

        for i in range(len(replays)):
            data.append(replays[i])

        print(data)
        print('--------------------------------------------------------')
        datalist.append(data)
       # datalistl.append(datalist)
       # print(datalist)
        print('......................................')
    print(datalist)
    return datalist
    print('-----------')

def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('淘宝司法拍卖', cell_overwrite_ok=True)  # 创建工作表
    col = ("问题链接", "问题标题", "图片描述", "文字描述", "回答1",)
    for i in range(0, 5):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 100):
        print("第%d条" % (i + 1))

        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    datalist =[]
    for e in range(11):
        datalistl=getData(e+1)
        for k in range(len(datalistl)):
            datalist.append(datalistl[k])

    print(datalist)

    #time.sleep(10)
    savepath = "sougou7.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    # init_db("movietest.db")
    print("爬取完毕！")