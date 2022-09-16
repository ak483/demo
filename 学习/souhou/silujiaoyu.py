
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
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'referer': 'http://www.silucg.com/'
}


def getData(p):

    url = 'http://www.silucg.com/youximeishu-'+str(p)+'-59.html'

    res = requests.get(url, headers=headers).text
    print(url)
#获取标题
    ti = 'class="c1" target="_blank">(.*?)</a>'
    title = re.findall(ti, res, re.S)
    print(title)

#获取链接
    hr = '<h3 class="f4"><a href="(.*?)"'
    href =re.findall(hr,res,re.S)
    print(href)

#获取链接正文
    # href = ['http://www.silucg.com/seo/youximeishu/20210728_1598.html']
    datalist = []
    for i in range(len(href)):
        print(i)
        data=[]
        ress = requests.get(url=href[i],headers=headers).text
        tree = etree.HTML(ress)
        # print(tree)

        div_list = tree.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]/div')
        #如果没有div正常操作
        try:
            if len(div_list)==0:
                div_list=tree.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]')

                for div in div_list:
                    content = div.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]/p/text()')
                    #如果长度小于4，则content藏于span下
                    if len(content[0]) < 4:
                        content = div.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]/p/span/text()')

                    for c in range(len(content)):
                        content[c] = re.sub('\u3000\u3000', '', content[c])
                        content[c] = re.sub('\r\n', '', content[c])
                        content[c] = re.sub('\n', '', content[c])
                        content[c] = re.sub('\t', '', content[c])
                    content = [x for x in content if len(x) > 1]

                content = content[1:-1]
                content = ('\n'.join(content))

                # print(content)
                data.append(href[i])
                data.append(title[i])
                data.append(content)
                datalist.append(data)

    #如果是div就添加div路径
            else:
                div_list=tree.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]/div')

                for div in div_list:
                    content = div.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]/div/p/text()')
                    if len(content[0])<4:
                        content = div.xpath('/html/body/div[7]/div/div[1]/div[1]/div[2]/div/p/span/text()')
                    for c in range(len(content)):
                        content[c] = re.sub('\u3000\u3000', '', content[c])
                        content[c] = re.sub('\r\n', '', content[c])
                        content[c] = re.sub('\n', '', content[c])
                        content[c] = re.sub('\t', '', content[c])
                    content = [x for x in content if len(x)> 1]

                content=content[1:-1]
                content = ('\n'.join(content))

                # print(content)
                data.append(href[i])
                data.append(title[i])
                data.append(content)
                datalist.append(data)
        except:
            pass

    return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('搜狐', cell_overwrite_ok=True)  # 创建工作表
    col = ("链接", "标题", "内容")
    for i in range(0, 3):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

if __name__ == "__main__":  # 当程序执行时
    #调用函数
    datalist =[]
    for e in range(96):
        datalistl=getData(e+1)
        for k in range(len(datalistl)):
            datalist.append(datalistl[k])

    print(datalist)

    #time.sleep(10)
    savepath = "丝路教育17.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    # init_db("movietest.db")
    print("爬取完毕！")

    # getData()