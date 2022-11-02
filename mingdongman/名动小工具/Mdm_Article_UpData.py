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
from My_code.名动漫.Mdm_API import ArticleClassAPI
from My_code.名动漫.Article_Published.Submit_SQL import Submit_Data
from My_code.名动漫.Article_Published.Get_Data_ import Data_Format


def Get_Data(mod: str) -> list:
    # 读取模板
    mainExcelDict = pd.read_excel(
        FILE_PATH_DICT['半自动洗稿项目'], sheet_name=[
            '第六批', '标题模板（通用）2', '首段模板（名动漫小站）2', '中间模板（名动漫小站）2', '尾段模板（名动漫小站）2'
        ]
    )
    mainExcelData = mainExcelDict['第六批']
    titleExcelData = mainExcelDict['标题模板（通用）2']
    firstParagraphExcelDataList = (mainExcelDict['首段模板（名动漫小站）2'])['模板'].to_list()
    middleSectionExcelDataList = (mainExcelDict['中间模板（名动漫小站）2'])['模板'].to_list()
    tailSectionExcelDataList = (mainExcelDict['尾段模板（名动漫小站）2'])['模板'].to_list()

    # 筛选
    mainExcelData = mainExcelData[(mainExcelData['发布状态'] != '已发布')]

    keyList = mainExcelData['知识点'].to_list()
    keyCategoryList = mainExcelData['知识点种类'].to_list()
    articleContentList = mainExcelData['文章内容'].to_list()
    articleClassificationNameList = mainExcelData['文章分类（名动漫）'].to_list()
    pictureClassificationList = mainExcelData['配图分类'].to_list()
    # 自定义课程
    customizeCourseList = mainExcelData['推荐课程ID'].to_list()
    # 自定义标题
    customizeTitleList = ['' for i in articleContentList]
    # customizeTitleList = mainExcelData['原标题'].to_list()
    # 自定义短标题
    customizeTitleList_ = ['' for i in articleContentList]
    # 自定义发布日期
    timeDateList = ['' for i in articleContentList]
    # timeDateList = mainExcelData['发布日期'].to_list()

    return Data_Format(
        mod=mod, MAXINDEX=MAXINDEX, FILE_PATH_DICT=FILE_PATH_DICT, keyList=keyList, keyCategoryList=keyCategoryList, articleContentList=articleContentList,
        articleClassificationNameList=articleClassificationNameList, pictureClassificationList=pictureClassificationList,
        titleExcelData=titleExcelData, firstParagraphExcelDataList=firstParagraphExcelDataList, middleSectionExcelDataList=middleSectionExcelDataList,
        tailSectionExcelDataList=tailSectionExcelDataList, customizeTitleList=customizeTitleList, customizeTitleList_=customizeTitleList_,
        customizeCourseList=customizeCourseList, timeDateList=timeDateList
    )


def Key_Html(articleId: int, keyStr: str, htmlStr: str):
    """
    1、关键词添加链接

    :param articleId: 添加成功的 ID
    :param keyStr: 关键词
    :param htmlStr: 格式化好的 HTML 代码
    :return: 添加好的 HTML 代码
    """

    htmlEtree = etree.HTML(htmlStr)
    htmlEtreeText = ''.join(htmlEtree.xpath('//text()'))
    # 关键词添加链接
    for key in keyStr.split(','):
        if key in htmlEtreeText:
            try:
                # 关键词有无添加链接
                keyBool = re.search(f'html">{key}</a>', htmlStr).group()
            except AttributeError:
                keyBool = False
            # 没有添加链接则添加
            if keyBool is False:
                htmlStr = htmlStr.replace(key, f'<a href="https://www.mingdongman.com/news/{int(articleId)}.html">{key}</a>', 1)

    return htmlStr


def Mdm_Article_Run(articleDataList: list):
    """
    1、发布半自动洗稿项目

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
        msg = articleClassAPI.Update_Article(
            articleTitle=item['articleTitle'], classify=item['articleClassificationName'], readingVolumeInt=random.randint(1, 50),
            originalBool=0, articleIdInt=item['articleIdInt'],
            labelList=item['labelStr'].split(','), keywordsList=item['labelStr'].split(','),
            thumbnailStr=item['coverImageUrl'], descriptionStr=item['descriptionStr'], contentStr=item['content'],
            shortTitle=item['articleShortTitle'], newsHuabshiBool=False, courseIdInt=item['mdmCourseIdInt']
        )
        if isinstance(msg, list):
            # 文章ID
            articleId = int(msg[0]['idInt'])
            logging.info(f'添加文章成功：{articleId}')
            # 添加关键词链接`
            htmlStr = Key_Html(articleId=articleId, keyStr=item['labelStr'], htmlStr=item['content'])
            # 更新内容
            msg = articleClassAPI.Update_Article(articleIdInt=articleId, contentStr=htmlStr, newsHuabshiBool=False)
            if isinstance(msg, list):
                pass
            else:
                logging.info(f'更新该文章的内容失败：{articleId} -> 原因：{msg}')

            excelTitleList.append(item['articleTitle'])
            (pd.DataFrame({'名动漫官网标题': excelTitleList})).to_excel(FILE_PATH_DICT['标题保存'], index=False)

            # 存档
            Submit_Data(
                articleid=str(articleId), platform='名动漫官网', title=item['articleTitle'], shorttitle=item['shortTitle'],
                classification=item['articleClassificationName'], keywords=item['labelStr'], coverimageurl=item['coverImageUrl'],
                pictureclassification=item['pictureClassification'], firstparagraph=item['firstParagraph'], middlesection=item['middleSection'],
                tailsection=item['tailSection'], content=item['content_']
            )
        else:
            logging.info(f"添加该文章失败：{item['articleTitle']} -> 原因：{msg}")
            excelTitleList.append('发布失败')
            (pd.DataFrame({'名动漫官网标题': excelTitleList})).to_excel(FILE_PATH_DICT['标题保存'], index=False)

        time.sleep(1)

    pass


FILE_PATH_DICT = {
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-名动漫官网.xlsx',
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
    # 发布文章数目
    MAXINDEX = 1

    Mdm_Article_Run(Get_Data(mod='名动漫小站-名动漫'))
    pass
