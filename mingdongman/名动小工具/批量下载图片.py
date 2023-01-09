# coding=utf-8
import pandas as pd,requests,time

headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
            }

savepath = 'C:\\Users\\Adminitrator03\\Desktop\\word'


mainExcelDict = pd.read_excel(
    'C:\\Users\\Adminitrator03\\Desktop\\百科词条.xlsx', sheet_name=[
        '图片下载',
    ]
)
mainExcelData = mainExcelDict['图片下载']


# 筛选
# mainExcelData = mainExcelData[(mainExcelData['发布状态'] != '已发布')]
urlList = mainExcelData['封面图'].to_list()
titleList = mainExcelData['词条名称'].to_list()

for i in range(len(urlList)):

    response1 = requests.get(urlList[i],headers=headers)
    bytes_data = response1.content
    # 保存数据
    with open(savepath + f'\{titleList[i]}.jpg','wb')as f:
        f.write(bytes_data)