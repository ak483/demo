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
# from demo.mingdongman.数据组合.MdmAPI import ArticleClassAPI
from My_code.名动漫.Mdm_API import ArticleClassAPI


dataSetList = []
def Get_Data(mod: str) -> list:
    # 读取模板
    mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['问答'], sheet_name=[
            '问答2'
        ]
    )
    mainExcelData = mainExcelDict['问答2']

    # 筛选
    mainExcelData = mainExcelData[(mainExcelData['发布状态'] != '已发布')]

    titleList = mainExcelData['问题标题'].to_list()
    categoryList = mainExcelData['分类'].to_list()
#    summaryList = mainExcelData['问题标题'].to_list()
    labelList = mainExcelData['标签'].to_list()
    answerList = mainExcelData['答案1内容'].to_list()
    answerList2 = mainExcelData['答案2内容'].to_list()
    answerList3 = mainExcelData['答案3内容'].to_list()
    answerList4 = mainExcelData['答案4内容'].to_list()
    answerList5 = mainExcelData['答案5内容'].to_list()
    answerList6 = mainExcelData['答案6内容'].to_list()
    answerList7 = mainExcelData['答案7内容'].to_list()


    q= answerList4[0]

    for i in range(len(titleList)):
        if len(dataSetList) >= MAXINDEX:
            break

        if pd.isnull(answerList2[i]):
            pass
        else:
            answerList[i]=answerList[i] + ',' + answerList2[i]
        if pd.isnull(answerList3[i]):
            pass
        else:
            answerList[i]=answerList[i] + ',' + answerList3[i]
        if pd.isnull(answerList4[i]):
            pass
        else:
            answerList[i]=answerList[i] + ',' + answerList4[i]
        if pd.isnull(answerList5[i]):
            pass
        else:
            answerList[i]=answerList[i] + ',' + answerList5[i]
        if pd.isnull(answerList6[i]):
            pass
        else:
            answerList[i]=answerList[i] + ',' + answerList6[i]
        if pd.isnull(answerList7[i]):
            pass
        else:
            answerList[i]=answerList[i] + ',' + answerList7[i]


        dataSetList.append({
            'titleList': titleList[i],
            'categoryList': categoryList[i],
           # 'summaryList': summaryList[i],
            'labelList': labelList[i],
            'answerList': answerList[i],
        })

    return dataSetList


def Mdm_Article_Run(articleDataList: list):
    """
    1、发布问答项目

    :param articleDataList:
    :return:
    """

    if isinstance(articleDataList, bool):
        return True
    if len(articleDataList) == 0:
        return True

    # 实例化API
    articleClassAPI = ArticleClassAPI()

    # 标题
    excelTitleList = []
    # 发布文章
    for item in articleDataList:
        msg = articleClassAPI.Add_QuestionAndAnswer(
            title=item['titleList'],category=item['categoryList']#,summary=item['summaryList']
            ,labelList=item['labelList'],answerList=item['answerList'],publishTime=int(str(time.time())[:10])
            ,readCount=random.randint(1, 50),status=0,auditStatus=0,
        )

        # if isinstance(msg, list):
        #     print(f'已更新')
        #
        # else:
        #     print(f'更新失败')
        # # time.sleep(1)

    pass


FILE_PATH_DICT = {
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-名动漫官网.xlsx',
    '问答': r'C:\Users\Adminitrator03\Desktop\问答.xlsx',
    '标题保存': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\标题2.xlsx',
    '原文配图': 'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/Fifth_Batch',
    '配图': {
        '3D': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/3D',
        '插画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E5%BD%B1%E8%A7%86',
        '绘画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E7%BB%98%E7%94%BB',
        '漫画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E6%BC%AB%E7%94%BB',
        '素描': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E7%B4%A0%E6%8F%8F',
        '线稿': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E7%BA%BF%E7%A8%BF',
        '影视': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E5%BD%B1%E8%A7%86',
        '游戏UI': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E6%B8%B8%E6%88%8FUI',
        '原画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E5%8E%9F%E7%94%BB',
    },
    '配图封面': {
        '3D': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/3D',
        '插画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E5%BD%B1%E8%A7%86',
        '绘画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E7%BB%98%E7%94%BB',
        '漫画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E6%BC%AB%E7%94%BB',
        '素描': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E7%B4%A0%E6%8F%8F',
        '线稿': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E7%BA%BF%E7%A8%BF',
        '影视': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E5%BD%B1%E8%A7%86',
        '游戏UI': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E6%B8%B8%E6%88%8FUI',
        '原画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E5%8E%9F%E7%94%BB',
    },

}

if __name__ == '__main__':
    # 发布问答数目
    MAXINDEX = 10

    Mdm_Article_Run(Get_Data(mod='名动漫小站-名动漫-问答'))
    pass
