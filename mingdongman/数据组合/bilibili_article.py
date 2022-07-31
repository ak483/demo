# -*- codeing = utf-8 -*-
# @Time :2022/7/29 22:04
# @Author:Eric
# @File : bilibili_article.py
# @Software: PyCharm
import pandas as pd
import re

FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\BiLiBiLi\one',
    'B站专栏图下载': r'G:\Selenium_UserData\BiLiBiLi\one\image',
    '发布窗口': '',
    '编辑器': '',
    '半自动洗稿项目': r'C:\Users\ASUS\Desktop\excel表\半自动洗稿项目-B站2.xlsx',
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

mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['半自动洗稿项目'], sheet_name=[
            '第三批', '标题模板（通用）2', '首段模板（名动漫小站）2', '中间模板（名动漫小站）2', '尾段模板（名动漫小站）2'
        ],keep_default_na=False
    )

mainExcelData = mainExcelDict['第三批']
titleExcelData = mainExcelDict['标题模板（通用）2']
firstParagraphExcelDataList = (mainExcelDict['首段模板（名动漫小站）2'])['模板'].to_list()#提取所有模板内容，转化为列表
middleSectionExcelDataList = (mainExcelDict['中间模板（名动漫小站）2'])['模板'].to_list()
tailSectionExcelDataList = (mainExcelDict['尾段模板（名动漫小站）2'])['模板'].to_list()

mainExcelData = mainExcelData[(mainExcelData['发布状态'] != '已发布')]

keyList = mainExcelData['知识点'].to_list()
keyCategoryList = mainExcelData['知识点种类'].to_list()
articleContentList = mainExcelData['文章内容'].to_list()
articleClassificationNameList = mainExcelData['文章分类（名动漫小站）'].to_list()
pictureClassificationList = mainExcelData['配图分类'].to_list()

customizeCourseList = ['' for i in articleContentList]

# print(mainExcelData)
# print(titleExcelData)
# print(firstParagraphExcelDataList)
print(articleContentList)
print(customizeCourseList)
print(titleExcelData)

dataSetList = []
titleOneList = []


keywordsClassificationName = '东西'

for _, k in j.iterrows():
#标题
#定位到对应的标题分类列表，并将该列的‘{知识点\}’替换成对应的知识点
#筛选出与这篇文章核心内容相同的的文章，将该标题与筛选出的文章的标题进行对比，如果标题相同，则更换标题，如果标题不同，则保留。

#如果



#首段
#定位到对应的首段模板列表。
#筛选出与这篇文章核心内容相同的的文章，将该首段与筛选出的文章的首段进行对比，如果首段相同，则更换首段，如果首段不同，则保留。

#尾段
#定位到对应的尾段模板列表。
#筛选出与这篇文章核心内容相同的的文章，将该尾段与筛选出的文章的尾段进行对比，如果尾段相同，则更换尾段，如果尾段不同，则保留。

#中段
#定位到对应的中段模板列表。
#筛选出与这篇文章核心内容相同的的文章，将该中段段与筛选出的文章的中段进行对比，如果中段段相同，则更换中段，如果中段不同，则保留。

#配图：核心内容小于三段只添加配图1，核心内容大于三段首段后配图一，核心内容尾段前配图二

    if keywordsClassificationName == '东西':
        if str(k[2]) == 'nan':
            continue
        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[2])))

    elif keywordsClassificationName == '知识':
        if str(k[3]) == 'nan':
            continue
        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[3])))

