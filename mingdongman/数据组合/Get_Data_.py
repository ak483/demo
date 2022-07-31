# -*- codeing = utf-8 -*-
# @Time :2022/7/31 19:08
# @Author:Eric
# @File : Get_Data_.py
# @Software: PyCharm
import re, logging, random, html, time
import pymysql
import pandas as pd

mySQL = pymysql.connect(host='182.61.132.25', port=3306, user='python_test', password='pzkZW4SLhbARLKW4',database='python_test', charset='utf8')
myCursor = mySQL.cursor()

def Description(htmlStr: str) -> str:
    """
    1、内容摘要

    :param htmlStr: 正文内容
    :return: 内容摘要
    """

    # 解析 HTML 代码
    soup = etree.HTML(htmlStr)
    textStr = soup.xpath('//text()')
    # 清洗
    textStr = ''.join(textStr)
    textStr = textStr.replace('\n', '')
    textStr = textStr.replace('\t', '')
    textStr = textStr.replace('\r', '')
    textStr = textStr.replace(' ', '')
    textStr = textStr.replace('　', '')
    textStr = textStr.replace('&nbsp;', '')
    textStr = textStr.replace('&emsp;', '')
    textStr = textStr.replace(' ', '')
    textStr = textStr.replace('\u2003', '')
    # 内容摘要
    description = textStr[:72]

    return description


def Title_Deduplication(titleOneList: list, titleTwoList: list, mod: str, content: str) -> (str, str):
    """
    1、标题模板去重

    2、同核心内容下的同短标题（双1）重新随机

    :param titleOneList: 标题1列表
    :param titleTwoList: 标题2列表
    :param mod: 平台
    :param content: 核心内容
    :return: 文章标题，短标题
    """

    # 本地数据库
    mySQL = pymysql.connect(host='182.61.132.25', port=3306, user='python_test', password='pzkZW4SLhbARLKW4',database='python_test', charset='utf8')
    myCursor = mySQL.cursor()

    # 转义
    content = html.escape(content)
    # 查询使用该核心内容的短标题
    myCursor.execute(
        f"select shorttitle from article_platform where content='{content}'"
    )
    try:
        # 数据库中的短标题
        shorttitleSQL = myCursor.fetchall()
        if len(shorttitleSQL) == 0:
            raise IndexError
        shorttitleList = []
        for i in shorttitleSQL:
            shorttitleList.append(i[0])
    except IndexError:
        # 短标题
        shortTitle = random.choice(titleOneList)
        # 文章标题
        if len(titleTwoList) == 0:
            # 没有双2直接用双1
            newTitle = shortTitle
        else:
            if shortTitle[-1] not in ['！', '？', '。']:
                # 短标题无符号补，
                newTitle = f'{shortTitle}，{random.choice(titleTwoList)}'
            else:
                newTitle = f'{shortTitle}{random.choice(titleTwoList)}'

        return newTitle, shortTitle

    while True:
        # 短标题
        shortTitle = random.choice(titleOneList)
        # 文章标题
        if len(titleTwoList) == 0:
            # 没有双2直接用双1
            newTitle = shortTitle
        else:
            if shortTitle[-1] not in ['！', '？', '。']:
                # 短标题无符号补，
                newTitle = f'{shortTitle}，{random.choice(titleTwoList)}'
            else:
                newTitle = f'{shortTitle}{random.choice(titleTwoList)}'
        # 同内容同短标题则重新随机
        if shortTitle in shorttitleList:
            continue
        else:
            break

    mySQL.close()

    return newTitle, shortTitle


def Paragraph_Deduplication(paragraphList: list, content: str, mod: str) -> str:
    """
    1、段落模板去重

    2、同核心内容同平台下的段落模板重新随机

    :param paragraphList: 段落模板列表
    :param content: 核心内容
    :param mod: 平台
    :return: 段落模板
    """

    # 本地数据库
    mySQL = pymysql.connect(host='182.61.132.25', port=3306, user='python_test', password='pzkZW4SLhbARLKW4',database='python_test', charset='utf8')
    myCursor = mySQL.cursor()

    # 转义
    content = html.escape(content)
    # 查询使用该核心内容的段落模板
    myCursor.execute(
        f"select firstparagraph,middlesection,tailsection from article_platform where content='{content}'"
    )
    try:
        # 数据库中的段落模板
        contentSQL = myCursor.fetchall()
        if len(contentSQL) == 0:
            raise IndexError
        contentList = []
        for i in contentSQL:
            contentList.append(''.join(i))
        # 数据库中的段落模板
        contentSQLStr = ''.join(contentList)
    except IndexError:
        # 随机模板
        return random.choice(paragraphList)

    while True:
        # 随机模板
        paragraphText = random.choice(paragraphList)
        # 重新选择
        if paragraphText in contentSQLStr:
            continue
        else:
            break

    mySQL.close()

    return paragraphText


def Data_Format(
        mod: str, MAXINDEX: int, FILE_PATH_DICT: dict, keyList: list, keyCategoryList: list, articleContentList: list, articleClassificationNameList: list,
        pictureClassificationList: list, titleExcelData: pd.DataFrame,
        firstParagraphExcelDataList: list, middleSectionExcelDataList: list, tailSectionExcelDataList: list,
        customizeCourseList: list, customizeTitleList: list, customizeTitleList_: list, timeDateList: list
) -> [{}, {}] or bool:


    dataSetList = []
    for item in range(len(articleContentList)):
        if len(dataSetList) >= MAXINDEX:
            break

        # 核心内容
        content = articleContentList[item]
        # 删除无关词语
        for removeKey in ['图源网络']:
            content = re.sub(removeKey, '', content)
        # 关键词
        keywords = re.sub('，', ',', keyList[item])
        # 关键词分类
        keywordsClassificationName = str(keyCategoryList[item])
        # 配图分类
        contentClassificationName = str(pictureClassificationList[item])
        # 名动漫官网课程ID
        mdmCourseIdInt = customizeCourseList[item]
        # 文章分类
        if mod == '名动漫小站' or mod == '名动漫小站-名动漫' or mod == '搜狐' or mod == 'B站' or mod == '名动漫小站-摸鱼' or mod == '知乎' or mod == '网易号':
            articleClassificationName = str(articleClassificationNameList[item])
        elif mod == '画师巴士' or mod == '画师巴士-摸鱼':
            articleClassificationName = str(articleClassificationNameList[item])
            # 核心内容修改品牌词
            content = re.sub('名动漫', '画师巴士', content)
        elif mod == '画帮帮':
            # 核心内容修改品牌词
            content = re.sub('名动漫', '画帮帮', content)
            articleClassificationName = str(articleClassificationNameList[item])
        else:
            logging.info(f'输入的平台不正确：{mod}')
            return False

        ## 组合标题
        # 双1，双2
        titleOneList, titleTwoList = [], []
        # 分组
        for i, j in titleExcelData.groupby(['位置']):
            for _, k in j.iterrows():
                if i == '双1':
                    if keywordsClassificationName == '东西':
                        if str(k[2]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[2])))

                    elif keywordsClassificationName == '知识':
                        if str(k[3]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[3])))

                    elif keywordsClassificationName == '自学':
                        if str(k[4]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[4])))

                    elif keywordsClassificationName == '对比':
                        if str(k[5]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[5])))

                    elif keywordsClassificationName == '职位':
                        if str(k[6]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[6])))

                    elif keywordsClassificationName == '机构':
                        if str(k[7]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[7])))

                    elif keywordsClassificationName == '专业':
                        if str(k[8]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[8])))

                    elif keywordsClassificationName == '就业':
                        if str(k[9]) == 'nan':
                            continue
                        titleOneList.append(re.sub('\{知识点\}', keywords, str(k[9])))
                    else:
                        logging.info(f'无该关键词分类：{keywordsClassificationName}')
                        continue
                elif i == '双2':
                    if keywordsClassificationName == '东西':
                        if str(k[2]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[2])))

                    elif keywordsClassificationName == '知识':
                        if str(k[3]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[3])))

                    elif keywordsClassificationName == '自学':
                        if str(k[4]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[4])))

                    elif keywordsClassificationName == '对比':
                        if str(k[5]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[5])))

                    elif keywordsClassificationName == '职位':
                        if str(k[6]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[6])))

                    elif keywordsClassificationName == '机构':
                        if str(k[7]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[7])))

                    elif keywordsClassificationName == '专业':
                        if str(k[8]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[8])))

                    elif keywordsClassificationName == '就业':
                        if str(k[9]) == 'nan':
                            continue
                        titleTwoList.append(re.sub('\{知识点\}', keywords, str(k[9])))
                    else:
                        logging.info(f'无该关键词分类：{keywordsClassificationName}')
                        continue
                else:
                    logging.info(f'无该位置：{i}')
                    continue

        # 文章标题，短标题
        if customizeTitleList[item] == '':
            newTitle, shortTitle = Title_Deduplication(titleOneList=titleOneList, titleTwoList=titleTwoList, mod=mod, content=content)
        else:
            newTitle, shortTitle = customizeTitleList[item], customizeTitleList_[item]
        # 保留未去符号的短标题
        shortTitle_ = shortTitle
        # 短标题去符号
        if shortTitle[-1] in ['！', '？', '。', '，']:
            shortTitle = shortTitle[:-1]
        # 首段，尾段标题
        if newTitle[-1] not in ['！', '？', '。', '，']:
            # 首段保持无符号
            newFirstTitle = newTitle
            # 尾段保持无符号
            newTailSectionTitle = newTitle
        else:
            # 首段去符号
            newFirstTitle = newTitle[:-1]
            # 尾段去符号
            newTailSectionTitle = newTitle[:-1]

        ## 组合正文
        # 首段
        a = re.sub('\{标题\}', newFirstTitle, Paragraph_Deduplication(paragraphList=firstParagraphExcelDataList, content=content, mod=mod))
        # 防止首段末尾没有句号
        if a[-1] == '，':
            a = list(a)
            a.append('。')
            a = ''.join(a)
        firstParagraph = f'<p>&nbsp; &nbsp; &nbsp; &nbsp; {a}</p><br />'
        # 去掉不应该存在的符号
        if '，。' in firstParagraph:
            newFirstTitle = newFirstTitle.rstrip('，')
            firstParagraph = firstParagraph.replace('，。', '。', 1)
        if '，，' in firstParagraph:
            newFirstTitle = newFirstTitle.rstrip('，')
            firstParagraph = firstParagraph.replace('，，', '，', 1)
        if '！。' in firstParagraph:
            newFirstTitle = newFirstTitle.rstrip('！')
            firstParagraph = firstParagraph.replace('！。', '。', 1)
        if '？。' in firstParagraph:
            newFirstTitle = newFirstTitle.rstrip('？')
            firstParagraph = firstParagraph.replace('？。', '。', 1)
        if '！，' in firstParagraph:
            newFirstTitle = newFirstTitle.rstrip('！')
            firstParagraph = firstParagraph.replace('！，', '，', 1)
        if '？，' in firstParagraph:
            newFirstTitle = newFirstTitle.rstrip('？')
            firstParagraph = firstParagraph.replace('？，', '，', 1)
        # 中段
        a = re.sub('\{标题\}', newTitle, Paragraph_Deduplication(paragraphList=middleSectionExcelDataList, content=content, mod=mod))
        middleSection = f'<p>&nbsp; &nbsp; &nbsp; &nbsp; {a}</p><br />'
        # 尾段
        a = re.sub('\{标题\}', newTailSectionTitle, Paragraph_Deduplication(paragraphList=tailSectionExcelDataList, content=content, mod=mod))
        tailSection = f'<p>&nbsp; &nbsp; &nbsp; &nbsp; {a}</p><br />'
        # 配图1，配图2
        a, b = random.sample([i for i in range(0, 100)], 2)
        # 检查配图分类正不正确
        try:
            FILE_PATH_DICT['配图'][contentClassificationName]
        except KeyError:
            logging.info(f'配图分类不存在：{contentClassificationName}')
            continue
        contentImageUrlList = [
            rf'<div style="text-align:center;"><img src="{FILE_PATH_DICT["配图"][contentClassificationName]}/{a}.jpg" alt="" /></div><br />',
            rf'<div style="text-align:center;"><img src="{FILE_PATH_DICT["配图"][contentClassificationName]}/{b}.jpg" alt="" /></div><br />',
        ]
        # 封面图
        coverImageUrl = rf"{FILE_PATH_DICT['配图封面'][contentClassificationName]}/{a}.jpg"
        # 段落列表
        contentList = []
        for i in content.split('\n'):
            if i == '':
                continue
            contentList.append(f'<p>&nbsp; &nbsp; &nbsp; &nbsp; {i}</p><br />')
        # 段落数目
        contentIndex = len(contentList)
        # 插配图
        if contentIndex >= 3:
            # 配图1位置：核心内容首段下方
            contentList.insert(1, contentImageUrlList[0])
            # 配图2位置：核心内容尾段上方
            contentList.insert(contentIndex, contentImageUrlList[1])
        elif contentIndex == 2:
            contentList.insert(1, contentImageUrlList[0])
        elif contentIndex == 1:
            contentList.append(contentImageUrlList[0])
        else:
            logging.info(f'配图插入失败：正文长度不正确')
            continue
        # 插入首段
        contentList.insert(0, firstParagraph)
        # 段落数目
        contentIndex = len(contentList)
        # 插入中段
        if contentIndex - 2 < 3:
            # 核心内容小于3则直接把中段加到尾部
            contentList.append(middleSection)
        else:
            a = random.sample([i for i in range(2, contentIndex - 2)], 1)[0]
            if 'img src=' in contentList[a]:
                a += 1
            contentList.insert(a, middleSection)
        # 插入尾段
        contentList.append(tailSection)

        # 发布日期
        try:
            timeDate = int(time.mktime(time.strptime(str(timeDateList[item]), '%Y/%m/%d %H:%M'))) if timeDateList[item] != '' else ''
        except Exception:
            timeDate = ''

        dataSetList.append({
            # 文章标题
            'articleTitle': newTitle,
            # 短标题
            'articleShortTitle': shortTitle,
            # 短标题未去除末尾符号（用于双1去重）
            'shortTitle': shortTitle_,
            # 文章分类
            'articleClassificationName': articleClassificationName,
            # 关键词
            'keywordsStr': keywords,
            # 标签
            'labelStr': keywords,
            # 正文内容
            'content': ''.join(contentList),
            # 核心内容
            'content_': content,
            # 内容摘要
            'descriptionStr': Description(''.join(contentList)),
            # 封面图
            'coverImageUrl': coverImageUrl,
            # 配图分类
            'pictureClassification': contentClassificationName,
            # 首段模板
            'firstParagraph': re.sub(
                '<p>&nbsp; &nbsp; &nbsp; &nbsp; ', '', re.sub(
                    '</p><br />', '', re.sub(newFirstTitle, '{标题}', firstParagraph))),
            # 中段模板
            'middleSection': re.sub(
                '<p>&nbsp; &nbsp; &nbsp; &nbsp; ', '', re.sub(
                    '</p><br />', '', re.sub(newTitle, '{标题}', middleSection))),
            # 尾段模板
            'tailSection': re.sub(
                '<p>&nbsp; &nbsp; &nbsp; &nbsp; ', '', re.sub(
                    '</p><br />', '', re.sub(newTailSectionTitle, '{标题}', tailSection))),
            # 名动漫官网课程ID
            'mdmCourseIdInt': mdmCourseIdInt,
            # 发布日期
            'timeDate': timeDate,
        })

    return dataSetList
