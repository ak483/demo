import pandas as pd
import pymysql

mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\学习\seleniumpy\知乎链接.xls', sheet_name=[
        '极画教育'
    ])
platform='知乎'
title = (mainExcelDict['极画教育'])['标题'].to_list()
href = (mainExcelDict['极画教育'])['链接'].to_list()
content = (mainExcelDict['极画教育'])['内容'].to_list()


for i in range(len(title)):
    db = pymysql.connect(host='182.61.132.25', port=3306, user='content_spider', password='z8fa75eMs64Ct57r', database='content_spider', charset='utf8')
    cur = db.cursor()  # 获取会话指针，用来调用SQL语句

    sql_1 = 'INSERT INTO All_spider(platform,title,href,content) VALUES (%s,%s,%s,%s)'  # 编写SQL语句
    cur.execute(sql_1, (platform, title[i], href[i], content[i]))# 执行SQL语句
    db.commit()  # 当改变表结构后，更新数据表的操作
    cur.close()  # 关闭会话指针
    db.close()  # 关闭数据库链接