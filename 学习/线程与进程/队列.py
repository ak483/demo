import queue
import requests
import threading
import re
import time,xlwt
import pandas as pd

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'referer': 'https://www.sogou.com/'
}

mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\学习\souhou\meatoo_url2.xlsx',sheet_name=[
        '第一段'
    ])
All_url = (mainExcelDict['第一段'])['url'].to_list()
All_url =All_url[:5000]

url_queue = queue.Queue()  # 创建一个空队列
for url in All_url:
    url_queue.put(url)  # 将网址添加到队列中

lock = threading.Lock()

All_titlelist = []
exc= []
def crawl():
    global title
    while not url_queue.empty():  # 当队列里还有内容时，就执行下面的内容

        url = url_queue.get()  # 提取队列中的网址（先进先出）
        print(url)

        try:  # 其实通常也不太会访问超时，但是最好还是加下吧，如果超时会执行except中的语句，不会让整个程序报错退出
            res = requests.get(url, headers=headers, timeout=10).text  # 如果怕连接超时，导致报错，可以设置try except语句
            titlelist = []
            title = re.findall('<title>(.*?)</title>', res)
            # print(title)

        except:
            res = url
            exc.append(res)
        titlelist.append(title[0])
        titlelist.append(url)
        All_titlelist.append(titlelist)

