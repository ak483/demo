# coding=utf-8


def switch_(url):#url转换
    browser.switch_to.default_content()
    # 获取所有窗口句柄集合
    handles = browser.window_handles
    # 创建页面
    handles = seleniumClass().Create_New_Page(browser=browser, newPageUrl=url)


class Account():

    def douyin(self):#抖音账号日报
        datalist = []
        browser.get('https://creator.douyin.com/creator-micro/home')
        browser.maximize_window()
        while True:
            try:
                WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="发布视频"]')))
                time.sleep(3)
                break
            except Exception:
                continue
        time.sleep(1)
        fans = browser.find_element(By.XPATH, '//div[@class="info--3nLbr"]/div[2]/div[1]/div[3]/span').text #粉丝数
        name = browser.find_element(By.XPATH, '//div[@class="baseinfo--2Vic1"]//div[@class="baseinfo--2Vic1"]').text #平台账户名称
        browser.find_element(By.XPATH, '//span[text()="数据总览"]').click()
        time.sleep(2)
        try:  #没有数据直接退出
            Play = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[1]/div[2]').text
        except:
            return False
        approve = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[3]/div[2]').text
        share = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[4]/div[2]').text
        comment = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[5]/div[2]').text
        Fans_raise = browser.find_element(By.XPATH, '//div[@class="flex-container--2YsHy"]/div[6]/div[2]').text
        platform = '抖音'

        datalist.append(day)
        datalist.append(name)
        datalist.append(platform)
        datalist.append('')#发布量
        datalist.append(Play)
        datalist.append(approve)
        datalist.append(approve_rate)
        datalist.append(comment)
        datalist.append(comment_rate)
        datalist.append(share)
        datalist.append(share_rate)
        datalist.append(Fans_raise)
        datalist.append(fans)
        All_datalist.append(datalist)


    def kuaishou(self):
        datalist = []
        while True:
            try:
                WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(text(),"发布视频")]')))
                time.sleep(3)
                break
            except Exception:
                continue

        div_list = browser.find_elements(By.XPATH, '//div[@class="tooltip"]/span')
        if len(div_list)==0:
            return False
        name = browser.find_element(By.XPATH, '//div[@class="detail__name"]').text
        fans = browser.find_element(By.XPATH, '//div[@class="detail__row"]/div[1]/div[1]').text
        Play = div_list[0].text
        Fans_raise = div_list[2].text
        comment = div_list[3].text
        approve = div_list[4].text
        share = div_list[5].text
        platform = "快手"


        datalist.append(day)
        datalist.append(name)
        datalist.append(platform)
        datalist.append('')#发布量
        datalist.append(Play)
        datalist.append(approve)
        datalist.append(approve_rate)
        datalist.append(comment)
        datalist.append(comment_rate)
        datalist.append(share)
        datalist.append(share_rate)
        datalist.append(Fans_raise)
        datalist.append(fans)
        All_datalist.append(datalist)
        return True

    def bilibili(self):
        datalist = []
        while True:
            try:
                WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
                time.sleep(3)
                break
            except Exception:
                continue

        fans = browser.find_element(By.XPATH, '//div[@class="section-row bcc-row first"]/div[1]/div[1]/div[1]/div[2]/span').text
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[text()="近7天"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//ul[@class="options-box"]//li[1]').click()
        time.sleep(1)

        div_list = browser.find_elements(By.XPATH, '//div[@class="value xx-bin-bold"]/span')
        Play = div_list[0].text
        Fans_raise = div_list[2].text
        approve = div_list[3].text
        comment = div_list[6].text
        share = div_list[8].text
        platform = "b站"


        datalist.append(day)
        datalist.append(bili_name)
        datalist.append(platform)
        datalist.append('')  # 发布量
        datalist.append(Play)
        datalist.append(approve)
        datalist.append(approve_rate)
        datalist.append(comment)
        datalist.append(comment_rate)
        datalist.append(share)
        datalist.append(share_rate)
        datalist.append(Fans_raise)
        datalist.append(fans)
        All_datalist.append(datalist)

    def xiaohongshu(self):
        datalist = []
        # 抓取的是近7日的
        while True:
            try:
                WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//a[text()="发布笔记"]')))
                time.sleep(3)
                break
            except Exception:
                continue
        # time.sleep(1)
        # browser.find_element(By.XPATH, '//div[text()="数据看板"]').click()
        name = browser.find_element(By.XPATH, '//span[@class="name-box"]').text
        fans = browser.find_element(By.XPATH, '//p[@class="detail"]/span[2]/label').text
        time.sleep(2)
        browser.find_element(By.XPATH, '//div[contains(text(),"笔记数据")]').click()
        time.sleep(1)
        div_list = browser.find_elements(By.XPATH, '//div[@class="block-line"]//span[2]')


        datalist.append(day)
        datalist.append(name)
        datalist.append(platform)
        datalist.append('')
        datalist.append(Play)
        datalist.append(approve)
        datalist.append(approve_rate)
        datalist.append(comment)
        datalist.append(comment_rate)
        datalist.append(share)
        datalist.append(share_rate)
        datalist.append(Fans_raise)
        datalist.append(fans)
        All_datalist.append(datalist)

    def shipinhao():
        datalist = []
        while True:
            try:
                WebDriverWait(browser, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//span[text()="首页"]')))
                time.sleep(3)
                break
            except Exception:
                continue
        name = browser.find_element(By.XPATH, '//h2').text
        fans = browser.find_element(By.XPATH, '//div[@class="finder-info"]/div[2]/span[2]').text

        time.sleep(1)
        browser.find_element(By.XPATH, '//span[text()="数据中心"]').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[text()="关注者数据"]').click()
        time.sleep(1)
        # 获取关注数据
        div_list = browser.find_elements(By.XPATH, '//div[@class="value"]')
        Fans_raise = div_list[1].text
        browser.find_element(By.XPATH, '//span[text()="动态数据"]').click()
        time.sleep(1)
        # 获取动态数据
        div_list = browser.find_elements(By.XPATH, '//div[@class="value"]')
        Play = div_list[0].text
        approve = div_list[1].text
        comment = div_list[2].text
        share = div_list[3].text
        platform = '视频号'


        datalist.append(day)
        datalist.append(name)
        datalist.append(platform)
        datalist.append('')  # 发布量
        datalist.append(Play)
        datalist.append(approve)
        datalist.append(approve_rate)
        datalist.append(comment)
        datalist.append(comment_rate)
        datalist.append(share)
        datalist.append(share_rate)
        datalist.append(Fans_raise)
        datalist.append(fans)
        All_datalist.append(datalist)

if __name__ == '__main__':
    pass
