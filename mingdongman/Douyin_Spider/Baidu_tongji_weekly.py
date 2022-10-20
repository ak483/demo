import pandas as pd
import xlwt,re

mainExcelDict=pd.DataFrame=pd.read_excel(r'C:\Users\Adminitrator03\Desktop\test.xlsx',sheet_name=[
        '42周客服数据','目标1','42周百度统计'
    ])

PC_URL_ExcelDataList = (mainExcelDict['42周客服数据'])['着陆页面'].to_list()
PC_count_ExcelDataList = (mainExcelDict['42周客服数据'])['接通人数'].to_list()
PC_customer_ExcelDataList = (mainExcelDict['42周客服数据'])['入库客户数'].to_list()
PC_count_rate_ExcelDataList = (mainExcelDict['42周客服数据'])['咨询率'].to_list()
Target_URL_ExcelDataList = (mainExcelDict['目标1'])['目标url1'].to_list()
Baidu_fanke_ExcelDataList = (mainExcelDict['42周百度统计'])['访客数(UV)'].to_list()
Baidu_URL_ExcelDataList = (mainExcelDict['42周百度统计'])['页面URL'].to_list()
Baidu_Avg_state_ExcelDataList = (mainExcelDict['42周百度统计'])['平均停留时长（秒）'].to_list()
Baidu_Out_rate_ExcelDatalist = (mainExcelDict['42周百度统计'])['退出率'].to_list()

def PC_data(https):
#整合数据列到一个列表
    PC_All_list=[]
    for i in range(len(PC_URL_ExcelDataList)):
        PClist = []
        PClist.append(PC_URL_ExcelDataList[i])
        PClist.append(PC_count_ExcelDataList[i])
        PClist.append(PC_customer_ExcelDataList[i])
        PClist.append(PC_count_rate_ExcelDataList[i])
        PC_All_list.append(PClist)

#接收查询url的列表
    PC_after_data=[]
    for l in range(len(PC_All_list)):
        if ( https == 'https://www.mingdongman.com/'==str(PC_All_list[l][0]) ):
            PC_after_data.append(PC_All_list[l])
            break
        elif ( https == 'https://www.huashibus.com/'==str(PC_All_list[l][0]) ):
            PC_after_data.append(PC_All_list[l])
            break
        elif ( https == 'https://www.meatoo.com/'==str(PC_All_list[l][0]) ):
            PC_after_data.append(PC_All_list[l])
            break
        elif ( https in str(PC_All_list[l][0]) ):
            PC_after_data.append(PC_All_list[l])

#百度统计板块
    Baidu_All_list=[]
    for i in range(len(Baidu_URL_ExcelDataList)):
        Baidulist = []
        Baidulist.append(Baidu_URL_ExcelDataList[i])
        Baidulist.append(Baidu_fanke_ExcelDataList[i])
        Baidulist.append(Baidu_Avg_state_ExcelDataList[i])
        Baidulist.append(Baidu_Out_rate_ExcelDatalist[i])
        Baidu_All_list.append(Baidulist)

    Baidu_after_data = []
    for l in range(len(Baidu_All_list)):
        if (https == 'https://www.mingdongman.com/' == str(Baidu_All_list[l][0])):#如果这三个链接完全一致，则直接拿取数据
            Baidu_after_data.append(Baidu_All_list[l])
            break
        elif (https == 'https://www.huashibus.com/' == str(Baidu_All_list[l][0])):
            Baidu_after_data.append(Baidu_All_list[l])
            break
        elif (https == 'https://www.meatoo.com/' == str(Baidu_All_list[l][0])):
            Baidu_after_data.append(Baidu_All_list[l])
            break
        elif (https in str(Baidu_All_list[l][0])):#筛选包含的url
            Baidu_after_data.append(Baidu_All_list[l])


    if len(Baidu_after_data)!=0:#如果查询的url不为空，继续进行后续运算
        Baidu_All_Sum_fanke = 0
        Baidu_All_Avg_time = 0
        Baidu_All_Out_rate = 0

#提取和清洗
        for i in range(len(Baidu_after_data)):
            Baidu_count_fanke = Baidu_after_data[i][1]
            Baidu_Avg_time = Baidu_after_data[i][2]
            Baidu_Out_rate = Baidu_after_data[i][3]

#执行累加
            Baidu_All_Sum_fanke = Baidu_count_fanke + Baidu_All_Sum_fanke  #访客数
            Baidu_All_Avg_time = Baidu_Avg_time + Baidu_All_Avg_time
            if Baidu_Out_rate == '--':
                Baidu_Out_rate = 0
            Baidu_All_Out_rate = Baidu_Out_rate + Baidu_All_Out_rate
        Baidu_All_Avg_time = Baidu_All_Avg_time/len(Baidu_after_data) #平均访问时长
        Baidu_All_Out_rate = Baidu_All_Out_rate / len(Baidu_after_data)
    else :#如果为空，赋值为0
        Baidu_All_Sum_fanke = 0
        Baidu_All_Avg_time = 0
        Baidu_All_Out_rate = 0



#计算列中元素，判断客服表数据是否为空
    if len(PC_after_data)!=0:
        All_Sum_fanke = 0
        All_Avg_outrate = 0
        All_Avg_state = 0
        Excel_ALl = []

#提取和清洗
        for i in range(len(PC_after_data)):
            count_fanke = PC_after_data[i][1]
            customer = PC_after_data[i][2]
            count_rate = float(re.sub('%','',PC_after_data[i][3]))
#执行累加
            All_Sum_fanke = count_fanke + All_Sum_fanke  #接通
            All_Avg_outrate = customer + All_Avg_outrate  #入库
            All_Avg_state = count_rate + All_Avg_state  #接通率
        All_Avg_state = All_Avg_state/len(PC_after_data)

        #入库
        Excel_ALl.append(https)
        Excel_ALl.append(Baidu_All_Sum_fanke)
        Excel_ALl.append(All_Sum_fanke)
        Excel_ALl.append(All_Avg_outrate)
        Excel_ALl.append('')
        Excel_ALl.append(All_Avg_state)
        Excel_ALl.append(Baidu_All_Avg_time)
        Excel_ALl.append(Baidu_All_Out_rate)

        return Excel_ALl
    else :#如果为0，返回空值
        return  [https,Baidu_All_Sum_fanke,0,0,'',0,Baidu_All_Avg_time,Baidu_All_Out_rate]



def saveData(datalists, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('百度统计', cell_overwrite_ok=True)  # 创建工作表
    col = ("着陆页面", '访客数',"接通人数", "入库客户数", '线索数',"接通率",'平均访问时长','跳出率')
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, (len(datalists))):
        print("第%d条" % (i + 1))
        data = datalists[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

if __name__ == '__main__':

    datalists = []
    for i in Target_URL_ExcelDataList:
        https = i
        print(https)
        data = PC_data(https)
        datalists.append(data)
    print(datalists)

    savepath = "百度42周统计跳出率.xls"
    # 2.保存数据
    saveData(datalists, savepath)