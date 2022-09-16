"""
名动漫API调用
"""

import requests, re, time, json, hashlib, os
from html import escape
from urllib import parse
from collections import OrderedDict

# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate ver
requests.packages.urllib3.disable_warnings()


class PublicClass:
    """
    1、画师巴士

    2、名动漫官网
    """

    def __init__(self):
        # 正式
        # self.requestsUrl = 'https://api.mingdongman.com'
        # 测试
        self.requestsUrl = 'http://new.adminapi.mingdongman.com'
        # 定义请求参数
        self.params = {
            'accessToken': '',
        }

    def __Encrypt(self, params: dict):
        """
        1、生成签名MD5

        :param params: 参数
        :return:
        """

        encrypt = hashlib.md5()
        dataStr = '5154ba123ede86c527a71ab16a4df807'
        for i in sorted(params):
            if isinstance(params[i], list):
                dataStr += f'{i}{"".join(params[i])}'
            else:
                dataStr += f'{i}{params[i]}'
        dataStr += '5154ba123ede86c527a71ab16a4df807'
        encrypt.update(dataStr.encode('utf-8'))
        return ((encrypt.hexdigest())[10:20]).upper()

    def Params(self):
        # 时间戳
        self.params['timestamp'] = int(str(time.time())[:10])
        # 签名
        self.params['sign'] = self.__Encrypt(self.params)

    def Format_Data(self, response: requests.Response, function: str) -> [{}, {}] or str:
        """
        1、JSON数据名称格式化

        :param response: 请求的数据
        :param function: 调用的函数名称
        :return: [{},{}] or [,,] or ''
        """

        # 读取为JSON
        responseJson = json.loads(response.text)

        # 请求失败
        if int(responseJson['error']) != 0:
            return responseJson['message']

        # 成功的数据 [{},{}]
        successDataList = []
        # 作品查询
        if function == 'Query_Illustration':
            # 读取
            successData = responseJson['data']
            for data in successData:
                orderedDict = OrderedDict()
                # 作品ID
                orderedDict['idInt'] = int(data['id'])
                # 作品名称
                orderedDict['nameStr'] = data['name']
                # 大图链接
                orderedDict['bigImageStr'] = data['big_image']
                # 发布时间
                orderedDict['publishTimeStr'] = data['publish_time']
                # 分类
                orderedDict['categoryStr'] = data['category']
                # 作品简介
                orderedDict['explainStr'] = data['explain']
                # 标签列表
                orderedDict['labelsList'] = data['labels']

                successDataList.append(orderedDict)
            return successDataList

        # 追加作品标签
        elif function == 'Append_Labels':
            # 读取
            successData = responseJson['data']
            successDataList.append(
                {
                    # 作品ID
                    'idInt': int(successData['worksId']),
                }
            )
            return successDataList

        # 添加文章
        elif function == 'Add_Article':
            # 读取
            successDataList.append(
                {
                    # 文章ID
                    'idInt': int(responseJson['data']['articleId']),
                    # 文章标题
                    'articleTitle': str(responseJson['data']['title']),
                }
            )
            return successDataList

            # 问答
        elif function == 'Add_Article':
            # 读取
            successDataList.append(
                {
                    # 文章ID
                    'idInt': int(responseJson['data']['articleId']),
                    # 文章标题
                    'articleTitle': str(responseJson['data']['title']),
                }
            )
            return successDataList

        # 更新文章
        elif function == 'Update_Article':
            # 读取
            successDataList.append(
                {
                    # 文章ID
                    'idInt': int(responseJson['data']['articleId']),
                }
            )
            return successDataList

        # 查询文章
        elif function == 'Query_Article':
            # 读取
            successData = responseJson['data']
            for data in successData:
                orderedDict = OrderedDict()
                # 文章ID
                orderedDict['idInt'] = int(data['id'])
                # 文章标题
                orderedDict['nameStr'] = data['title']
                # 短标题
                orderedDict['shortTitleStr'] = data['short_title']
                # 分类ID
                orderedDict['categoryInt'] = int(data['category_id'])
                # 分类名称
                orderedDict['categoryStr'] = data['category']
                # 关键词列表
                orderedDict['keywordsList'] = data['keywords']
                # 缩略图链接
                orderedDict['thumbnailStr'] = data['cover_pic']
                # 标签列表
                orderedDict['labelList'] = data['labels']
                # 文章HTML代码内容
                orderedDict['contentStr'] = data['content']
                # 文章内容摘要
                orderedDict['descriptionStr'] = data['summary']
                # 文章发布时间
                orderedDict['releaseTimeInt'] = int(time.mktime(time.strptime(data['publish_time'], '%Y-%m-%d %H:%M:%S')))

                successDataList.append(orderedDict)
            return successDataList

        # 添加资源
        elif function == 'Add_Resource':
            # 读取
            successDataList.append(
                {
                    # 资源ID
                    'idInt': int(responseJson['data']['id']),
                    # 资源标题
                    'resourceTitle': str(responseJson['data']['title']),
                }
            )
            return successDataList

        # 添加教程
        elif function == 'Add_Tutorial':
            # 读取
            successDataList.append(
                {
                    # 教程ID
                    'idInt': int(responseJson['data']['id']),
                    # 教程标题
                    'tutorialTitle': str(responseJson['data']['title']),
                }
            )
            return successDataList

        # 查询资源
        elif function == 'Query_Resource':
            # 读取
            successData = responseJson['data']
            for data in successData:
                successDataList.append(
                    {
                        # 资源ID
                        'idInt': int(data['id']),
                        # 资源标题
                        'resourceTitle': str(data['name']),
                        # 资源正文
                        'contentStr': str(data['content']),
                        # 标签列表用逗号隔开
                        'labelsStr': str(data['labels']),
                        # 关键词列表用逗号隔开
                        'keywordsStr': str(data['keywords']),
                    }
                )
            return successDataList

        # 查询教程
        elif function == 'Query_Tutorial':
            # 读取
            successData = responseJson['data']
            for data in successData:
                # 教程章节整理 [{},{}]
                chapterList = []
                for chapter in data['chapterList']:
                    chapterList.append({
                        # 章节名称
                        'chapterName': chapter['name'],
                        # 章节视频名称
                        'chapterTitle': chapter['video_name'],
                        # 章节视频网络链接
                        'chapterVideoUrl': chapter['video_url'],
                    })

                successDataList.append(
                    {
                        # 教程ID
                        'idInt': int(data['id']),
                        # 教程标题
                        'tutorialTitle': str(data['name']),
                        # 教程正文
                        'contentStr': str(data['content']),
                        # 教程章节
                        'chapterList': chapterList,
                        # 标签列表用逗号隔开
                        'labelsStr': str(data['labels']),
                        # 关键词列表用逗号隔开
                        'keywordsStr': str(data['keywords']),
                    }
                )
            return successDataList

        # 更新资源
        elif function == 'Update_Resource':
            # 读取
            successDataList.append(
                {
                    # 资源ID
                    'idInt': int(responseJson['data']['id']),
                }
            )
            return successDataList

        # 更新教程
        elif function == 'Update_Tutorial':
            # 读取
            successDataList.append(
                {
                    # 教程ID
                    'idInt': int(responseJson['data']['id']),
                }
            )
            return successDataList

        # 百科词条添加
        elif function == 'Add_Entry':
            # 读取
            successDataList.append(
                {
                    # 百科词条ID
                    'idInt': int(responseJson['data']['id']),
                    # 百科词条名称
                    'name': str(responseJson['data']['name']),
                }
            )
            return successDataList

        # 查询百科词条
        elif function == 'Query_Entry':
            # 读取
            successData = responseJson['data']
            for data in successData:
                successDataList.append(
                    {
                        # 百科词条ID
                        'idInt': int(data['id']),
                        # 百科词条分类名称
                        'classifyStr': str(data['category']),
                        # 百科词条标题
                        'entryTitle': str(data['name']),
                        # 百科词条封面链接
                        'entryCoverPicUrl': str(data['cover_pic']),
                        # 百科词条正文
                        'contentStr': str(data['content']),
                        # 标签列表用逗号隔开
                        'labelsStr': str(data['labels']),
                        # 关键词列表用逗号隔开
                        'keywordsStr': str(data['keywords']),
                        # 发布时间
                        'publishTime': str(data['publish_time']),
                    }
                )
            return successDataList

        else:
            return ''


class IllustrationWorkClassAPI(PublicClass):
    """
    1、作品
    """

    def Query(self, articleIdInt=None, arcrankInt=None, inquireIndex=None):
        """
        1、查询官网作品

        :param articleIdInt: 查询的作品ID
        :param arcrankInt: 审核状态：通过 -> 0
        :param inquireIndex: 查询作品的个数
        :return:
        """

        self.__init__()
        # 作品ID
        if not articleIdInt is None:
            self.params['articleIdInt'] = int(articleIdInt)
        # 通过状态
        if not arcrankInt is None:
            self.params['arcrankInt'] = int(arcrankInt)
        # 查询个数
        if not inquireIndex is None:
            self.params['inquireIndex'] = int(inquireIndex)

        self.Params()

        return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-works/query', params=self.params),
                                function='Query_Illustration')

    def Append_Labels(self, articleIdInt: int, labelList: list):
        """
        1、作品ID追加标签

        :param articleIdInt: 作品ID
        :param labelList: 追加的标签列表
        :return:
        """

        self.__init__()
        # 作品ID
        self.params['articleIdInt'] = int(articleIdInt)
        # 追加标签列表
        self.params['labelList'] = ','.join(labelList)

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-works/create-tag', data=self.params),
                                function='Append_Labels')


class ArticleClassAPI(PublicClass):
    """
    1、画师巴士资讯文章
    """

    def Add_Article(
            self, articleTitle: str, classify: str, readingVolumeInt: int, originalBool: int, releaseTimeInt: int,
            labelList: list, keywordsList: list, thumbnailStr: str, descriptionStr: str, contentStr: str,
            shortTitle='', newsHuabshiBool=True, likeInt=0, courseIdInt=0

    ):
        """
        1、添加画师巴士资讯文章

        :param articleTitle: 文章标题
        :param classify: 分类名称
        :param readingVolumeInt: 阅读量
        :param originalBool: 是否原创：原创 -> 1 or 非原创 -> 0
        :param releaseTimeInt: 发布时间
        :param labelList: 标签列表
        :param keywordsList: 关键词列表
        :param thumbnailStr: 缩略图链接
        :param descriptionStr: 文章摘要
        :param contentStr: 文章内容
        :param shortTitle: 短标题
        :param newsHuabshiBool: True：画师巴士 or False：名动漫官网
        :param likeInt: 猜你喜欢（画师巴士）：设置 -> 1 or 不设置 -> 0
        :param courseIdInt: 课程ID
        :return:
        """

        self.__init__()
        # 文章标题
        self.params['articleTitle'] = str(articleTitle)
        # 短标题
        if shortTitle:
            self.params['shortTitle'] = str(shortTitle)
        # 分类名称
        self.params['classify'] = str(classify)
        # 阅读量
        self.params['readingVolumeInt'] = int(readingVolumeInt)
        # 标签列表
        self.params['labelList'] = ','.join(labelList)
        # 关键字列表
        self.params['keywordsList'] = ','.join(keywordsList)
        # 原创
        self.params['originalBool'] = int(originalBool)
        # 缩略图
        self.params['thumbnailStr'] = str(thumbnailStr)
        # 文章摘要
        self.params['descriptionStr'] = str(descriptionStr)
        # 发布时间
        self.params['releaseTimeInt'] = int(releaseTimeInt)
        # 文章内容HTML
        self.params['contentStr'] = str(contentStr)
        # 猜你喜欢
        if likeInt == 1 and newsHuabshiBool:
            self.params['likeInt'] = int(likeInt)
        # 课程
        if courseIdInt != 0:
            self.params['courseIdInt'] = int(courseIdInt)

        self.Params()

        if newsHuabshiBool:
            return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-article/create', data=self.params), function='Add_Article')
        else:
            return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-news/create', data=self.params), function='Add_Article')


    def Add_QuestionAndAnswer(
            self, title: str, category: str, publishTime: str, readCount:str,
            status:int, auditStatus:int, labelList: str, answerList: str   #summary: str,

    ):
        """
        1、添加问答

        :param title: 文章标题
        :param category: 分类名称
        :param summary: 问题摘要
        :param publishTime: 发布时间
        :param readCount: 阅读量
        :param status: 显示状态，1显示 0不显示
        :param auditStatus: 审核状态，0待审核 1审核通过 2审核拒绝
        :param labelList: 标签，多个逗号隔开
        :param answerList: 设置答案，多个逗号隔开

        """

        self.__init__()
        # 文章标题
        self.params['title'] = str(title)
        # 分类名称
        self.params['category'] = str(category)
        # 问题摘要
       # self.params['summary'] = str(summary)
        # 发布时间
        self.params['publishTime'] = int(publishTime)
        # 阅读量
        self.params['readCount'] = int(readCount)
        # 显示状态，1显示 0不显示
        self.params['status'] = int(status)
        # 审核状态，0待审核 1审核通过 2审核拒绝
        self.params['auditStatus'] = int(auditStatus)
        # 标签，多个逗号隔开
        self.params['labelList'] = str(labelList)
        # 设置答案，多个逗号隔开
        self.params['answerList'] = str(answerList)

        self.Params()

        response = requests.post(self.requestsUrl + '/interface-wenda/create', data=self.params)

        responseJson = json.loads(response.text)

        print(responseJson)

        # 请求失败
        # if int(responseJson['error']) != 0:
        #     return responseJson['message']
        # else:
        #     print(responseJson)

    def Update_QuestionAndAnswer(
           # title: str, category: str, publishTime: str, readCount: str,
          #  status: int, auditStatus: int, labelList: str, answerList: str,
            self,   summary: str,questionId:int,

    ):
        """
        1、添加问答

        :param title: 文章标题
        :param category: 分类名称
        :param summary: 问题摘要
        :param publishTime: 发布时间
        :param readCount: 阅读量
        :param status: 显示状态，1显示 0不显示
        :param auditStatus: 审核状态，0待审核 1审核通过 2审核拒绝
        :param labelList: 标签，多个逗号隔开
        :param answerList: 设置答案，多个逗号隔开

        """

        self.__init__()
        # 文章标题
        self.params['questionId'] = str(questionId)
        # 分类名称
        # self.params['category'] = str(category)
        # 问题摘要
        self.params['summary'] = str(summary)
        # # 发布时间
        # self.params['publishTime'] = int(publishTime)
        # # 阅读量
        # self.params['readCount'] = int(readCount)
        # # 显示状态，1显示 0不显示
        # self.params['status'] = int(status)
        # # 审核状态，0待审核 1审核通过 2审核拒绝
        # self.params['auditStatus'] = int(auditStatus)
        # # 标签，多个逗号隔开
        # self.params['labelList'] = str(labelList)
        # # 设置答案，多个逗号隔开
        # self.params['answerList'] = str(answerList)

        self.Params()

        response = requests.post(self.requestsUrl + '/interface-wenda/update', data=self.params)

        responseJson = json.loads(response.text)

        print(responseJson)

    def Query_QuestionAndAnswer(
            self,questionId:int, category: str,  status: int, auditStatus: int,inquireIndex:int
    ):
        """
        1、查询问答

        :param questionId: 文章ID
        :param category: 分类名称
        :param auditStatus: 审核状态：通过 -> 1 or 待审核 -> 0 or 不通过 -> 2
        :param status: 显示状态：显示 -> 1 or 不显示 -> 0
        :param inquireIndex: 查询个数
        :return:
        """

        self.__init__()
        # 文章ID
        if not questionId is None:
            self.params['questionId'] = int(questionId)
        # 分类名称
        if category != '':
            self.params['category'] = str(category)
        # 审核状态 -> 0：待审核 or 1：通过 or 2：不通过
        if not auditStatus is None:
            self.params['auditStatus'] = int(auditStatus)
        # 显示状态 -> 1：显示 or 0：不显示
        if not status is None:
            self.params['status'] = int(status)
        # 查询个数
        if not inquireIndex is None:
            self.params['inquireIndex'] = int(inquireIndex)

        self.Params()

        return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-news/query', params=self.params), function='Query_Article')

    def Update_Article(
            self, articleIdInt: int, articleTitle='', shortTitle='', classify='', readingVolumeInt=0,
            labelList=None, keywordsList=None, originalBool=None, thumbnailStr='',
            descriptionStr='', releaseTimeInt=0, contentStr='', arcrankInt=None, articleShowInt=None,
            newsHuabshiBool=True, likeInt=None, courseIdInt=None
    ):
        """
        1、更新画师巴士资讯文章

        :param articleIdInt: 文章ID
        :param articleTitle: 文章标题
        :param shortTitle: 短标题
        :param classify: 分类名称
        :param readingVolumeInt: 阅读量
        :param labelList: 标签列表（会覆盖原有）
        :param keywordsList: 关键字列表（会覆盖原有）
        :param originalBool: 是否原创：原创 -> 1 or 非原创 -> 0
        :param thumbnailStr: 缩略图
        :param descriptionStr: 文章摘要
        :param releaseTimeInt: 发布时间
        :param contentStr: 文章内容
        :param arcrankInt: 审核状态：通过 -> 1 or 待审核 -> 0 or 不通过 -> 2
        :param articleShowInt: 显示状态：显示 -> 1 or 不显示 -> 0
        :param newsHuabshiBool: True：画师巴士 or False：名动漫官网
        :param likeInt: 猜你喜欢（画师巴士）：设置 -> 1 or 不设置 -> 0
        :param courseIdInt: 课程ID
        :return:
        """

        self.__init__()
        # 文章ID
        self.params['articleIdInt'] = int(articleIdInt)
        # 文章标题
        if articleTitle != '':
            self.params['articleTitle'] = str(articleTitle)
        # 短标题
        if shortTitle != '':
            self.params['shortTitle'] = str(shortTitle)
        # 分类名称
        if classify != '':
            self.params['classify'] = str(classify)
        # 阅读量
        if readingVolumeInt != 0:
            self.params['readingVolumeInt'] = int(readingVolumeInt)
        # 标签列表
        if labelList is None:
            labelList = []
        if len(labelList) != 0:
            if isinstance(labelList, list):
                self.params['labelList'] = ','.join(labelList)
        # 关键字列表
        if keywordsList is None:
            keywordsList = []
        if len(keywordsList) != 0:
            if isinstance(keywordsList, list):
                self.params['keywordsList'] = ','.join(keywordsList)
        # 原创
        if not originalBool is None:
            self.params['originalBool'] = int(originalBool)
        # 缩略图
        if thumbnailStr != '':
            self.params['thumbnailStr'] = str(thumbnailStr)
        # 文章摘要
        if descriptionStr != '':
            self.params['descriptionStr'] = str(descriptionStr)
        # 发布时间
        if releaseTimeInt != 0:
            if len(str(releaseTimeInt)) == 10:
                self.params['releaseTimeInt'] = int(releaseTimeInt)
        # 文章内容
        if contentStr != '':
            self.params['contentStr'] = str(contentStr)
        # 审核状态
        if not arcrankInt is None:
            self.params['arcrankInt'] = int(arcrankInt)
        # 显示状态
        if not articleShowInt is None:
            self.params['statusInt'] = int(articleShowInt)
        # 猜你喜欢
        if not likeInt is None:
            if newsHuabshiBool:
                self.params['likeInt'] = int(likeInt)
        # 课程
        if not courseIdInt is None:
            self.params['courseIdInt'] = int(courseIdInt)

        self.Params()

        if newsHuabshiBool:
            return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-article/update', data=self.params), function='Update_Article')
        else:
            return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-news/update', data=self.params), function='Update_Article')

    def Query_Article(
            self, articleIdInt=None, classify='', originalBool=None, arcrankInt=None, articleShowInt=None,
            inquireIndex=None, newsHuabshiBool=True
    ):
        """
        1、查询画师巴士资讯文章

        :param articleIdInt: 文章ID
        :param classify: 分类名称
        :param originalBool: 是否原创：原创 -> 1 or 非原创 -> 0
        :param arcrankInt: 审核状态：通过 -> 1 or 待审核 -> 0 or 不通过 -> 2
        :param articleShowInt: 显示状态：显示 -> 1 or 不显示 -> 0
        :param inquireIndex: 查询个数
        :param newsHuabshiBool: True：画师巴士 or False：名动漫官网
        :return:
        """

        self.__init__()
        # 文章ID
        if not articleIdInt is None:
            self.params['articleIdInt'] = int(articleIdInt)
        # 分类名称
        if classify != '':
            self.params['classify'] = str(classify)
        # 原创：原创 -> 1 or 非原创 -> 0
        if not originalBool is None:
            self.params['originalBool'] = int(originalBool)
        # 审核状态 -> 0：待审核 or 1：通过 or 2：不通过
        if not arcrankInt is None:
            self.params['arcrankInt'] = int(arcrankInt)
        # 显示状态 -> 1：显示 or 0：不显示
        if not articleShowInt is None:
            self.params['statusInt'] = int(articleShowInt)
        # 查询个数
        if not inquireIndex is None:
            self.params['inquireIndex'] = int(inquireIndex)

        self.Params()

        if newsHuabshiBool:
            return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-article/query', params=self.params), function='Query_Article')
        else:
            return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-news/query', params=self.params), function='Query_Article')


class SectionClassAPI(PublicClass):
    """
    1、教程

    2、资源
    """

    def Add_Tutorial(
            self, tutorialTitle: str, classifyName: str, labelList: str, keywordsList: str, sectionShowInt: int, playInt: int, originalInt: int,
            leaderboardInt: int, chapterList: list, releaseTimeInt: int, contentStr: str, refinedInt: int, descriptionStr=''
    ):
        """
        1、添加教程到画师巴士

        :param tutorialTitle: 教程名称
        :param classifyName: 分类名称
        :param labelList: 标签名称，多个逗号隔开
        :param keywordsList: 关键词名称，多个逗号隔开
        :param sectionShowInt: 显示状态：显示 -> 1 or 不显示 -> 0
        :param playInt: 播放量
        :param originalInt: 是否原创：是 -> 1 or 否 -> 0
        :param leaderboardInt: 是否排行榜：是 -> 1 or 否 -> 0
        :param chapterList: 章节列表，json对象
        :param releaseTimeInt: 发布时间：时间戳
        :param contentStr: 教程内容
        :param refinedInt: 是否加精：是 -> 1 or 否 -> 0
        :param descriptionStr: 内容摘要
        :return:
        """

        self.__init__()
        # 教程名称
        self.params['tutorialTitle'] = str(tutorialTitle)
        # 分类
        self.params['classifyName'] = str(classifyName)
        # 标签
        self.params['labelList'] = str(labelList)
        # 关键词
        self.params['keywordsList'] = str(keywordsList)
        # 发布状态
        self.params['sectionShowInt'] = int(sectionShowInt)
        # 播放量
        self.params['playInt'] = int(playInt)
        # 是否原创
        self.params['originalInt'] = int(originalInt)
        # 是否排行榜
        self.params['leaderboardInt'] = int(leaderboardInt)
        # 是否加精
        self.params['refinedInt'] = int(refinedInt)
        # 发布时间
        self.params['releaseTimeInt'] = int(releaseTimeInt)
        # 教程内容
        self.params['contentStr'] = str(contentStr)
        # 章节 JSON
        self.params['chapterList'] = json.dumps(chapterList)
        # 内容摘要
        self.params['descriptionStr'] = descriptionStr

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-video/create', data=self.params),
                                function='Add_Tutorial')

    def Add_Resource(
            self, resourceTitle: str, networkDiskAddress: str, classifyName: str, labelList: str, keywordsList: str, sectionShowInt: int,
            downloadsInt: int, releaseTimeInt: int, contentStr: str, refinedInt: int, downloadPwd: str, descriptionStr=''
    ):
        """
        1、添加资源到画师巴士

        :param resourceTitle: 资源名称
        :param networkDiskAddress: 资源下载地址
        :param classifyName: 分类名称
        :param labelList: 标签名称，多个逗号隔开
        :param keywordsList: 关键词名称，多个逗号隔开
        :param sectionShowInt: 显示状态：显示 -> 1 or 不显示 -> 0
        :param downloadsInt: 下载量
        :param releaseTimeInt: 发布时间：时间戳
        :param contentStr: 资源内容
        :param refinedInt: 是否加精：是 -> 1 or 否 -> 0
        :param downloadPwd: 压缩包密码
        :param descriptionStr: 内容摘要
        :return:
        """

        self.__init__()
        # 资源名称
        self.params['resourceTitle'] = str(resourceTitle)
        # 资源内容
        self.params['contentStr'] = str(contentStr)
        # 分类
        self.params['classifyName'] = str(classifyName)
        # 标签
        self.params['labelList'] = str(labelList)
        # 关键词
        self.params['keywordsList'] = str(keywordsList)
        # 资源下载地址
        self.params['networkDiskAddress'] = str(networkDiskAddress)
        # 是否加精
        self.params['refinedInt'] = int(refinedInt)
        # 发布状态
        self.params['sectionShowInt'] = int(sectionShowInt)
        # 下载量
        self.params['downloadsInt'] = int(downloadsInt)
        # 发布时间
        self.params['releaseTimeInt'] = int(releaseTimeInt)
        # 资源压缩包密码
        self.params['downloadPwd'] = str(downloadPwd)
        # 内容摘要
        self.params['descriptionStr'] = descriptionStr

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-resource/create', data=self.params),
                                function='Add_Resource')

    def Query_Resource(self, resourceId: int, inquireIndex=1):
        """
        1、查询资源

        :param resourceId: 资源ID
        :param inquireIndex: 查询个数
        :return:
        """

        self.__init__()
        # 资源ID
        self.params['idInt'] = int(resourceId)
        # 查询个数
        if not inquireIndex == 1:
            self.params['inquireIndex'] = inquireIndex

        self.Params()

        return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-resource/query', params=self.params),
                                function='Query_Resource')

    def Query_Tutorial(self, tutorialId: int, inquireIndex=1):
        """
        1、查询教程

        :param tutorialId: 教程ID
        :param inquireIndex: 查询个数
        :return:
        """

        self.__init__()
        # 教程ID
        self.params['idInt'] = int(tutorialId)
        # 查询个数
        if not inquireIndex == 1:
            self.params['inquireIndex'] = inquireIndex

        self.Params()

        return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-video/query', params=self.params),
                                function='Query_Tutorial')

    def Update_Resource(
            self, resourceId: int, contentStr: str, downloadUrl='', downloadPwd='',
            labelList='', keywordsList='', descriptionStr=''
    ):
        """
        1、更新资源

        :param resourceId: 资源ID
        :param contentStr: 资源正文
        :param downloadUrl: 资源下载网络链接
        :param downloadPwd: 压缩包密码
        :param labelList: 标签名称，多个逗号隔开
        :param keywordsList: 关键词名称，多个逗号隔开
        :param descriptionStr: 内容摘要
        :return:
        """

        self.__init__()
        # 资源ID
        self.params['idInt'] = int(resourceId)
        # 正文内容
        self.params['contentStr'] = str(contentStr)
        # 资源网络地址
        if downloadUrl != '':
            self.params['downloadUrl'] = str(downloadUrl)
        # 资源压缩包密码
        if downloadPwd != '':
            self.params['downloadPwd'] = str(downloadPwd)
        # 标签
        if labelList != '':
            self.params['labelList'] = str(labelList)
        # 关键词
        if keywordsList != '':
            self.params['keywordsList'] = str(keywordsList)
        # 内容摘要
        if descriptionStr != '':
            self.params['descriptionStr'] = str(descriptionStr)

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-resource/update', data=self.params),
                                function='Update_Resource')

    def Update_Tutorial(self, tutorialId: int, contentStr: str, labelList='', keywordsList='', descriptionStr=''):
        """
        1、更新教程

        :param tutorialId: 教程ID
        :param contentStr: 教程正文
        :param labelList: 标签名称，多个逗号隔开
        :param keywordsList: 关键词名称，多个逗号隔开
        :param descriptionStr: 内容摘要
        :return:
        """

        self.__init__()
        # 教程ID
        self.params['idInt'] = int(tutorialId)
        # 正文内容
        self.params['contentStr'] = str(contentStr)
        # 标签
        if labelList != '':
            self.params['labelList'] = str(labelList)
        # 关键词
        if keywordsList != '':
            self.params['keywordsList'] = str(keywordsList)
        # 内容摘要
        if descriptionStr != '':
            self.params['descriptionStr'] = str(descriptionStr)

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-video/update', data=self.params),
                                function='Update_Tutorial')


class EntryAPI(PublicClass):
    """
    1、百科词条
    """

    def Add_Entry(
            self, entryName: str, categoryId: int,
            publishTime: int, contentStr: str, browseCount: int, labelListStr: str, keywords='',
            isHot=0, status=0, auditStatus=0, coverPic: str = ''
    ):
        """
        1、添加百科词条

        :param entryName: 百科名称
        :param categoryId: 百科分类ID
        :param coverPic: 百科封面图
        :param publishTime: 发布时间戳
        :param contentStr: HTML正文内容
        :param browseCount: 浏览量
        :param keywords: 关键字
        :param labelListStr: 标签，多个逗号隔开
        :param isHot: 是否热门：非热门 -> 0 or 热门 -> 1
        :param status: 显示状态：不显示 -> 0 or 显示 -> 1
        :param auditStatus: 审核状态：通过 -> 1 or 待审核 -> 0 or 不通过 -> 2
        :return:
        """

        self.__init__()
        # 百科名称
        self.params['entryName'] = str(entryName)
        # 百科分类ID
        self.params['categoryId'] = int(categoryId)
        # 百科封面图
        if coverPic != '':
            self.params['coverPic'] = str(coverPic)
        # 是否热门：1热门 0非热门
        if isHot != 0:
            self.params['isHot'] = int(isHot)
        # 显示状态：1显示 0不显示
        if status != 0:
            self.params['status'] = int(status)
        # 审核状态：0待审核 1已审核 2审核拒绝
        if auditStatus != 0:
            self.params['auditStatus'] = int(auditStatus)
        # 发布时间戳
        self.params['publishTime'] = int(publishTime)
        # HTML正文内容
        self.params['contentStr'] = str(contentStr)
        # 浏览量
        self.params['browseCount'] = int(browseCount)
        # 关键字
        if keywords != '':
            self.params['keywords'] = str(keywords)
        # 标签，多个逗号隔开
        self.params['labelList'] = str(labelListStr)

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-entry/create', data=self.params),
                                function='Add_Entry')

    def Query_Entry(
            self, entryIdint: int, categoryName='', status=0, auditStatus=0, inquireIndex=1
    ):
        """
        1、查询百科词条

        :param entryIdint: 百科词条ID
        :param categoryName: 百科词条分类名称
        :param status: 显示状态：不显示 -> 0 or 显示 -> 1
        :param auditStatus: 审核状态：通过 -> 1 or 待审核 -> 0 or 不通过 -> 2
        :param inquireIndex: 查询个数
        :return:
        """

        self.__init__()
        # 百科词条ID
        self.params['entryId'] = int(entryIdint)
        # 百科词条分类名称
        if categoryName != '':
            self.params['classify'] = str(categoryName)
        # 显示状态：1 -> 显示 or 0 -> 不显示
        if status != 0 and isinstance(status, int):
            self.params['status'] = int(status)
        # 审核状态：0 -> 待审核 or 1 -> 已审核 or 2 -> 审核拒绝
        if auditStatus != 0 and isinstance(auditStatus, int):
            self.params['auditStatus'] = int(auditStatus)
        # 查询个数
        if not inquireIndex == 1 and isinstance(inquireIndex, int):
            self.params['inquireIndex'] = int(inquireIndex)

        self.Params()

        return self.Format_Data(response=requests.get(self.requestsUrl + '/interface-entry/query', params=self.params),
                                function='Query_Entry')


class PublicClass2:
    """
    1、画帮帮
    """

    def __init__(self):
        # 正式
        self.requestsUrl = 'https://master.huabangbang.com'
        # 测试
        # self.requestsUrl = 'https://admin.huabangbang.com'
        # 定义请求参数
        self.params = {
            'accessToken': '',
        }

    def __Encrypt(self, params: dict):
        """
        1、生成签名MD5

        :param params: 参数
        :return:
        """

        encrypt = hashlib.md5()
        dataStr = 'f077ac807b4954d5e57aa82660b4438f'
        for i in sorted(params):
            if isinstance(params[i], list):
                dataStr += f'{i}{"".join(params[i])}'
            else:
                dataStr += f'{i}{params[i]}'
        dataStr += 'f077ac807b4954d5e57aa82660b4438f'
        encrypt.update(dataStr.encode('utf-8'))
        return ((encrypt.hexdigest())[10:20]).upper()

    def Params(self):
        # 时间戳
        self.params['timestamp'] = int(str(time.time())[:10])
        # 签名
        self.params['sign'] = self.__Encrypt(self.params)

    def Format_Data(self, response: requests.Response, function: str) -> [{}, {}] or str:

        # 读取为JSON
        responseJson = json.loads(response.text)

        # 请求失败
        if int(responseJson['code']) != 0:
            return responseJson['message']

        # 成功的数据 [{},{}]
        successDataList = []
        # 添加文章
        if function == 'Add_Article':
            # 读取
            successDataList.append(
                {
                    # 文章ID
                    'idInt': int(responseJson['data']['articleId']),
                    # 文章标题
                    'articleTitle': str(responseJson['data']['title']),
                }
            )
            return successDataList

        # 更新文章
        elif function == 'Update_Article':
            # 读取
            successDataList.append(
                {
                    # 文章ID
                    'idInt': int(responseJson['data']['articleId']),
                }
            )

            return successDataList


class ArticleClassAPI2(PublicClass2):
    """
    1、画帮帮资讯文章
    """

    def Add_Article(
            self, articleTitle: str, thumbnailStr: str, descriptionStr: str, contentStr: str, classify: str, readingVolumeInt: int,
            releaseTimeInt: int, labelStr: str, isPublish=1, isRecommend=0,
    ):
        """
        1、添加画帮帮资讯文章

        :param articleTitle: 文章标题
        :param thumbnailStr: 缩略图链接
        :param descriptionStr: 文章摘要
        :param contentStr: 文章内容
        :param classify: 分类名称
        :param readingVolumeInt: 阅读量
        :param releaseTimeInt: 发布时间
        :param labelStr: 标签字符串
        :param isPublish: 发布状态：已发布 -> 0 or 未发布（待审核） -> 1 or 待发布（已审核） -> 2
        :param isRecommend: 是否推荐：不推荐 -> 0 or 推荐 -> 1
        :return:
        """

        self.__init__()
        # 文章标题
        self.params['articleTitle'] = str(articleTitle)
        # 分类名称
        self.params['classify'] = str(classify)
        # 阅读量
        self.params['readingVolumeInt'] = int(readingVolumeInt)
        # 标签，多个逗号隔开
        self.params['labelList'] = str(labelStr)
        # tdk关键词
        self.params['tdk_k'] = str(labelStr)
        # 缩略图
        self.params['thumbnailStr'] = str(thumbnailStr)
        # 文章摘要
        self.params['descriptionStr'] = str(descriptionStr)
        # tdk内容
        self.params['tdk_d'] = str(descriptionStr)
        # 发布时间
        self.params['releaseTimeInt'] = int(releaseTimeInt)
        # 文章内容HTML
        self.params['contentStr'] = str(contentStr)
        # 发布状态
        self.params['isPublish'] = int(isPublish)
        # 是否推荐
        self.params['isRecommend'] = int(isRecommend)
        # 作者名称
        self.params['author'] = str('hjh')

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-article/create', data=self.params),
                                function='Add_Article')

    def Update_Article(
            self, articleId: int, contentStr: str
    ):
        """
        1、更新文章

        :param articleId: 文章ID
        :param contentStr: 文章内容
        :return:
        """

        self.__init__()
        # 文章ID
        self.params['articleIdInt'] = int(articleId)
        # 文章内容HTML
        self.params['contentStr'] = str(contentStr)

        self.Params()

        return self.Format_Data(response=requests.post(self.requestsUrl + '/interface-article/update', data=self.params),
                                function='Update_Article')


if __name__ == '__main__':
    # 作品
    # a = IllustrationWorkClassAPI()
    # b = a.Query(articleIdInt=1)
    # print(b)
    print('a')
    # 文章
    a = ArticleClassAPI()
    # b = a.Query_Article(articleIdInt=26415, newsHuabshiBool=True, classify='素材参考', inquireIndex=10, arcrankInt=1)
    b = a.Update_Article(articleIdInt=26444, newsHuabshiBool=True, arcrankInt=1,readingVolumeInt=22)
    print(b)

    # 教程
    # a = SectionClassAPI()
    # b = a.Query_Tutorial(tutorialId=1636, inquireIndex=1)
    # b = a.Update_Tutorial(tutorialId=1636, keywordsList=b[0]['labelsStr'],contentStr=b[0]['contentStr'])
    # print(b)

    # 资源
    # a = SectionClassAPI()
    # b = a.Query_Resource(resourceId=1727, inquireIndex=1)
    # b = a.Update_Resource(resourceId=1727, contentStr=b[0]['contentStr'], keywordsList=b[0]['labelsStr'])
    # print(b)

    # 百科词条
    # a = EntryAPI()
    # b = a.Query_Entry(entryIdint=93, inquireIndex=10, categoryName='游戏', status=1)
    # print(b)
    pass
