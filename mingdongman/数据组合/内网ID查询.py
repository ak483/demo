# coding=utf-8
import os, time, sys, shutil, logging, re, random
import pandas as pd
from lxml import etree
import pymysql
import xlwt


mainExcelData=[]
Idlist = []

def Get_Data(mod: str) -> list:
    # 读取模板
    mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['半自动洗稿项目'], sheet_name=[
            '第六批2'
        ]
    )
    print(mainExcelDict)
    mainExcelData = mainExcelDict['第六批2']['小站'].to_list()

    # for i in range(len(mainExcelData)):
    #   #  print(mainExcelData[i])
    #     if mainExcelData[i]== nan:
    #         del mainExcelData[i]

    print(mainExcelData)



    mySQL = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='159357', database='python_test', charset='utf8')
    myCursor = mySQL.cursor()

    Idlist = []
    # 查询使用该核心内容的短标题
    for i in mainExcelData:
        myCursor.execute(
            f"select articleid from article_platform where pictureclassification='{i}'ANd platform = '{'名动漫小站'}'"
        )


        id = myCursor.fetchall()
        print(id)



        for a in range(len(id)):
            idlist = []

            idlist.append(i)

            idlist.append(id[a])

            Idlist.append(idlist)

        # print(id)
        # idlist.append(id)


    print(Idlist)


    a = pd.DataFrame(Idlist)
    # b = pd.DataFrame(mainExcelData)

    a.to_excel('名动漫小站第六批ID.xls',sheet_name='第六批')
    # b.to_excel('名动漫官网6.xls')

#
FILE_PATH_DICT = {
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目.xlsx',
}

if __name__ == '__main__':
    Get_Data(mod='画师巴士')

