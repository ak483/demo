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
newsHuabshiBool=True
for _,i in data.iterrows():
    if str(i[0])=='nan':
        continue

    try:
        articleDict=articleClass.Query_Article(articleIdInt=i[0],newsHuabshiBool=newsHuabshiBool,inquireIndex=1)[0]
        # print(articleDict)
    except IndexError:
        print(f'无数据：{id}')
        continue

    xiugaiBool = False
    articleId = articleDict['idInt']
    thumbnailStr = articleDict['thumbnailStr']

    thumbnailStr = thumbnailStr.replace('%E5%BD%B1%E8%A7%86','%E6%8F%92%E7%94%BB')


    a.append(
        {'id': articleId, 'thumbnailStr': thumbnailStr}
    )

    time.sleep(1)
    # break


input('确认更新...')

for i in a:
    msg=articleClass.Update_Article(articleIdInt=i['id'],thumbnailStr=i['thumbnailStr'],newsHuabshiBool=newsHuabshiBool)
    if isinstance(msg,list):
        print(f'已更新：{i["id"]}')
        b.append(
            {i["id"]}
        )
    else:
        print(f'更新失败：{i["id"]}')

    time.sleep(1)


c = pd.DataFrame(b)
    # b = pd.DataFrame(mainExcelData)

c.to_excel('名动漫官网黄中间段6.xls',sheet_name='第一段')

exit()