import requests
import json
import pandas as pd
import re
import pprint
import xlwt



def main():
    #1.获取数据
    datalists = getData()
    savepath = "百度8月统计1.xls"
    # 2.保存数据
    saveData(datalists, savepath)


def saveData(datalists, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('百度统计', cell_overwrite_ok=True)  # 创建工作表
    col = ("url", "访客数", "跳出率", "平均访问时长")
    for i in range(0, 4):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, (len(datalists))):
        print("第%d条" % (i + 1))
        data = datalists[i]
        for j in range(0, 4):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


def getData():
    datalistss =[]
    url = 'https://api.baidu.com/json/tongji/v1/ReportService/getData'
    data = {
        "header": {
            "username": "动境教育培训",
            "password": 'Xiaosaoy123.',
            "token": "4d098831185e037b4593e0aed223116e",
            "account_type": 1
        },
        "body": {
            "site_id": "16367176",
            "start_date": "20220801",
            "end_date": "20220831",
            "metrics": "visitor_count,bounce_ratio,avg_visit_time",
            "method": "visit/landingpage/a",
            'start_index': 19999,
            # "clientDevice": "mobile",
            "max_results": 19999,

        }
    }

    data = json.dumps(data)
    response_data = requests.post(url=url, data=data).json()
    for i in range(len(response_data['body']['data'][0]['result']['items'][1])):
        https = response_data['body']['data'][0]['result']['items'][0][i][0]['name']
        lists = response_data['body']['data'][0]['result']['items'][1][i]

        datalist = []
        datalist.append(https)
        datalist.append(lists[0])#直接用extend（）即可，增加新的列表元素。等价于datalist.extend(lists)
        datalist.append(lists[1])
        datalist.append(lists[2])

        datalistss.append(datalist)
    return datalistss
    # print(len(response_data['body']['data'][0]['result']['items'][0]))

#json格式化校验
# a=response_data.text
# print(a)
# j = json.loads(a)
# json_dicts = json.dumps(j,indent=4,ensure_ascii=False)
# print(json_dicts)
#

if __name__ == '__main__':

    main()
    # getData()
    pass


