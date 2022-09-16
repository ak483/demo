import sys,os,re,MySQLdb,html
import time
from lxml import etree
import pandas as pd

mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\mingdongman\Douyin_Spider\统计模板.xls',sheet_name=[
        '7月百度统计pc', '7月百度统计mobile','查询url','8月统计pc','8月统计mobile'
    ])

# PC_ExcelData = mainExcelDict['7月百度统计pc']
# Mobile_ExcelData = mainExcelDict['7月百度统计mobile']
# PC_Need_url= (mainExcelDict['查询url'])['需要查询的url'].to_list()
#
# print(PC_Need_url)
#
# PC_URL_ExcelDataList = (mainExcelDict['7月百度统计pc'])['url'].to_list()
# PC_Fanke_ExcelDataList = (mainExcelDict['7月百度统计pc'])['访客数'].to_list()
# PC_Outrate_ExcelDataList = (mainExcelDict['7月百度统计pc'])['跳出率'].to_list()
# PC_state_ExcelDataList = (mainExcelDict['7月百度统计pc'])['平均访问时长'].to_list()
#
# Mobile_URL_ExcelDataList = (mainExcelDict['7月百度统计mobile'])['url'].to_list()
# Mobile_Fanke_ExcelDataList = (mainExcelDict['7月百度统计mobile'])['访客数'].to_list()
# Mobile_Outrate_ExcelDataList = (mainExcelDict['7月百度统计mobile'])['跳出率'].to_list()
# Mobile_state_ExcelDataList = (mainExcelDict['7月百度统计mobile'])['平均访问时长'].to_list()


PC_ExcelData = mainExcelDict['8月统计pc']
Mobile_ExcelData = mainExcelDict['8月统计mobile']
PC_Need_url= (mainExcelDict['查询url'])['需要查询的url'].to_list()

print(PC_Need_url)

PC_URL_ExcelDataList = (mainExcelDict['8月统计pc'])['url'].to_list()
PC_Fanke_ExcelDataList = (mainExcelDict['8月统计pc'])['访客数'].to_list()
PC_Outrate_ExcelDataList = (mainExcelDict['8月统计pc'])['跳出率'].to_list()
PC_state_ExcelDataList = (mainExcelDict['8月统计pc'])['平均访问时长'].to_list()

Mobile_URL_ExcelDataList = (mainExcelDict['8月统计mobile'])['url'].to_list()
Mobile_Fanke_ExcelDataList = (mainExcelDict['8月统计mobile'])['访客数'].to_list()
Mobile_Outrate_ExcelDataList = (mainExcelDict['8月统计mobile'])['跳出率'].to_list()
Mobile_state_ExcelDataList = (mainExcelDict['8月统计mobile'])['平均访问时长'].to_list()




def PC_data(https):

#整合数据列到一个列表
    PC_All_list=[]
    for i in range(len(PC_URL_ExcelDataList)):
        PClist = []
        PClist.append(PC_URL_ExcelDataList[i])
        PClist.append(PC_Fanke_ExcelDataList[i])
        PClist.append(PC_Outrate_ExcelDataList[i])
        PClist.append(PC_state_ExcelDataList[i])
        PC_All_list.append(PClist)

#接收查询url的列表
    PC_after_data=[]
    for l in range(len(PC_All_list)):
        if ( https in str(PC_All_list[l][0]) ):
            PC_after_data.append(PC_All_list[l])

#计算列中元素
    All_Sum_fanke = 0
    All_Avg_outrate = 0
    All_Avg_state = 0
    for i in range(len(PC_after_data)):
        Sum_fanke=PC_after_data[i][1]
        Avg_outrate = PC_after_data[i][2]
        Avg_state = PC_after_data[i][3]

#执行累加
        All_Sum_fanke = Sum_fanke + All_Sum_fanke
        All_Avg_outrate = Avg_outrate + All_Avg_outrate
        All_Avg_state = Avg_state + All_Avg_state

#输出累加总数
    print('访客数为：', All_Sum_fanke)
    Excel_fanke.append(All_Sum_fanke)

    try:
        All_Avg_outrate=All_Avg_outrate/(len(PC_after_data))
        print('跳出率为：', All_Avg_outrate)
        Excel_outrate.append(All_Avg_outrate)
    except:
        print('All_Avg_outrate为：0')
        Excel_outrate.append(0)

    try:
        All_Avg_state = All_Avg_state/(len(PC_after_data))
        print('平均访问时长为：', All_Avg_state)
        Excel_state.append(All_Avg_state)
    except:
        print('All_Avg_state为:0')
        Excel_state.append(All_Avg_state)


def Mobile_data(https):

#整合数据列到一个列表
    Mobile_All_list=[]
    for i in range(len(Mobile_URL_ExcelDataList)):
        Mobilelist = []
        Mobilelist.append(Mobile_URL_ExcelDataList[i])
        Mobilelist.append(Mobile_Fanke_ExcelDataList[i])
        Mobilelist.append(Mobile_Outrate_ExcelDataList[i])
        Mobilelist.append(Mobile_state_ExcelDataList[i])
        Mobile_All_list.append(Mobilelist)

#接收查询url的列表
    Mobile_after_data=[]
    for l in range(len(Mobile_All_list)):
        if ( https in str(Mobile_All_list[l][0]) ):
            Mobile_after_data.append(Mobile_All_list[l])

#计算列中元素
    All_Sum_fanke = 0
    All_Avg_outrate = 0
    All_Avg_state = 0
    for i in range(len(Mobile_after_data)):
        Sum_fanke=Mobile_after_data[i][1]
        Avg_outrate = Mobile_after_data[i][2]
        Avg_state = Mobile_after_data[i][3]
#进行累加
        All_Sum_fanke = Sum_fanke + All_Sum_fanke
        All_Avg_outrate = Avg_outrate + All_Avg_outrate
        All_Avg_state = Avg_state + All_Avg_state

    print('访客数为：', All_Sum_fanke)
    Excel_fanke.append(All_Sum_fanke)

    try:
        All_Avg_outrate=All_Avg_outrate/(len(Mobile_after_data))
        print('跳出率为：', All_Avg_outrate)
        Excel_outrate.append(All_Avg_outrate)
    except:
        print('All_Avg_outrate为：0')
        Excel_outrate.append(0)

    try:
        All_Avg_state = All_Avg_state/(len(Mobile_after_data))
        print('平均访问时长为：', All_Avg_state)
        Excel_state.append(All_Avg_state)
    except:
        print('All_Avg_state为:0')
        Excel_state.append(All_Avg_state)

def ALl_data():
    # 输出累加总数
    print('总访客数为：')
    for i in range(len(Excel_fanke)):
        print(Excel_fanke[i])

    print('跳出率为：')
    for i in range(len(Excel_outrate)):
        print(Excel_outrate[i])

    print('总访问时长为：')
    for i in range(len(Excel_state)):
        print(Excel_state[i])



if __name__ == '__main__':
    # pass
    # https = input ("请输入您要查询的链接：")
    # data(https)

    # 统计成列表
    Excel_fanke = []
    Excel_outrate = []
    Excel_state = []

    for i in PC_Need_url:
        https = i
        print(https)
        # PC_data(https)
        Mobile_data(https)

    ALl_data()

