# coding=utf-8


class Account_Clear():

    def douyin_clear(self):
        # 清洗数据
        Play = re.sub(',', '', Play)
        Fans_raise = re.sub(',', '', Fans_raise)
        comment = re.sub(',', '', comment)
        approve = re.sub(',', '', approve)
        share = re.sub(',', '', share)
        fans = re.sub(',', '', fans)

        if Play == '0':
            approve_rate = 0
            share_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve) / int(Play)
            share_rate = int(share) / int(Play)
            comment_rate = int(comment) / int(Play)
    def kuaishou_clear(self):
        Play = re.sub(',', '', Play)
        Fans_raise = re.sub(',', '', Fans_raise)
        comment = re.sub(',', '', comment)
        approve = re.sub(',', '', approve)
        share = re.sub(',', '', share)
        Play = re.sub('\+', '', Play)
        Fans_raise = re.sub('\+', '', Fans_raise)
        comment = re.sub('\+', '', comment)
        approve = re.sub('\+', '', approve)
        share = re.sub('\+', '', share)
        fans = re.sub(',', '', fans)

        if Play == '0':
            approve_rate = 0
            share_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve) / int(Play)
            share_rate = int(share) / int(Play)
            comment_rate = int(comment) / int(Play)

    def bilibili_clear(self):
        Play = re.sub(',', '', Play)
        Fans_raise = re.sub(',', '', Fans_raise)
        comment = re.sub(',', '', comment)
        approve = re.sub(',', '', approve)
        share = re.sub(',', '', share)
        fans = re.sub(',', '', fans)
        if Play == '0万':
            Play = '0'
        if Fans_raise == '0万':
            Fans_raise = 0
        if comment == '0万':
            comment = 0
        if approve == '0万':
            approve = 0
        if share == '0万':
            share = 0
        if fans == '0万':
            fans = 0

        if Play == '0':
            approve_rate = 0
            share_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve) / int(Play)
            share_rate = int(share) / int(Play)
            comment_rate = int(comment) / int(Play)

    def Xiaohongshu_clear(self):
        Play = div_list[0].text
        approve = div_list[2].text
        comment = div_list[4].text
        Fans_raise = div_list[6].text
        platform = '小红书'
        share = ''

        Play = re.sub(',', '', Play)
        Fans_raise = re.sub(',', '', Fans_raise)
        comment = re.sub(',', '', comment)
        approve = re.sub(',', '', approve)
        share = re.sub(',', '', share)
        fans = re.sub(',', '', fans)

        if Play == '0':
            approve_rate = 0
            share_rate = ''
            comment_rate = 0
        else:
            approve_rate = int(approve) / int(Play)
            share_rate = ''
            comment_rate = int(comment) / int(Play)

    def Shipinhao_clear(self):

        Play = re.sub(',', '', Play)
        Fans_raise = re.sub(',', '', Fans_raise)
        comment = re.sub(',', '', comment)
        approve = re.sub(',', '', approve)
        share = re.sub(',', '', share)
        fans = re.sub(',', '', fans)

        if Play == '0':
            approve_rate = 0
            share_rate = 0
            comment_rate = 0
        else:
            approve_rate = int(approve) / int(Play)
            share_rate = int(share) / int(Play)
            comment_rate = int(comment) / int(Play)

class Video_clear():
    def douyin(self):




if __name__ == '__main__':
    pass
