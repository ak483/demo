# coding=utf-8
from lxml import html
etree = html.etree
import requests
import re,time
import xlwt

headers = {

    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}

All_datalist = []

def getData(p):

    url = 'https://www.hxsd.com/seolist/dmhhjc/p'+str(p)+'/'

    res = requests.get(url, headers=headers).text
    tree = etree.HTML(res)
    category = tree.xpath('//a[@class="active"]/text()')[0]
    titlelist = tree.xpath('//p[@class="news-tit text-ov"]/text()')
    timelist = tree.xpath('//p[@class="news-other"]//span[2]/text()')
    hreflist = tree.xpath('//ul[@class="seo-news-ul"]/a/@href')
    tempdatalist = []
    for i in range(len(titlelist)):
        datalist = []
        title = titlelist[i]
        time = timelist[i]
        href = hreflist[i]
        datalist.append(title)
        datalist.append(time)
        datalist.append(href)
        datalist.append(category)
        tempdatalist.append(datalist)
        All_datalist.append(datalist)
    return tempdatalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('搜狐', cell_overwrite_ok=True)  # 创建工作表
    col = ("标题", "时间", "链接", "分类")
    for i in range(0, 4):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

if __name__ == "__main__":  # 当程序执行时
    #调用函数

    for p in range(3):
        print(p)
        datalistl = getData(p + 2)
        print(datalistl)
        time.sleep(1)
    print(All_datalist)


    savepath = "火星时代动漫绘画教程.xls"
    # 3.保存数据
    saveData(All_datalist, savepath)
    print("爬取完毕！")

