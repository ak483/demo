# coding=utf-8
# coding=utf-8
import sys,os,re,MySQLdb,html
import time
from lxml import etree
import pandas as pd
sys.path.append(r'D:\untitled1')
# from demo.mingdongman.数据组合.MdmAPI import ArticleClassAPI
from My_code.名动漫.Mdm_API import ArticleClassAPI

articleClass=ArticleClassAPI()
data:pd.DataFrame=pd.read_excel(r'C:\Users\Adminitrator03\Desktop\新建Microsoft Excel 工作表.xlsx')

# 整理
a=[]
b=[]
newsHuabshiBool=False
test=[15,16]
for i in test:

    questionId = i
    summary = ' '
    a.append(
        {'id': questionId,'summary': summary}
    )
    time.sleep(1)
print('正在更新.....')

for i in a:
    msg=articleClass.Update_QuestionAndAnswer(questionId=i['id'],summary=i['summary'])
    time.sleep(1)
exit()