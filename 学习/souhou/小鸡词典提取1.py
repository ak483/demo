import pandas as pd
import re,requests,xlwt,time
from lxml import html
etree = html.etree

def changeip():
    proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=90c34d3530c24197ab052ea0e68110f9&orderno=YZ202212158025KhRjtI&returnType=1&count=1').text
    proxy = proxy.strip()
    print('提取IP为：' + proxy)
    proxies = {"http": "http://" + proxy}
    time.sleep(5)
    return proxies

def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('搜狐', cell_overwrite_ok=True)  # 创建工作表
    col = ("标题", "内容", "图片", "标签", "链接")
    for i in range(0, 5):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

def xiaoji(urlnum):
    datalist = []
    url = 'https://jikipedia.com/definition/' + str(urlnum)

    res = requests.get(url, headers=headers, timeout=10, proxies=proxies).text



    title = re.findall('<title>(.*?)</title>', res, re.S)
    title = re.sub(' - 小鸡词典','',title[0])

    # content = re.findall('name="description" content="(.*?)">', res, re.S)
    #用xpath提取文章内容
    restree = etree.HTML(res)
    contents = restree.xpath('//div[@class="content"]//span/text()')
    content = ''.join(contents)



    img = re.findall('<img src="https://api.jikipedia.com/media/image/(.*?)"', res, re.S)
    if len(img)>0:
        img = 'https://api.jikipedia.com/media/image/'+img[0]
    else:
        img = ''
    label = re.findall('<span data-v-09429acf>(.*?)</span>', res, re.S)
    str_label = '、'.join(label)

    datalist.append(title)
    datalist.append(content)

    if len(img) == 0:
        datalist.append('')
    else:
        datalist.append(img)

    datalist.append(str_label)
    datalist.append('https://jikipedia.com/definition/' + str(urlnum))
    print(datalist)

    All_datalist.append(datalist)

    time.sleep(2)
    return title


mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\学习\souhou\未清洗小鸡链接1.xls',sheet_name=[
        '小鸡3'
    ])

href = (mainExcelDict['小鸡3'])['链接'].to_list()
All_datalist = []
headers = {
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'cookie': 'XID=533a1126-2527-47e8-b3c4-9d64d8da0685; Hm_lvt_63a8941b9af78a70fb9a9951990bbcbd=1671175977; __gads=ID=dc630cd7f22789a2-22448e4419d900ad:T=1671175977:RT=1671175977:S=ALNI_MbvOdQ_e-oT71niKzcPB0-B3gKDgw; __gpi=UID=00000b9151c7a2eb:T=1671175977:RT=1671175977:S=ALNI_MbkdSUTkQrcvtQSTKGMjH9z_vZf2w; user=%7B%22id%22:866004497,%22name%22:%22%E5%B0%8F%E9%B8%A15fdc6a2e0ebd3%22,%22token%22:%22afb20c81131cc7d4804cef3b390ec3c6827ce692e5b219d213f69a8b340066ce%22,%22user_id%22:866004497,%22user_name%22:%22%E5%B0%8F%E9%B8%A15fdc6a2e0ebd3%22,%22avatar%22:%22%22,%22scaled_avatar%22:%22%22,%22user_role%22:%22editor%22,%22badge%22:%7B%7D,%22badge_full_image%22:%22%22%7D; Hm_lpvt_63a8941b9af78a70fb9a9951990bbcbd=1671182097'
}
proxies = changeip()
res = xiaoji(href[0])

for i in range(len(href)):


    try:
        res = xiaoji(href[i])
        while 'hello moss' == res:  # while else类似 if else，不过可以一直循环，直到不再满足while中的条件为止
            print('原代理IP失效，开始切换IP')
            proxies = changeip()
            res = xiaoji(i)
            input('检查下')
        else:
            print(i)
            print('1词典爬取成功')
    except:
        # print('原代理IP失效，开始切换IP啊')
        # proxies = changeip()
        # res = xiaoji(i)
        print('词条爬取失败')


savepath = "小鸡词典内容3.xls"
# 3.保存数据
saveData(All_datalist, savepath)

