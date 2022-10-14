# coding=utf-8

class Video():

    def douyin_video1():  # 获取抖音所有作品
        browser.get('https://creator.douyin.com/creator-micro/home')
        browser.maximize_window()
        time.sleep(1)
        name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
        platform = '抖音'
        browser.find_element(By.XPATH, '//span[text()="作品管理"]').click()
        time.sleep(1)
        if len(browser.find_elements(By.XPATH, '//div[@class="info-title-text--kEYth info-title-small-desc--tW-Ce"]')) == 0:  # 如果账号没有数据则退出
            return False

        while True:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(text(),"没有更多视频")]')))
                time.sleep(3)
                break
            except Exception:
                continue

        title = browser.find_elements(By.XPATH, '//div[@class="info-title-text--kEYth info-title-small-desc--tW-Ce"]')
        play = browser.find_elements(By.XPATH, '//div[@class="info-row--1OQ3-"]/div[1]/span')
        comment = browser.find_elements(By.XPATH, '//div[@class="info-row--1OQ3-"]/div[2]/span')
        approve = browser.find_elements(By.XPATH, '//div[@class="info-row--1OQ3-"]/div[3]/span')
        times = browser.find_elements(By.XPATH, '//div[@class="info-time--1PtPa"]')

        for i in range(len(title)):

            douyin_public_time = times[i].text
            douyin_public_time = re.sub('年', '/', douyin_public_time)
            douyin_public_time = re.sub('月', '/', douyin_public_time)
            douyin_public_time = re.sub('日.*$', '', douyin_public_time)
            # 播放数据
            j = play[i].text
            if "w" in j:
                j = re.sub('w', '', j)
                j = float(j) * 10000
            if j == '0':
                approve_rate = 0
                comment_rate = 0
            else:
                approve_rate = int(approve[i].text) / int(j)
                comment_rate = int(comment[i].text) / int(j)

            datalist = []
            datalist.append(day)
            datalist.append(title[i].text)  # 标题
            datalist.append(name)
            datalist.append(platform)
            datalist.append(douyin_public_time)  # 发布时间
            datalist.append('')  # 发布天数
            datalist.append(int(j))  # 播放
            datalist.append('')  # 完播率
            datalist.append('')  # 均播
            datalist.append(int(approve[i].text))  # 点赞
            datalist.append(approve_rate)  # 点赞率
            datalist.append(int(comment[i].text))
            datalist.append(comment_rate)
            datalist.append('')  # 分享
            datalist.append('')  # 分享率
            datalist.append('')  # 视频带粉
            All_datalist1.append(datalist)
        return True

    def douyin_video():  # 获取抖音最近30天发布的作品
        browser.find_element(By.XPATH, '//span[text()="关注管理"]').click()
        browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()

        time.sleep(1)
        name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text
        platform = '抖音'
        browser.find_element(By.XPATH, '//span[text()="作品数据"]').click()
        Publish_time = browser.find_elements(By.XPATH, '//div[@class="date-text--2Aa6v"]')
        if len(Publish_time) == 0:  # 判断是否存在最近30天作品
            print(name, '没有最近30天作品')
        else:
            title = browser.find_elements(By.XPATH, '//div[@class="title-text--37-P9 first-text--2S8h2"]')
            play = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[3]//div[@class="number-text--1NhF0"]')
            finish_play = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[9]//div[@class="number-text--1NhF0"]')
            ave_time = ''
            approve = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[4]//div[@class="number-text--1NhF0"]')
            comment = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[6]//div[@class="number-text--1NhF0"]')
            share = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[5]//div[@class="number-text--1NhF0"]')
            Fans_raise = browser.find_elements(By.XPATH, '//tr[@class="semi-table-row"]/td[8]//div[@class="number-text--1NhF0"]')

            for i in range(len(title)):
                datalist = []
                datalist.append(day)
                datalist.append(title[i].text)
                datalist.append(name)
                datalist.append(platform)

                # 清洗发布时间
                douyin_public_time = Publish_time[i].text
                douyin_public_time = re.sub('年', '/', douyin_public_time)
                douyin_public_time = re.sub('月', '/', douyin_public_time)
                douyin_public_time = re.sub('日.*$', '', douyin_public_time)
                datalist.append(douyin_public_time)

                datalist.append('')  # 发布天数
                j = play[i].text  # 播放数据
                if "w" in j:
                    j = re.sub('w', '', j)
                    j = float(j) * 10000

                datalist.append(int(j))
                datalist.append(finish_play[i].text)
                datalist.append(ave_time)
                datalist.append(int(approve[i].text))
                if j == '0':
                    approve_rate = 0
                    share_rate = 0
                    comment_rate = 0
                else:
                    approve_rate = int(approve[i].text) / int(j)
                    share_rate = int(share[i].text) / int(j)
                    comment_rate = int(comment[i].text) / int(j)

                datalist.append(approve_rate)  # 点赞率
                datalist.append(int(comment[i].text))
                datalist.append(comment_rate)
                datalist.append(int(share[i].text))
                datalist.append(share_rate)
                datalist.append(int(Fans_raise[i].text))
                Douyin_All_datalist.append(datalist)
            for i in range(len(Douyin_All_datalist)):
                All_datalist1[i] = Douyin_All_datalist[i]

    def kuaishou_video():

        browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()
        time.sleep(1)
        platform = "快手"
        name = browser.find_element(By.XPATH, '//div[@class="detail__name"]').text

        time.sleep(1)
        # browser.find_element(By.XPATH, '//span[contains(text(),"数据中心")]').click()
        # time.sleep(1)
        browser.find_element(By.XPATH, '//li[contains(text(),"视频数据")]').click()
        time.sleep(1)

        Publish_time = browser.find_elements(By.XPATH, '//div[@class="video-item__info__detail__date"]')
        if len(Publish_time) == 0:
            return
        title = browser.find_elements(By.XPATH, '//div[@class="video-item__info__detail__title__content"]')
        play = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[1]/div[2]')
        finish_play = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[2]/div[2]')
        ave_time = ''
        approve = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[5]/div[2]')
        comment = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[4]/div[2]')
        share = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[6]/div[2]')
        Fans_raise = browser.find_elements(By.XPATH, '//div[@class="video-item__data"]/div[3]/div[2]')

        for i in range(len(title)):
            datalist = []
            datalist.append(day)
            datalist.append(re.sub(' ', '', title[i].text))
            datalist.append(name)
            datalist.append(platform)

            # 清洗发布时间
            kuaishou_public_time = Publish_time[i].text
            kuaishou_public_time = re.sub('发布于 ', '', kuaishou_public_time)
            kuaishou_public_time = re.sub('-', '/', kuaishou_public_time)
            kuaishou_public_time = re.sub(' .*$', '', kuaishou_public_time)

            datalist.append(kuaishou_public_time)
            # 发布天数
            datalist.append('')
            j = play[i].text
            if "万" in j:
                j = re.sub('万', '', j)
                j = int(float(j) * 10000)
            j = re.sub(',', '', str(j))
            datalist.append(int(j))  # 播放量
            if finish_play[i].text == '--':
                finish_play[i] = '0%'
            datalist.append(finish_play[i])
            datalist.append(ave_time)

            a = approve[i].text
            b = (comment[i].text)
            c = (share[i].text)
            d = Fans_raise[i].text

            a = re.sub(',', '', str(a))
            if "万" in a:
                a = re.sub('万', '', a)
                a = int((float(a),) * 10000)
            elif "--" in a:
                a = 0

            b = re.sub(',', '', (b))
            if "万" in b:
                b = re.sub('万', '', b)
                b = int(float(b) * 10000)
            elif "--" in b:
                b = 0

            c = re.sub(',', '', str(c))
            if "万" in c:
                c = re.sub('万', '', c)
                c = int(float(c) * 10000)
            elif "--" in c:
                c = 0

            d = re.sub(',', '', str(d))
            if "万" in d:
                d = re.sub('万', '', d)
                d = int(float(d) * 10000)
            elif "--" in d:
                d = 0

            if j == '0':
                approve_rate = 0
                share_rate = 0
                comment_rate = 0
            else:
                approve_rate = int(a) / int(j)
                share_rate = int(c) / int(j)
                comment_rate = int(b) / int(j)

            datalist.append(int(a))  # 点赞量
            datalist.append(approve_rate)  # 点赞率
            datalist.append(int(b))  # 评论量
            datalist.append(share_rate)  # 评论率
            datalist.append(int(c))  # 转发量
            datalist.append(comment_rate)  # 转发率
            datalist.append(int(d))  # 增粉数

            All_datalist1.append(datalist)

    def bilibili_video():

        browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()
        time.sleep(1)
        platform = "b站"
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[contains(text(),"内容管理")]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[contains(text(),"稿件管理")]').click()
        time.sleep(1)

        Publish_time = browser.find_elements(By.XPATH, '//div[@class="pubdate is-success"]/span[1]')
        if len(Publish_time) == 0:
            return
        title = browser.find_elements(By.XPATH, '//div[@class="meta-title"]/a')
        play = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[1]//span')
        finish_play = ''
        ave_time = ''
        approve = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[6]//span')
        comment = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[3]//span')
        share = browser.find_elements(By.XPATH, '//div[@class="meta-footer clearfix"]/div[7]//span')
        Fans_raise = ''

        # 获取名称
        # switch_(FILE_PATH_DICT['b站个人主页'])
        # name = browser.find_element(By.XPATH, '//span[@id="h-name"]').text

        for i in range(len(title)):
            datalist = []
            datalist.append(day)
            datalist.append(title[i].text)
            datalist.append(bili_name)
            datalist.append(platform)

            # 发布时间清洗
            bilibili_public_time = Publish_time[i].text
            bilibili_public_time = re.sub('-', '/', bilibili_public_time)
            bilibili_public_time = re.sub(' .*$', '', bilibili_public_time)
            bilibili_public_time = '20' + bilibili_public_time

            datalist.append(bilibili_public_time)
            datalist.append('')
            j = play[i].text
            if "w" in j:
                j = re.sub('w', '', j)

                j = float(j) * 10000

            datalist.append(int(j))
            datalist.append(finish_play)
            datalist.append(ave_time)
            datalist.append(int(approve[i].text))
            datalist.append(int(approve[i].text) / int(j))  # 点赞率
            datalist.append(int(comment[i].text))
            datalist.append(int(comment[i].text) / int(j))
            datalist.append(int(share[i].text))
            datalist.append(int(share[i].text) / int(j))
            datalist.append(Fans_raise)
            All_datalist1.append(datalist)

    def xiaohongshu_video():

        browser.find_element(By.XPATH, '//div[contains(text(),"首页")]').click()
        time.sleep(1)
        # browser.find_element(By.XPATH, '//div[text()="数据看板"]').click()
        name = browser.find_element(By.XPATH, '//span[@class="name-box"]').text
        platform = '小红书'
        time.sleep(2)
        browser.find_element(By.XPATH, '//div[contains(text(),"笔记数据")]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//input[@readonly]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//div[contains(text(),"48条")]').click()
        time.sleep(1)
        Publish_time = browser.find_elements(By.XPATH, '//span[@class="publish-time"]')
        if len(Publish_time) == 0:
            return
        title = browser.find_elements(By.XPATH, '//span[@class="title"]')
        play = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[1]/b')
        finish_play = ''
        ave_time = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[2]/b')
        approve = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[1]/li[3]/b')
        comment = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[1]/b')
        share = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[3]/b')
        Fans_raise = browser.find_elements(By.XPATH, '//div[@class="info-list"]/ul[2]/li[4]/b')

        for i in range(len(title)):
            datalist = []
            datalist.append(day)
            datalist.append(title[i].text)
            datalist.append(name)
            datalist.append(platform)
            xiaohongshu_public_time = Publish_time[i].text
            xiaohongshu_public_time = re.sub('发布于 ', '', xiaohongshu_public_time)
            xiaohongshu_public_time = re.sub('-', '/', xiaohongshu_public_time)

            datalist.append(xiaohongshu_public_time)
            datalist.append('')
            j = play[i].text
            if "w" in j:
                j = re.sub('w', '', j)

                j = float(j) * 10000
            datalist.append(int(j))  # 播放量
            datalist.append(finish_play)
            ave_times = ave_time[i].text
            ave_times = re.sub('s', '', ave_times)
            if 'min' in ave_times:
                ave_times = re.sub('min', '', ave_times)
                ave_times = int(ave_times) * 60
            datalist.append(int(ave_times))
            datalist.append(int(approve[i].text))
            datalist.append(int(approve[i].text) / int(j))  # 点赞率
            datalist.append(int(comment[i].text))
            datalist.append(int(comment[i].text) / int(j))
            datalist.append(int(share[i].text))
            datalist.append(int(share[i].text) / int(j))
            datalist.append(int(Fans_raise[i].text))
            All_datalist1.append(datalist)

    def shipinhao_video1():

        # browser.get('https://channels.weixin.qq.com/platform')

        browser.maximize_window()
        platform = '视频号'
        browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()
        name = browser.find_element(By.XPATH, '//h2').text
        browser.find_element(By.XPATH, '//span[text()="内容管理"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[text()="动态管理"]').click()
        time.sleep(2)
        page = browser.find_elements(By.XPATH, '//span[@class="weui-desktop-pagination__num__wrp spread"]/label')  # 判断有多少页
        if len(page) == 0:
            page = [1]
        for l in range(len(page)):

            page_text = browser.page_source
            tree = etree.HTML(page_text)

            title = tree.xpath('//div[@class="post-title"]')
            if len(title) == 0:
                return False
            play = tree.xpath('//div[@class="post-data"]/div[1]/span[2]')
            comment = tree.xpath('//div[@class="post-data"]/div[3]/span[2]')
            approve = tree.xpath('//div[@class="post-data"]/div[2]/span[2]')
            share = tree.xpath('//div[@class="post-data"]/div[4]/span[1]')
            Publish_time = tree.xpath('//div[@class="post-time"]/span')

            for i in range(len(title)):
                datalist = []
                datalist.append(day)
                datalist.append(title[i].text)
                datalist.append(name)
                datalist.append(platform)
                shipinhao_public_time = Publish_time[i].text
                shipinhao_public_time = re.sub('年', '/', shipinhao_public_time)
                shipinhao_public_time = re.sub('月', '/', shipinhao_public_time)
                shipinhao_public_time = re.sub('日.*$', '', shipinhao_public_time)
                datalist.append(shipinhao_public_time)
                datalist.append('')  # 发布天数
                j = play[i].text
                if "万" in j:
                    j = re.sub('万', '', j)
                    j = float(j) * 10000
                datalist.append(int(j))  # 播放量
                datalist.append('')  # 完播率
                datalist.append('')  # 平均播放时长
                datalist.append(int(approve[i].text))  # 点赞量
                if j == '0':
                    datalist.append(0)  # 点赞率
                    datalist.append(int(comment[i].text))
                    datalist.append(0)
                    datalist.append(int(share[i].text))
                    datalist.append(0)
                else:
                    datalist.append(int(approve[i].text) / int(j))  # 点赞率
                    datalist.append(int(comment[i].text))
                    datalist.append(int(comment[i].text) / int(j))
                    datalist.append(int(share[i].text))
                    datalist.append(int(share[i].text) / int(j))
                datalist.append('')  # 视频带粉

                Shipinhao_All_datalist.append(datalist)
            if len(page) != 1:
                input('点击下一页')
            #     browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            #     input('滑到底部')
            #     browser.find_element(By.XPATH, '//a[text()="下一页"]').click()
            # time.sleep(1)

        return True

    def shipinhao_video():

        browser.find_element(By.XPATH, '//span[contains(text(),"首页")]').click()

        platform = '视频号'
        name = browser.find_element(By.XPATH, '//h2').text

        time.sleep(1)
        # browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
        # time.sleep(1)
        browser.find_element(By.XPATH, '//span[text()="动态数据"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//a[contains(text(),"单篇动态")]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[contains(text(),"近30天数据")]').click()

        Publish_time = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[2]')
        if len(Publish_time) != 0:
            title = browser.find_elements(By.XPATH, '//div[@class="post-wrap"]/span')
            play = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[5]')
            finish_play = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[3]')
            ave_time = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[4]')
            approve = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[6]')
            comment = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[7]')
            share = browser.find_elements(By.XPATH, '//tr[@class="ant-table-row ant-table-row-level-0"]/td[8]')
            Fans_raise = ''
            for i in range(len(title)):
                datalist = []
                datalist.append(day)
                datalist.append(title[i].text)
                datalist.append(name)
                datalist.append(platform)
                datalist.append(Publish_time[i].text)
                datalist.append('')
                j = play[i].text
                if "万" in j:
                    j = re.sub('万', '', j)

                    j = float(j) * 10000

                datalist.append(int(j))
                if finish_play[i].text == '0':
                    finish_play[i] = '0%'
                datalist.append(finish_play[i])
                ave_times = ave_time[i].text
                ave_times = re.sub('\..*$', '', ave_times)
                ave_times = re.sub('-', '0', ave_times)
                datalist.append(int(ave_times))
                datalist.append(int(approve[i].text))

                if j == '0':
                    datalist.append(0)  # 点赞率
                    datalist.append(int(comment[i].text))
                    datalist.append(0)
                    datalist.append(int(share[i].text))
                    datalist.append(0)
                else:
                    datalist.append(int(approve[i].text) / int(j))  # 点赞率
                    datalist.append(int(comment[i].text))
                    datalist.append(int(comment[i].text) / int(j))
                    datalist.append(int(share[i].text))
                    datalist.append(int(share[i].text) / int(j))
                datalist.append(Fans_raise)
                Shipinhao_All_datalist1.append(datalist)  # 最近30天的视频
                for i in range(len(Shipinhao_All_datalist1)):  # 将最近30天的作品并入所有作品中
                    Shipinhao_All_datalist[i] = Shipinhao_All_datalist1[i]
                for i in range(len(Shipinhao_All_datalist)):  # 将视频号所有作品纳入总数据中
                    All_datalist1.append(Shipinhao_All_datalist[i])
        else:  # 单独将30天外数据存入
            for i in range(len(Shipinhao_All_datalist)):  # 将视频号所有作品纳入总数据中
                All_datalist1.append(Shipinhao_All_datalist[i])