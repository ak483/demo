import os, time, sys, shutil, logging, re, random
import pandas as pd
from lxml import etree

# 输出到文件
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(funcName)s -> %(message)s',
                    filename=rf'.\{os.path.splitext(os.path.split(__file__)[1])[0]}.log')
# 输出到屏幕
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(funcName)s -> %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

sys.path.append(r'D:\untitled1')
# from demo.mingdongman.数据组合.MdmAPI import PlatformDataAPI
from My_code.名动漫.Mdm_API import PlatformDataAPI


dataSetList = []
def Get_Data(mod: str) -> list:
    # 读取模板
    mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['平台统计'], sheet_name=[
            '账号数据'
        ]
    )
    mainExcelData = mainExcelDict['账号数据']

    #账号数据
    statisticsDate = mainExcelData['数据日期'].to_list()
    account = mainExcelData['账号'].to_list()
    platform = mainExcelData['所属平台'].to_list()
    releaseVolume = mainExcelData['发布量'].to_list()
    playVolume = mainExcelData['播放量'].to_list()
    likes = mainExcelData['点赞量'].to_list()
    commentVolume = mainExcelData['评论量'].to_list()
    forwardVolume = mainExcelData['转发量'].to_list()
    attentionVolume = mainExcelData['关注量'].to_list()
    attentionVolumeTotal = mainExcelData['累计关注量'].to_list()

    for i in range(len(statisticsDate)):
        # if len(dataSetList) >= MAXINDEX:
        #     break

        dataSetList.append({
            'statisticsDate': statisticsDate[i],
            'account': account[i],
            'platform': platform[i],
            'releaseVolume': releaseVolume[i],
            'playVolume': playVolume[i],
            'likes': likes[i],
            'commentVolume': commentVolume[i],
            'forwardVolume': forwardVolume[i],
            'attentionVolume': attentionVolume[i],
            'attentionVolumeTotal': attentionVolumeTotal[i],
        })

    return dataSetList

#短视频数据
dataSetList1 = []
def Get_Video_Data(mod: str) -> list:
    # 读取模板
    mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['平台统计'], sheet_name=[
            '短视频数据'
        ]
    )
    mainExcelData = mainExcelDict['短视频数据']

    #账号数据
    statisticsDate = mainExcelData['数据日期'].to_list()
    title = mainExcelData['视频标题'].to_list()
    account = mainExcelData['所属账号'].to_list()
    platform = mainExcelData['所属平台'].to_list()
    publishDate = mainExcelData['发布日期'].to_list()
    playVolume = mainExcelData['播放量（总）'].to_list()
    completionRate = mainExcelData['完播率'].to_list()
    for i in range(len(completionRate)):
        if pd.isnull(completionRate[i]):
            completionRate[i]=completionRate[i]
        else:
            completionRate[i]=re.sub('%', '', str(completionRate[i]))
    averagePlayTime = mainExcelData['平均播放时长(s)'].to_list()
    likes = mainExcelData['点赞量（总）'].to_list()
    commentVolume = mainExcelData['评论量（总）'].to_list()
    forwardVolume = mainExcelData['转发量（总）'].to_list()
    fansVolume = mainExcelData['视频带粉数（总）'].to_list()

    for i in range(len(statisticsDate)):
        if pd.isnull(averagePlayTime[i]):
            averagePlayTime[i]=''
        elif pd.isnull(completionRate[i]):
            completionRate[i]=''

        dataSetList1.append({
            'statisticsDate': statisticsDate[i],
            'title':title[i],
            'account': account[i],
            'platform': platform[i],
            'publishDate': publishDate[i],
            'playVolume': playVolume[i],
            'completionRate':completionRate[i],
            'averagePlayTime':averagePlayTime[i],
            'likes': likes[i],
            'commentVolume': commentVolume[i],
            'forwardVolume': forwardVolume[i],
            'fansVolume': fansVolume[i]
        })

    return dataSetList1


def Mdm_Article_Run(articleDataList: list):

    if isinstance(articleDataList, bool):
        return True
    if len(articleDataList) == 0:
        return True

    # 实例化API
    platformDataAPI =PlatformDataAPI()
    # 发布文章
    for item in articleDataList:
        msg = platformDataAPI.Add_Count_Data(
            statisticsDate=item['statisticsDate'],account=item['account'],platform=item['platform'],
            releaseVolume=item['releaseVolume'],playVolume=item['playVolume'], likes=item['likes'],
            commentVolume=item['commentVolume'],forwardVolume=item['forwardVolume'],attentionVolume=item['attentionVolume'],
            attentionVolumeTotal=item['attentionVolumeTotal']
        )
        print(msg)
    pass

#短视频数据
def Mdm_Video_Run(articleDataList: list):

    if isinstance(articleDataList, bool):
        return True
    if len(articleDataList) == 0:
        return True

    # 实例化API
    platformDataAPI =PlatformDataAPI()
    # 发布文章
    for item in articleDataList:
        msg = platformDataAPI.Add_Video_Data(
            statisticsDate=item['statisticsDate'],title=item['title'],account=item['account'],platform=item['platform'],
            publishDate=item['publishDate'],playVolume=item['playVolume'], completionRate=item['completionRate'],averagePlayTime=item['averagePlayTime'],
            likes=item['likes'],commentVolume=item['commentVolume'],forwardVolume=item['forwardVolume'],fansVolume=item['fansVolume']
        )
        # print(msg)
    pass

FILE_PATH_DICT = {
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-名动漫官网.xlsx',
    '平台统计': r'D:\untitled1\Excel\短视频数据统计-20221013.xlsx',
    '标题保存': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\标题2.xlsx',
    '原文配图': 'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/Fifth_Batch',

}

if __name__ == '__main__':
    # 发布问答数目
    MAXINDEX = 10

    Mdm_Article_Run(Get_Data(mod='名动漫小站-名动漫-问答'))
    Mdm_Video_Run(Get_Video_Data(mod='名动漫小站-名动漫-短视频'))
    pass
