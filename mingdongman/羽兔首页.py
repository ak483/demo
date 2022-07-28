# -*- codeing = utf-8 -*-
# @Time :2022/7/20 19:34
# @Author:Eric
# @File : yutu.py
# @Software: PyCharm
import requests
import re
from lxml import etree
import xlwt

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
answerlist = []
def main():
    for i in range(1):
        i = i+1
        getData(i)

    # 1.爬取网页
    datalist = answerlist
    savepath = "羽兔2.xls"
    print(datalist)
    #3.保存数据
    saveData(datalist, savepath)


def getData(i):
    url = 'https://www.yutu.cn/soft/tag_15742.html'
    print(url)
    r = requests.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    res=r.text
   # print(res)
    title = re.findall('<p class="h2-tite">(.*?)</p>', res)
    href = re.findall('<a class="comm-item" target="_blank" href="(.*?)">', res)
    print(title)
    print(href)

    for q in range(len(href)):
        qr = requests.get(url=href[q], headers=headers)
        qr.encoding = 'utf-8'
        ress = qr.text
        tree = etree.HTML(ress)
        answer = []
        # 提取元素并清除空列表以及列表元素为空格
        div_list = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/p')
        descript = tree.xpath('/html/head/meta[6]/@content')
        answer.append(title[q])
        answer.append(descript[0])
        print(len(div_list))
        if len(div_list) == 0:
            div_list = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/text()')
            answer.append(div_list[0])
            answerlist.append(answer)

        else:
            answer1=[]
            for p in div_list:
                answer_t = p.xpath('./text()')
                if len(answer_t) == 0:
                    del answer_t
                elif answer_t[0] == ' ':
                    del answer_t
                else:
                    answer1.append(answer_t[0])
            answer.append(answer1)
            answerlist.append(answer)

    print(answerlist)


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('羽兔', cell_overwrite_ok=True)  # 创建工作表
    col = ("标题", "描述", "回答")
    for i in range(0, 3):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 3):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


if __name__ == "__main__":
    main()
