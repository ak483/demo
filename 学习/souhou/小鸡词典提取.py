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
        '小鸡2'
    ])

headers = {
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'cookie': 'XID=679dff1c-6897-4e3b-b3e8-45a6e404b72f; Hm_lvt_63a8941b9af78a70fb9a9951990bbcbd=1671178549; __gads=ID=97e5a24279143e12-22633ee1e7d800fc:T=1671178547:RT=1671178547:S=ALNI_MaTtyW7W-nL21vs_URgjQ5KJAz4sg; __gpi=UID=00000b9155fe5d6a:T=1671178547:RT=1671178547:S=ALNI_MaczkMl1kAR8FsBTxUmxU8AJEm1nA; Hm_lpvt_63a8941b9af78a70fb9a9951990bbcbd=1671181774; user=%7B%22id%22:944221469,%22name%22:%22%E5%B0%8F%E9%B8%A1639c2436f2e73%22,%22token%22:%2225bc6631dfb1e0bbe7ec5c63aa8e5e3b576eac71351a90c93e06a773671acc95%22,%22user_id%22:944221469,%22user_name%22:%22%E5%B0%8F%E9%B8%A1639c2436f2e73%22,%22avatar%22:%22%22,%22scaled_avatar%22:%22%22,%22user_role%22:%22editor%22,%22badge%22:%7B%7D,%22badge_full_image%22:%22%22%7D'
}
href = (mainExcelDict['小鸡2'])['链接'].to_list()
All_datalist = []
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


savepath = "小鸡词典内容2.xls"
# 3.保存数据
saveData(All_datalist, savepath)

