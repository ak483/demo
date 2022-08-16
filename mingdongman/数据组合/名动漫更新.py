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
for _,i in data.iterrows():
    if str(i[0])=='nan':
        continue

    try:
        articleDict=articleClass.Query_Article(articleIdInt=i[0],newsHuabshiBool=newsHuabshiBool,inquireIndex=1)[0]
    except IndexError:
        print(f'无数据：{id}')
        continue

    xiugaiBool = False
    articleId = articleDict['idInt']
    content = articleDict['contentStr']

    content1 = content.replace('从名动漫3D建模进阶网络班毕业后同学们可以进入动画行业、游戏行业、建筑行业、工业行业等。成为3d美术设计师，广泛行业施展拳脚，任你发挥。更能在线申请合作企业内推机会喔！','名动漫授课老师都是有实体带班经验的资深老师，严控的高质量网课，学习等同于上实体班。小白同学也适合报名参加，每天学一点循序渐进，零基础也能学得很好。')


    a.append(
        {'id': articleId, 'content': content1}
    )

    time.sleep(1)
    # break

input('确认更新...')

for i in a:
    msg=articleClass.Update_Article(articleIdInt=i['id'],contentStr=i['content'],newsHuabshiBool=newsHuabshiBool)
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

c.to_excel('名动漫官网黄中间段5.xls',sheet_name='第一段')

exit()