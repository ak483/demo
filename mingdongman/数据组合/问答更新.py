# coding=utf-8
# coding=utf-8
import sys,os,re,MySQLdb,html
import time
from lxml import etree
import pandas as pd
sys.path.append(r'D:\untitled1')
from demo.mingdongman.数据组合.MdmAPI import ArticleClassAPI




articleClass=ArticleClassAPI()
data:pd.DataFrame=pd.read_excel(r'C:\Users\Adminitrator03\Desktop\新建Microsoft Excel 工作表.xlsx')

# 整理
a=[]
b=[]
newsHuabshiBool=False
test=[15,16]
for i in test:


    # try:
    #     articleDict=articleClass.Query_Article(articleIdInt=i[0],newsHuabshiBool=newsHuabshiBool,inquireIndex=1)[0]
    # except IndexError:
    #     print(f'无数据：{id}')
    #     continue
    #
    # xiugaiBool = False
    questionId = i
   # content = articleDict['contentStr']
    summary = ' '


    a.append(
        {'id': questionId,'summary': summary}
    )

    time.sleep(1)
    # break

print('正在更新.....')

for i in a:
    msg=articleClass.Update_QuestionAndAnswer(questionId=i['id'],summary=i['summary'])
    # if isinstance(msg,list):
    #     print(f'已更新：{i["id"]}')
    #     b.append(
    #         {i["id"]}
    #     )
    # else:
    #     print(f'更新失败：{i["id"]}')

    time.sleep(1)

# c = pd.DataFrame(b)
#     # b = pd.DataFrame(mainExcelData)
#
# c.to_excel('名动漫官网黄中间段.xls',sheet_name='第一段')

exit()