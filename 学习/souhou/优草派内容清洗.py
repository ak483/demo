import queue
import requests
import threading
import re
import time,xlwt
import pandas as pd


mainExcelDict=pd.DataFrame=pd.read_excel(r'C:\Users\Adminitrator03\Desktop\优草派.xls',sheet_name=[
        '搜狐'
    ])
All_content = (mainExcelDict['搜狐'])['内容'].to_list()
last_content = []

for i in range(len(All_content)):
    All_contents = []

    #取出列表字符
    content_str = re.sub(r'\r\n', '', All_content[i])
    content_str = re.sub(r'\n\n', '', content_str)
    content_str = re.sub(r'    ', '', content_str)
    content_str = re.sub(' ', '', content_str)
    #分割字符
    content_list = content_str.split('\n')
    #删列表最后一个元素
    content_list.pop()

    for j in range(len(content_list)):
        content_list[j] = '    ' + content_list[j]
    #清理列表
    if '小编' in content_list[0]:
        content_list.pop(0)
        content = '\n'.join(content_list)
        All_contents.append(content)
        last_content.append(All_contents)
        continue
    elif '本期' in content_list[0]:
        content_list.pop(0)
        content = '\n'.join(content_list)
        All_contents.append(content)
        last_content.append(All_contents)
        continue
    elif '下面' in content_list[0]:
        content_list.pop(0)
        content = '\n'.join(content_list)
        All_contents.append(content)
        last_content.append(All_contents)
        continue
    else:
        content = '\n'.join(content_list)
        All_contents.append(content)
        last_content.append(All_contents)





def save1(All_titlelist):#保存账号数据
    savepath = r'优草派清洗后3.xlsx'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('优草', cell_overwrite_ok=True)
    col = ["内容"]

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_titlelist)):
        # print("第%d条" % (i + 1))
        data = All_titlelist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


print(last_content)
save1(last_content)
