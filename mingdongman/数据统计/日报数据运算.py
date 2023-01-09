# coding=utf-8
import os, time, sys, shutil, logging, re, random,xlwt
import pandas as pd
from lxml import etree

FILE_PATH_DICT = {

    '平台统计': r'D:\untitled1\Excel\短视频数据统计-20221206.xlsx',
    '平台统计1': r'D:\untitled1\Excel\短视频数据统计-20221207.xlsx',
}

savepath = r'D:\untitled1\demo\Excel杂货间\新增数据221207.xlsx'
def save():#保存短视频数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('短视频数据', cell_overwrite_ok=True)
    # col = ("数据日期", "视频标题", "所属账号", "所属平台", "发布日期", "播放量（增）", "点赞量（增）", "评论量（增）",  "转发量（增）", "视频带粉数（增）")
    col = ("数据日期", "视频标题", "所属账号", "所属平台", "发布日期", "发布天数", "播放量（增）", "完播率", "平均播放时长(s)", "点赞量（增）", "点赞率（点赞/播放）", "评论量（增）", "评论率（评论/播放）", "转发量（增）", "转发率（准发/播放）", "视频带粉数（增）")
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条视频" % (i + 1))
        data = All_datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

#前一天的数据
mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['平台统计'], sheet_name=[
            '短视频数据'
        ]
    )
mainExcelData = mainExcelDict['短视频数据']
statisticsDate = mainExcelData['数据日期'].to_list()
title = mainExcelData['视频标题'].to_list()
account = mainExcelData['所属账号'].to_list()
platform = mainExcelData['所属平台'].to_list()
publishDate = mainExcelData['发布日期'].to_list()
playVolume = mainExcelData['播放量（总）'].to_list()
completionRate = mainExcelData['完播率'].to_list()
# for i in range(len(completionRate)):
#     if pd.isnull(completionRate[i]):
#         completionRate[i]=completionRate[i]
    # else:
    #     completionRate[i]=re.sub('%', '', str(completionRate[i]))

averagePlayTime = mainExcelData['平均播放时长(s)'].to_list()
likes = mainExcelData['点赞量（总）'].to_list()
commentVolume = mainExcelData['评论量（总）'].to_list()
forwardVolume = mainExcelData['转发量（总）'].to_list()
fansVolume = mainExcelData['视频带粉数（总）'].to_list()


#今天的数据
mainExcelDict1 = pd.read_excel(
        FILE_PATH_DICT['平台统计1'], sheet_name=[
            '短视频数据'
        ]
    )
mainExcelData1 = mainExcelDict1['短视频数据']

#账号数据
statisticsDate1 = mainExcelData1['数据日期'].to_list()
title1 = mainExcelData1['视频标题'].to_list()
account1 = mainExcelData1['所属账号'].to_list()
platform1 = mainExcelData1['所属平台'].to_list()
publishDate1 = mainExcelData1['发布日期'].to_list()
playVolume1 = mainExcelData1['播放量（总）'].to_list()
completionRate1 = mainExcelData1['完播率'].to_list()
# for i in range(len(completionRate1)):
#     if pd.isnull(completionRate1[i]):
#         completionRate1[i]=completionRate1[i]
#     else:
#         completionRate1[i]=re.sub('%', '', str(completionRate1[i]))
averagePlayTime1 = mainExcelData1['平均播放时长(s)'].to_list()
likes1 = mainExcelData1['点赞量（总）'].to_list()
commentVolume1 = mainExcelData1['评论量（总）'].to_list()
forwardVolume1 = mainExcelData1['转发量（总）'].to_list()
fansVolume1 = mainExcelData1['视频带粉数（总）'].to_list()


All_datalist = []
for i in range(len(title1)):
    for j in range(len(title)):#遍历前一天所有的数据
        if title1[i] ==title[j] and account1[i] ==account[j] and platform1[i] ==platform[j]:
            datalist = []

            # 新增播放
            newplay = playVolume1[i] - playVolume[j]
            # 新增点赞
            newlike = likes1[i] - likes[j]
            # 新增评论
            newcomment = commentVolume1[i] - commentVolume[j]
            # 新增转发
            if pd.isnull(forwardVolume1[i]):#如果为空赋空值
                newforward = ''
                newforward_rate = ''  # 转发率
            else:
                newforward = forwardVolume1[i] - forwardVolume[j]

                if newplay == 0:
                    newforward_rate = 0
                else:
                    newforward_rate = newforward / newplay  # 转发率

            #判断播放
            if newplay == 0:
                newlike_rate = 0  # 点赞率
                newcomment_rate = 0#评论率
                # newforward_rate = 0#转发率
            else:
                newlike_rate = newlike / newplay  # 点赞率
                newcomment_rate = newcomment / newplay  # 评论率

            # 新增带粉
            if pd.isnull(fansVolume1[i]):
                newfan = ''
            elif pd.isnull(fansVolume[j]):
                newfan = fansVolume1[i]
            else:
                newfan = fansVolume1[i] - fansVolume[j]

                print(i)
            datalist.append(statisticsDate1[i])
            datalist.append(title1[i])
            datalist.append(account1[i])
            datalist.append(platform1[i])
            datalist.append(publishDate1[i])
            datalist.append('')#发布天数
            datalist.append(newplay)
            if pd.isnull(completionRate1[i]):#完播率
                datalist.append('')
            else:
                datalist.append(completionRate1[i])
            if pd.isnull(averagePlayTime1[i]):#平均播放时长
                datalist.append('')
            else:
                datalist.append(averagePlayTime1[i])
            datalist.append(newlike)#新增点赞
            datalist.append(newlike_rate)#点赞率
            datalist.append(newcomment)#新增评论
            datalist.append(newcomment_rate)
            datalist.append(newforward)
            datalist.append(newforward_rate)
            datalist.append(newfan)#带粉数
            All_datalist.append(datalist)
            break#找到相同值入列后则推出


        elif j == len(title)-1:#如果遍历完所有还没找到的画则只添加自己的值
            datalist = []

            if pd.isnull(forwardVolume1[i]):  # 如果转发为空赋空值
                newforward = ''
                newforward_rate = ''  # 转发率
            else:
                newforward = forwardVolume1[i] #如果不为空则赋原值

                if playVolume1[i] == 0:#如果播放为0
                    newforward_rate = 0
                else:
                    newforward_rate = newforward / playVolume1[i]  # 转发率

            # 判断播放
            if playVolume1[i] == 0:#如果播放为空，赋0
                newlike_rate = 0  # 点赞率
                newcomment_rate = 0  # 评论率
            else:
                newlike_rate = likes1[i] / playVolume1[i]  # 点赞率
                newcomment_rate = commentVolume1[i] / playVolume1[i] # 评论率


            # 新增带粉
            if pd.isnull(fansVolume1[i]):
                newfan = ''
            elif pd.isnull(fansVolume[j]):
                 newfan = fansVolume1[i]
            else:
                newfan = fansVolume1[i] - fansVolume[j]

            datalist.append(statisticsDate1[i])
            datalist.append(title1[i])
            datalist.append(account1[i])
            datalist.append(platform1[i])
            datalist.append(publishDate1[i])
            datalist.append('')#发布天数
            datalist.append(playVolume1[i])#播放量
            if pd.isnull(completionRate1[i]): #完播率
                datalist.append('')
            else:
                datalist.append(completionRate1[i])

            if pd.isnull(averagePlayTime1[i]):  # 平均播放时长
                datalist.append('')
            else:
                datalist.append(averagePlayTime1[i])

            datalist.append(likes1[i])#点赞
            datalist.append(newlike_rate)#点赞率
            datalist.append(commentVolume1[i])#评论
            datalist.append(newcomment_rate)#评论率
            datalist.append(newforward)#转发
            datalist.append(newforward_rate)#转发率
            datalist.append(newfan)#带粉数
            All_datalist.append(datalist)

print(All_datalist)
save()
