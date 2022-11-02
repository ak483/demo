import queue
import requests
import threading
import re
import time,xlwt
import pandas as pd

headers={

    'referer': 'https://www.sogou.com/'
}

mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\学习\souhou\meatoo_url2.xlsx',sheet_name=[
        '第一段'
    ])
All_url = (mainExcelDict['第一段'])['url'].to_list()
# All_url =All_url[:5000]

url_queue = queue.Queue()  # 创建一个空队列
for url in All_url:
    url_queue.put(url)  # 将网址添加到队列中

lock = threading.Lock()

All_titlelist = []

All_exc=[]
def crawl():

    while not url_queue.empty():  # 当队列里还有内容时，就执行下面的内容

        url = url_queue.get()  # 提取队列中的网址（先进先出）
        print(url)

        try:  # 其实通常也不太会访问超时，但是最好还是加下吧，如果超时会执行except中的语句，不会让整个程序报错退出
            res = requests.get(url, headers=headers, timeout=10).text  # 如果怕连接超时，导致报错，可以设置try except语句
            titlelist = []
            title = re.findall('<title>(.*?)</title>', res)

            titlelist.append(title[0])
            titlelist.append(url)
            All_titlelist.append(titlelist)
        except:
            exc = []
            exc.append('')
            exc.append(url)
            All_exc.append(exc)


def save1(All_titlelist):#保存账号数据
    savepath = r'D:\untitled1\demo\学习\souhou\meatoo_url_title10.xlsx'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('七麦', cell_overwrite_ok=True)
    col = ("标题","url")

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_titlelist)):
        # print("第%d条" % (i + 1))
        data = All_titlelist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


start_time = time.time()  # 起始时间

thread_list = []
for i in range(10):  # 这里激活5个线程，可以自己改成1，看看单线程的时间
    thread_list.append(threading.Thread(target=crawl))

for t in thread_list:
    t.start()
for t in thread_list:
    t.join()

for e in range(len(All_exc)):
    All_titlelist.append(All_exc[e])



end_time = time.time()  # 结束时间
total_time = end_time - start_time

print(All_titlelist)
save1(All_titlelist)

print("所有任务结束，总耗时为：" + str(total_time))