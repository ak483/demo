import sys, os, time, pprint, pyperclip, threading, logging, cv2,re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui as pag
from PIL import Image

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
from My_code.Toolbox import Selenium
from My_code.名动漫.Mdm_API import IllustrationWorkClassAPI
from My_code.Toolbox.Download_Image import Download_Image


class ZcoolClass:

    def __init__(self):
        # 作品标题对应ID
        self.worksIdDict = {}

    def Zcool(self, userName: str, userPass: str, worksDataList: list, getImgUrl=False):
        """
        1、站酷网主程序

        :param userName: 账号名称
        :param userPass: 账号密码
        :param worksDataList: 作品字典列表
        :param getImgUrl: 是否获取URL链接
        :return:
        """

        # 登录
        browser = self.Selenium_Login(userName, userPass)

        # 返回的标题
        titleList = []
        # 作品ID
        idList = []
        # 发布
        for worksDataDict in worksDataList:

            #如果没有图片则跳过
            tmp_name = worksDataDict['nameStr']
            img_path = r'G:\2345下载 - 副本' + f'\{tmp_name}.jpg'
            if os.path.exists(img_path):
                pass
            else:
                continue

            if getImgUrl:
                # 获取链接
                titleList.append(self.Works(browser, worksDataDict, getImgUrl))
            else:
                # 发布作品
                titleList.append(self.Works(browser, worksDataDict, getImgUrl))
                idList.append(worksDataDict['idInt'])
                (pd.DataFrame({'作品ID': idList, '标题': titleList})).to_excel(fr"{FILE_PATH_DICT['站酷花瓣']}\自动保存——站酷.xlsx")

        self.Get_Works_Url(browser, titleList)

        browser.quit()

    def Selenium_Login(self, userName: str, userPass: str) -> webdriver.Chrome:
        """
        1、登录
        :param userName: 账号名称
        :param userPass: 账号密码
        :return: 浏览器
        """

        browser = Selenium.seleniumClass().Selenium_Initialization_Chrome(chromeExe=FILE_PATH_DICT['浏览器程序'], chromeUser=FILE_PATH_DICT['站酷用户'])
        while True:
            # 登录
            browser.maximize_window()
            browser.get('https://www.zcool.com.cn/')
            time.sleep(1)
            # 已登录退出
            try:
                WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="headerImage"]')))
                break
            except Exception:
                pass
            browser.find_elements(By.XPATH,'//span[contains(@class,"header_login")]')[0].click()
            time.sleep(3)
            try:
                WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="login-div-box"]')))
            except Exception:
                continue
            # 切换
            browser.switch_to.frame('loginChild')
            # 账号密码
            browser.find_element(By.XPATH,'//div[@class="l-tab-list"]').click()
            WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="username"]')))
            browser.find_element(By.XPATH,'//*[@id="username"]').send_keys(userName)
            time.sleep(1)
            browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(userPass)
            time.sleep(1)
            time.sleep(2)
            try:
                browser.find_element(By.XPATH,'//*[@id="loginbtn"]').click()
            except Exception:
                logging.info('未能成功点击登录 -> 手动登录')
                logging.info(f'账号：{userName} 密码：{userPass}')
                input('继续：')
                sys.stdout.flush()
                time.sleep(2)
            browser.switch_to.default_content()

            try:
                time.sleep(5)
                WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="login-div-box"]')))
                logging.info('未能成功登录 -> 手动登录')
                logging.info(f'账号：{userName} 密码：{userPass}')
                input('继续：')
                sys.stdout.flush()
                time.sleep(2)
            except Exception:
                pass
            break

        while True:
            # 跳转到作品中心
            browser.get('https://my.zcool.com.cn/works')
            # 检查有没有进入到作品中心
            try:
                WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(text(),"上传作品")]')))
                browser.get('https://my.zcool.com.cn/works')
                break
            except Exception:
                browser.get('https://www.zcool.com.cn/')
                time.sleep(2)
                continue

        return browser

    def Works(self, browser: webdriver.Chrome, worksDataDict: dict, getImgUrl=False) -> str:
        """
        1、发布作品

        :param browser: 浏览器
        :param worksDataDict: 作品字典
        :param getImgUrl: 是否获取URL链接
        :return: 标题名称
        """

        # 作品名称
        global worksNameStr
        worksNameStr = str(worksDataDict['nameStr'])
        categoryStr_ = str(worksDataDict['categoryStr'])
        worksNameStrr = f'{worksNameStr}'+f'({categoryStr_})'
        self.worksIdDict[worksNameStrr] = int(worksDataDict['idInt'])
        if getImgUrl:
            return worksNameStrr
        # 添加单个作品
        logging.info(f'当前作品ID为：{worksDataDict["idInt"]}')
        # 作品类型
        if '临摹' in str(worksDataDict['labelsList']):
            worksClass = '临摹'
        else:
            worksClass = '原创'
        # 一级分类
        worksClass_ = ''
        # 二级分类
        worksClass__ = ''
        # 官网作品分类
        worksClassData = str(worksDataDict['categoryStr'])
        if worksClassData == '商业插画' or worksClassData == 'CG美术基础':
            worksClass_ = '插画'
            worksClass__ = '商业插画'
        elif worksClassData == '角色原画':
            worksClass_ = '插画'
            worksClass__ = '游戏原画'
        elif worksClassData == '场景概念':
            worksClass_ = '插画'
            worksClass__ = '概念设定'
        elif worksClassData == 'CG漫画':
            worksClass_ = '动漫'
            worksClass__ = '其他动漫'
        elif worksClassData == '游戏UI':
            worksClass_ = 'UI'
            worksClass__ = '游戏UI'
        elif worksClassData == '3D模型':
            worksClass_ = '三维'
            worksClass__ = '其他三维'
        else:
            # 作品类型2
            worksClass_ = ''
            # 作品类型3
            worksClass__ = ''

        # 大图链接
        urlStr = str(worksDataDict['bigImageStr'])
        # 关键词列表
        keyStrList = worksDataDict['labelsList']
        # 作品发布时间
        timeStr = str(worksDataDict['publishTimeStr'])
        # 年
        yearStr = timeStr.split('-')[0]
        # 月
        monthStr = timeStr.split('-')[1]
        # 日
        dayStr = (timeStr.split('-')[2]).split(' ')[0]
        # 下载图片
        requestsImgTh = threading.Thread(target=Download_Image, args=(urlStr, FILE_PATH_DICT['站酷花瓣图片下载地址']))
        requestsImgTh.start()

        # 正式控制浏览器
        try:
            browser.get('https://my.zcool.com.cn/works')
            time.sleep(2)
            # 点击开始创作
            WebDriverWait(browser, 10, 1).until(
                EC.presence_of_all_elements_located((By.XPATH, '//section[contains(@class,"leftPanel")]//button[contains(@class,"uploadBtnStyle")]'))
            )
            time.sleep(1)
            browser.find_element(By.XPATH,'//section[contains(@class,"leftPanel")]//button[contains(@class,"uploadBtnStyle")]').click()
            time.sleep(2)
        except Exception as e:
            logging.info('点击上传作品失败 -> 手动点击上传作品')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(2)

        # 输入标题
        while True:
            try:
                WebDriverWait(browser, 15, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@name="title"]')))
                # 添加标题
                browser.find_element(By.XPATH,'//input[@name="title"]').send_keys(worksNameStrr)
                time.sleep(1)
                break
            except Exception:
                input('输入标题有问题 确定后将重新输入：')
                sys.stdout.flush()
                logging.info('正在重新输入...')
                browser.refresh()
            time.sleep(1)

        # 选类型
        browser.find_element(By.XPATH,'//div[contains(@class,"text_container")]').click()
        time.sleep(0.5)
        # 选择类型
        if worksClass == '原创':
            browser.find_elements(By.XPATH,'//div[contains(@class,"radioItem")]')[0].click()
            time.sleep(0.5)
        else:
            browser.find_elements(By.XPATH,'//div[contains(@class,"radioItem")]')[1].click()
            time.sleep(0.5)

        try:
            # 类型2
            if worksClass_ == '插画':
                browser.find_element(By.XPATH,'//section[contains(@class,"listBox")]/ul/li[4]').click()
            elif worksClass_ == '动漫':
                browser.find_element(By.XPATH,'//section[contains(@class,"listBox")]/ul/li[5]').click()
            elif worksClass_ == 'UI':
                browser.find_element(By.XPATH,'//section[contains(@class,"listBox")]/ul/li[2]').click()
            elif worksClass_ == '三维':
                browser.find_element(By.XPATH,'//section[contains(@class,"listBox")]/ul/li[9]').click()
            else:
                logging.info(f'无一级分类：{worksClass_} -> 手动添加一级分类')
                input('等待：')
                sys.stdout.flush()
                logging.info('继续...')
                time.sleep(2)
        except Exception:
            logging.info(f'点击一级分类：{worksClass_} 失败 -> 手动点击一级分类')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(2)
        time.sleep(1)
        try:
            # 类型3
            if worksClass_ == '插画':
                if worksClass__ == '商业插画':
                    browser.find_element(By.XPATH,'//section[contains(@class,"listSubBox")]/ul/li[1]').click()
                elif worksClass__ == '游戏原画':
                    browser.find_element(By.XPATH,'//section[contains(@class,"listSubBox")]/ul/li[3]').click()
                elif worksClass__ == '概念设定':
                    browser.find_element(By.XPATH,'//section[contains(@class,"listSubBox")]/ul/li[2]').click()

            elif worksClass_ == '动漫':
                # 选择其他漫画
                browser.find_elemen(By.XPATH,'//li[contains(text(),"其他动漫")]').click()
                # browser.find_elemen(By.XPATH, '//li[contains(text(),"其他动漫")]').click()
                # pag.press('enter')

            elif worksClass_ == 'UI':
                # 选择游戏UI
                browser.find_element(By.XPATH,'//section[contains(@class,"listSubBox")]/ul/li[2]').click()

            elif worksClass_ == '三维':
                # 选择其他三维
                browser.find_elemen(By.XPATH,'//section[contains(@class,"listSubBox")]/ul/li[7]').click()

            else:
                logging.info(f'手动选择二级分类：{worksClass__}')
                input('继续：')
                sys.stdout.flush()
                time.sleep(2)
        except Exception:
            logging.info(f'点击二级分类：{worksClass__} 失败 -> 手动点击')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(2)
        time.sleep(1)

        # 作品行业
        browser.find_element(By.XPATH,'//div[@name="industry"]').click()
        time.sleep(1.5)
        browser.find_element(By.XPATH,'//div[@class="rc-virtual-list-holder"]//*[@title="教育"]').click()
        time.sleep(1)

        # 添加描述说明
        str_explainStr = str(worksDataDict['explainStr'])
        str_explainStr = re.sub('名动漫', '', str_explainStr)
        browser.find_element(By.XPATH,'//*[@placeholder="作品说明"]').send_keys(str_explainStr)
        time.sleep(1)

        # 上传图片
        ActionChains(browser).move_to_element(browser.find_element(By.XPATH,'//div[@name="productImages"]//input[@type="file"]/..')).perform()
        browser.find_element(By.XPATH,'//div[@name="productImages"]//input[@type="file"]/..').click()
        time.sleep(0.5)
        requestsImgTh.join()
        # 分割图片
        self.Images_Beyond()
        # 控制鼠标
        Mouse_Move(requestsImgTh)
        # 获取图片方向
        xyBool = Image_Direction()

        # 添加标签
        ActionChains(browser).move_to_element(browser.find_element(By.XPATH,'//div[contains(@class,"formItem")]//input')).perform()
        for j in range(len(keyStrList[:10])):
            if keyStrList[j] != '' and str(keyStrList[j]) != 'None':
                try:
                    browser.find_element(By.XPATH,'//div[contains(@class,"formItem")]//input').send_keys(keyStrList[j])
                except Exception:
                    break
                time.sleep(1)
                browser.find_element(By.XPATH,'//div[contains(@class,"formItem")]//button').click()
                time.sleep(1.5)

        # 处理封面
        ActionChains(browser).move_to_element(browser.find_element(By.XPATH,'//div[@name="coverName"]//div[1]//div')).perform()
        browser.find_element(By.XPATH,'//div[@name="coverName"]//div[1]//div').click()
        time.sleep(2)
        try:
            # 向上拖动
            if xyBool:
                pag.moveTo(1117, 500, duration=0.5)
                pag.click(1117, 500)
                # 按照鼠标左键拖动
                pag.dragTo(1117, 400, duration=0.5)
            # 向右拖动
            else:
                pag.moveTo(1117, 500, duration=0.5)
                pag.click(1117, 500)
                # 按照鼠标左键拖动
                pag.dragTo(1200, 500, duration=0.5)
            time.sleep(1)
            browser.find_element(By.XPATH,'//div[@class="modal__footer"]/section/button[1]').click()
        except Exception:
            logging.info('站酷封面上传失败 -> 手动调整图片位置')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(2)
        time.sleep(3)

        # 更多设置
        ActionChains(browser).move_to_element(browser.find_elements(By.XPATH,'//*[contains(@class,"dOmqQl")]')[3]).perform()
        try:
            browser.find_elements(By.XPATH,'//*[contains(@class,"dOmqQl")]')[3].find_element(By.XPATH,'.//span').click()
        except Exception:
            logging.info('点击更多设置失败 -> 手动打开更多设置')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(3)
        time.sleep(1)

        # 滚动到最低
        browser.execute_script('document.documentElement.scrollTop=100000')
        time.sleep(1)

        # 作品分类
        try:
            (browser.find_elements(By.XPATH,'//span[@class="rc-select-selection-item"]'))[-1].click()
        except Exception:
            logging.info('点击作品分类失败 -> 手动点击作品分类')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(3)
        time.sleep(1)
        try:
            if worksClass__ == '其他漫画':
                browser.find_element(By.XPATH,'//div[@title="CG漫画"]').click()
            elif worksClass__ == '商业插画':
                browser.find_element(By.XPATH,'//div[@title="商业插画"]').click()
            elif worksClass__ == '游戏UI':
                browser.find_element(By.XPATH,'//div[@title="游戏UI"]').click()
            elif worksClass__ == '其他三维':
                browser.find_element(By.XPATH,'//div[@title="3D模型"]').click()
            else:
                # 默认CG美术基础
                browser.find_element(By.XPATH,'//div[@title="CG美术基础"]').click()
        except Exception:
            logging.info(f'点击 {worksClass__} 分类失败 -> 手动点击')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(2)

        # 添加时间
        try:
            browser.find_element(By.XPATH,'//div[@class="rc-picker-input"]').click()
        except Exception:
            logging.info('点击添加时间失败 -> 手动点击添加时间')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(3)
        time.sleep(1)
        try:
            # 选择年
            if yearStr not in browser.find_element(By.XPATH,'//div[@class="rc-picker-header-view"]/button[1]').text:
                browser.find_element(By.XPATH,'//div[@class="rc-picker-header-view"]/button[1]').click()
                time.sleep(1)
                browser.find_element(By.XPATH,f'//table[@class="rc-picker-content"]//td[@title="{int(yearStr)}"]').click()
                time.sleep(1)
            # 选择月
            if monthStr + '月' != browser.find_element(By.XPATH,'//div[@class="rc-picker-header-view"]/button[2]').text:
                browser.find_element(By.XPATH,'//div[@class="rc-picker-header-view"]/button[2]').click()
                time.sleep(1)
                browser.find_element(By.XPATH,'//table[@class="rc-picker-content"]//td[@title="{}-{:02d}"]'.format(yearStr, int(monthStr))).click()
                time.sleep(1)
            # 选择日
            browser.find_element(By.XPATH,'//table[@class="rc-picker-content"]//td[@title="{}-{:02d}-{:02d}"]'.format(yearStr, int(monthStr), int(dayStr))).click()
            time.sleep(1)
        except Exception:
            logging.info('点击时间失败 -> 手动点击')
            logging.info(f'年：{yearStr}：月{monthStr}：日{dayStr}')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(2)

        # 等待保存草稿
        # if browser.find_element(By.XPATH,'//span[contains(@class,"hRMpWa")]').text != '已保存草稿':
        #     time.sleep(8)
        time.sleep(8)

        # 发布
        try:
            browser.find_element(By.XPATH,'//button[contains(text(),"发布")]').click()
        except Exception:
            logging.info('点击发布失败 -> 手动点击发布')
            input('等待：')
            sys.stdout.flush()
            logging.info('继续...')
            time.sleep(3)
        time.sleep(3)
        try:
            WebDriverWait(browser, 10, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(text(),"返回创作中心")]')))
            # 返回作品列表
            browser.find_element(By.XPATH,'//button[contains(text(),"返回创作中心")]').click()
        except Exception:
            logging.info('未能发现 "返回作品列表" 按钮 -> 即将重试...')
            time.sleep(2)
            input('等待：')
            # try:
            #     # 发布
            #     browser.find_element(By.XPATH,'//button[contains(text(),"返回创作中心")]').click()
            #     WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class,"dcoOXk")]')))
            #     # 返回作品列表
            #     browser.find_element(By.XPATH,'//button[contains(@class,"dcoOXk")]').click()
            # except Exception:
            #     logging.info('重试失败，请检查问题 -> 确定后将直接返回作品列表')
            #     input('等待：')
            #     sys.stdout.flush()
            #     logging.info('继续...')
            #     time.sleep(2)
            #     browser.get('https://my.zcool.com.cn/works')
        time.sleep(3)
        Img_Remove()

        return worksNameStrr

    def Get_Works_Url(self, browser: webdriver.Chrome, titleList: list):
        """
        1、获取作品链接

        :param browser: 浏览器
        :param titleList: 标题列表
        :return:
        """

        input('是否开始获取图片链接（审核通过后再获取）：')
        sys.stdout.flush()
        logging.info('开始获取...')
        # 打开我的创作
        browser.get('https://my.zcool.com.cn/works')
        time.sleep(2)
        # 存放标题
        divTitleList = []
        # 存放链接
        divUrlList = []
        while True:
            # 获取DIV
            divWeb = browser.find_elements(By.XPATH,'//div[@wrap="wrap"]/div')
            for divWeb_ in divWeb:
                divTitleList.append(divWeb_.find_element(By.XPATH,'.//a[@class="cardImgHover"]').get_attribute('title'))
                divUrlList.append(divWeb_.find_element(By.XPATH,'.//a[@class="cardImgHover"]').get_attribute('href'))
            try:
                browser.find_element(By.XPATH,'//div[contains(@class,"pagination_wrap")]/*[last()]').click()
            except Exception:
                break
            time.sleep(2)
            # 终止
            if len(divTitleList) >= 100:
                break

        # 获取到的标题链接去重
        titleUrlPd = pd.DataFrame({'标题': divTitleList, '链接': divUrlList})
        titleUrlPd = titleUrlPd.drop_duplicates(subset=['标题'])
        titleSaveList, urlSaveList, worksIdList = [], [], []
        # 匹配
        for name in titleList:
            for _, data in titleUrlPd.iterrows():
                dataName = data[0]
                dataUrl = data[1]
                # 当前标题是否匹配
                if dataName == name:
                    titleSaveList.append(name)
                    urlSaveList.append(dataUrl)
                    worksIdList.append(self.worksIdDict[name])
                    (pd.DataFrame({'作品ID': worksIdList, '标题': titleSaveList, '链接': urlSaveList})).to_excel(
                        fr"{FILE_PATH_DICT['站酷花瓣']}\站酷.xlsx", index=False)
                    break

    def Images_Beyond(self):
        """
        1、分割图片

        :return:
        """

        os.chdir(FILE_PATH_DICT['站酷花瓣图片下载地址'])
        for i in os.listdir('.'):
            try:
                img = Image.open(fr'.\{i}')
            except Exception:
                continue
            w, h = img.size
            img.close()
            del img
            if h > 16384:
                # 分割次数
                segmentationIndex = 2
                while True:
                    if h / segmentationIndex > 16384:
                        segmentationIndex += 1
                        continue
                    else:
                        break
                Image_Segmentation(
                    imageFilePath=fr'{FILE_PATH_DICT["站酷花瓣图片下载地址"]}\{i}',
                    imageFileSavePath=FILE_PATH_DICT["站酷花瓣图片下载地址"], segmentationIndex=segmentationIndex
                )


class HuaBanClass:

    def __init__(self):
        # 描述对应作品ID
        self.worksIdDict = {}

    def Huaban(self, userName: str, userPass: str, worksDataList: list, getImgUrl=False):
        """
        1、花瓣网主程序

        :param userName: 账号名称
        :param userPass: 账号密码
        :param worksDataList: 作品字典列表
        :param getImgUrl: 是否获取URL链接
        :return:
        """
        # global worksNameStr
        # worksNameStr = str(worksDataList['nameStr'])


        # 登录
        browser = self.Selenium_Login(userName, userPass)

        # 返回的描述
        miaosuList = []
        # 数据集
        worksDataPd = pd.DataFrame(worksDataList)
        # 按分类分组
        for i, j in worksDataPd.groupby('categoryStr'):
            # 重置索引
            j.index = range(len(j))
            # 发布
            logging.info(f'正在发布该分类：{i}')
            if getImgUrl:
                # 获取链接
                miaosuList.append(self.Works(browser, j, getImgUrl))
            else:
                # 发布作品
                miaosuList.append(self.Works(browser, j))
                (
                    pd.DataFrame({
                        '描述': ['\n'.join([str(j) for j in i]) for i in miaosuList]
                    })
                ).to_excel(fr"{FILE_PATH_DICT['站酷花瓣']}\自动保存——花瓣.xlsx")
            logging.info(f'已发布完该分类：{i}')

        self.Get_Works_Url(browser, miaosuList)

        browser.quit()

    def Selenium_Login(self, userName: str, userPass: str) -> webdriver.Chrome:
        """
        1、登录

        :param userName: 账号名称
        :param userPass: 账号密码
        :return: 浏览器
        """

        browser = Selenium.seleniumClass().Selenium_Initialization_Chrome(chromeExe=FILE_PATH_DICT['浏览器程序'], chromeUser=FILE_PATH_DICT['花瓣用户'])

        while True:
            browser.maximize_window()
            browser.get('https://huaban.com/')
            # 已登录退出
            try:
                WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@data-button-name="登陆注册"]')))
                pass
            except Exception:
                break
            browser.find_element(By.XPATH,'//*[@data-button-name="登陆注册"]').click()
            time.sleep(2)
            # 登录
            browser.find_element(By.XPATH,'//*[@data-placeholder="手机号或邮箱"]/input').send_keys(userName)
            time.sleep(1)
            browser.find_element(By.XPATH,'//*[@data-placeholder="密码"]//input').send_keys(userPass)
            time.sleep(1)
            browser.find_element(By.XPATH,'//*[@data-dialog-title="登录弹窗"]/button').click()
            time.sleep(3)

            browser.get('https://huaban.com/mingdongman/')
            time.sleep(2)

            try:
                # 检查有没有登录成功
                WebDriverWait(browser, 10, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="head-line"]/div')))
                break
            except Exception:
                continue

        return browser

    def Works(self, browser: webdriver.Chrome, worksDataPd: pd.DataFrame, getImgUrlBool=False) -> [str]:
        """
        1、发布作品

        :param browser: 浏览器
        :param worksDataPd: 作品数据集
        :param getImgUrlBool: 是否获取URL链接
        :return: 标题名称列表
        """

        miaosuList, urlList, huaBanList = [], [], []
        # 组合
        for _, data in worksDataPd.iterrows():
            # 描述
            miaosuList.append(str(data[1]) + '-' + str(data[5]))
            # 描述对应作品ID
            self.worksIdDict[str(data[1]) + '-' + str(data[5])] = int(data[0])
            # 大图链接
            urlList.append(str(data[2]))

            # 根据分类对应画板
            if str(data[4]) == 'CG美术基础':
                huaBanList.append('CG美术基础')
            elif str(data[4]) == '角色原画':
                huaBanList.append('角色原画')
            elif str(data[4]) == '场景概念':
                huaBanList.append('场景概念')
            elif str(data[4]) == 'CG漫画':
                huaBanList.append('CG漫画')
            elif str(data[4]) == '商业插画':
                huaBanList.append('商业插画')
            elif str(data[4]) == '游戏UI':
                huaBanList.append('游戏UI')
            elif str(data[4]) == '3D模型':
                huaBanList.append('3D模型')
            else:
                logging.info(f'没有找到该分类画板：{data[4]}')
                huaBanList.append(input('输入分类画板名称：'))
                sys.stdout.flush()
        pass

        del data, _

        if getImgUrlBool:
            return miaosuList

        # 起始
        startIndex = 0
        # 结束
        endIndex = 10
        for i in range(0, len(miaosuList), 10):
            # 下载图片
            requestsImgTh = threading.Thread(target=Download_Image, args=(urlList[startIndex:endIndex], FILE_PATH_DICT['站酷花瓣图片下载地址']))
            requestsImgTh.start()

            # 添加采集
            WebDriverWait(browser, 15, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class,"mRDw5P7W")]')))
            time.sleep(0.5)
            while True:
                ActionChains(browser).move_to_element(
                    (browser.find_elements(By.XPATH,'//div[@class="ant-dropdown-trigger EzlxjT3_"]'))[-1]
                ).perform()
                time.sleep(0.5)

                try:
                    browser.find_element(By.XPATH,'//span[text()="上传采集"]').click()
                    break
                except Exception:
                    logging.info(fr'点击添加采集失败 -> 正在重试...')
                    continue
            time.sleep(3)

            # 上传图片
            try:
                browser.find_element(By.XPATH,'//div[contains(@class,"ant-upload-drag")]/span').click()
            except Exception:
                logging.info(f'点击上传图片失败，手动点击')
                input('继续：')
                sys.stdout.flush()
                time.sleep(2)
            # 操控电脑鼠标
            Mouse_Move(requestsImgTh)
            time.sleep(2)

            # 选择画板
            try:
                # 当前画板与需要选择的画板不一致
                if str(browser.find_element(By.XPATH,'//div[contains(@class,"qDk6HvsO")]/div/div/span[2]').get_attribute('title')) != huaBanList[0]:
                    browser.find_element(By.XPATH,'//div[contains(@class,"qDk6HvsO")]/div/div').click()
                    time.sleep(1)
                    ActionChains(browser).move_to_element(
                        (browser.find_elements(By.XPATH,f'//div[@class="fsHJkcyc" and @title="{huaBanList[0]}"]/../../..'))[-1]
                    ).perform()
                    browser.find_element(By.XPATH,f'//div[@class="fsHJkcyc" and @title="{huaBanList[0]}"]/../../..').click()
                    time.sleep(1)
            except Exception:
                logging.info('花瓣上传图片有问题 或 选择画板有问题：请手动选择画板')
                input('继续：')
                sys.stdout.flush()
                time.sleep(2)

            # 添加描述
            imgIndex = 1
            temp = (browser.find_elements(By.XPATH,'//div[@class="RlFn7ZVa"]'))[0]
            for i in temp.find_elements(By.XPATH,'./div'):
                # 跳过第一个DIV
                if i.get_attribute('class') == 'RlFn7ZVa':
                    continue
                try:
                    # 点击图片
                    i.find_element(By.XPATH,'./div/div/img').click()
                    # 添加描述
                    browser.find_element(By.XPATH,'//*[@placeholder="填写作品相关的描述"]').send_keys(miaosuList[startIndex + imgIndex - 1])
                    time.sleep(1)
                except Exception:
                    try:
                        pprint.pprint(miaosuList[startIndex + imgIndex - 1])
                    except IndexError:
                        break
                    logging.info('添加描述失败 -> 手动添加')
                    input('继续：')
                    sys.stdout.flush()
                    time.sleep(2)
                imgIndex += 1
            del temp

            # 点击上传
            try:
                browser.find_element(By.XPATH,'//button[@data-button-name="上传"]').click()
            except Exception:
                logging.info('点击上传有问题 -> 手动点击上传')
                input('继续：')
                sys.stdout.flush()
            time.sleep(8)
            try:
                WebDriverWait(browser, 15, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-content-source="添加采集"]')))
                logging.info('上传失败！！！手动点击上传！！！')
                input('继续：')
                sys.stdout.flush()
                time.sleep(2)
            except Exception:
                pass

            Img_Remove()
            startIndex = endIndex
            endIndex += 10

        return miaosuList

    def Get_Works_Url(self, browser: webdriver.Chrome, miaosuList: list):
        """
        1、获取作品链接

        :param browser: 浏览器
        :param miaosuList: 描述列表
        :return:
        """

        input('是否开始获取图片链接：')
        sys.stdout.flush()
        logging.info('开始获取...')
        time.sleep(2)
        # 采集页面
        browser.get('https://huaban.com/user/mingdongman/pins')
        time.sleep(3)

        # 存放描述
        divMiaosuList = []
        # 存放描述现对应的ID
        divIdList = []
        # 滚动系数
        gundon = 400
        while True:
            # 获取DIV
            webDiv = browser.find_elements(By.XPATH,'//div[contains(@class,"kgGJbqsa")]/div')
            # 循环添加
            for webDiv_ in webDiv:
                try:
                    # 描述
                    divMiaosuList.append(
                        webDiv_.find_element(By.XPATH,'./div/a/img').get_attribute('alt')
                    )
                    # ID
                    divIdList.append(
                        webDiv_.find_element(By.XPATH,'./div').get_attribute('data-content-id')
                    )
                except Exception:
                    print('跳过添加采集')
                    continue
            # 滚动
            browser.execute_script(f'document.documentElement.scrollTop={gundon}')
            gundon += 500
            time.sleep(1.5)
            # 终止
            if len(divMiaosuList) >= 700:
                break

        # 获取到的描述ID去重
        titleUrlPd = pd.DataFrame({'描述': divMiaosuList, '作品id': divIdList})
        titleUrlPd = titleUrlPd.drop_duplicates(subset=['描述'])
        titleSaveList, urlSaveList, worksIdList = [], [], []
        # 匹配
        for miaosu in miaosuList:
            for miaosu_ in miaosu:
                miaosuBool = True
                for _, data in titleUrlPd.iterrows():
                    dataName = data[0]
                    dataUrl = data[1]
                    # 当前标题是否匹配
                    if dataName.find(miaosu_) != -1:
                        titleSaveList.append(miaosu_)
                        urlSaveList.append(f'https://huaban.com/pins/{dataUrl}')
                        worksIdList.append(self.worksIdDict[miaosu_])
                        (pd.DataFrame({'作品ID': worksIdList, '描述': titleSaveList, '链接': urlSaveList})).to_excel(
                            fr"{FILE_PATH_DICT['站酷花瓣']}\花瓣.xlsx", index=False)
                        miaosuBool = False
                        break
                # 未能找到的
                if miaosuBool:
                    titleSaveList.append(miaosu_)
                    urlSaveList.append('失败')
                    worksIdList.append(self.worksIdDict[miaosu_])
                    (pd.DataFrame({'作品ID': worksIdList, '描述': titleSaveList, '链接': urlSaveList})).to_excel(
                        fr"{FILE_PATH_DICT['站酷花瓣']}\花瓣.xlsx", index=False)

        # 排序
        data = pd.read_excel(fr"{FILE_PATH_DICT['站酷花瓣']}\花瓣.xlsx", dtype={'作品ID': int})
        data = data.sort_values(by='作品ID', ascending=True)
        data.to_excel(fr"{FILE_PATH_DICT['站酷花瓣']}\花瓣.xlsx", index=False)


def Get_Image_Size():
    """
    1、获取图片物理占用

    :return:
    """

    from PIL import Image
    # os.chdir(FILE_PATH_DICT['站酷花瓣图片下载地址'])
    os.chdir(FILE_PATH_DICT['无水印图片'])
    # 修改的宽度
    img_daxiao = [1920, 1080, 720, 480]
    # 遍历文件夹下的所有图片
    for file_name_list in os.walk('.'):
        for i in file_name_list[2]:
            # 初始化
            with open(i, 'rb') as f:
                # 物理大小
                size = len(f.read())
            # 循环检测图片是否符合要求
            for img_daxiao_ in img_daxiao:
                # 最大5MB，超过将进行修改
                if size / 1e6 > float(5):
                    img = Image.open(i)
                    (w, h) = img.size
                    wt = img_daxiao_
                    ht = int(h * wt / w)
                    img_ = img.resize((wt, ht), Image.ANTIALIAS)
                    img_.save(i, quality=100)
                    # 检查图片大小是否符合要求
                    with open(i, 'rb') as f:
                        size = len(f.read())
                    if size / 1e6 > float(5):
                        continue
                    else:
                        print('已修改')
                        break
                else:
                    break


def Mouse_Move(requestsImgTh: threading.Thread):
    """
    1、控制鼠标上传

    :param requestsImgTh: 图片下载线程
    :return:
    """

    # 等待图片下载
    requestsImgTh.join()
    Get_Image_Size()

    # 控制
    pag.moveTo(1000, 600, duration=0.8)
    pag.click(1000, 600)
    time.sleep(0.5)

    # pyperclip.copy(FILE_PATH_DICT['站酷花瓣图片下载地址'])
    pyperclip.copy(r'G:\2345下载 - 副本'+f'\{worksNameStr}.jpg')
    pag.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(1)
    pag.moveTo(900, 500, duration=0.8)
    pag.click(900, 500)
    # time.sleep(0.5)
    # pag.hotkey('ctrl', 'a')
    # time.sleep(0.5)
    # pag.moveTo(1200, 635, duration=0.8)
    # pag.click(1200, 635)
    time.sleep(8)


def Image_Direction() -> bool:
    """
    1、获取图片的方向

    :return:
    """

    # 获取图片方向
    xyBool = True
    os.chdir(FILE_PATH_DICT['站酷花瓣图片下载地址'])
    # 批量识别二维码
    for file_name_list in os.walk('.'):
        for i in file_name_list[2]:
            try:
                # 加载文件路径下的图片
                img = cv2.imread(i)
                # 获取高和宽
                img_wh = img.shape
                # 判断为纵向图片
                if img_wh[0] > img_wh[1]:
                    xyBool = True
                # 判断为横向
                elif img_wh[0] < img_wh[1]:
                    xyBool = False
                else:
                    pass
            except Exception:
                logging.info(f'读取{i}失败')
                continue

    return xyBool


def Image_Segmentation(imageFilePath: str, imageFileSavePath: str, segmentationIndex: int = 2):
    """
    1、图片分割

    :param imageFilePath: 图片文件路径
    :param imageFileSavePath: 图片保存目录路径
    :param segmentationIndex: 分割次数
    :return:
    """

    # 读取图片
    try:
        img = Image.open(imageFilePath)
    except Exception:
        return '打开图片失败'
    # 图片高度
    imgWidth, imgHeight = img.size
    # 累加高度
    heightSum = 0
    # 平均高度
    heightAverage = int(imgHeight / segmentationIndex) - 2
    # 图片名称
    imgNewName = 0
    for i in range(segmentationIndex):
        # 分割
        if i == 0:
            img2 = img.crop((0, heightSum, imgWidth, heightAverage))
        else:
            img2 = img.crop((0, heightSum, imgWidth, heightAverage + heightSum))
        img2.save(fr'{imageFileSavePath}\{str(imgNewName)}.jpg', quality=100)
        # 累加高度
        heightSum += heightAverage
        imgNewName += 1
    img.close()
    del img


def Img_Remove():
    """
    1、删除图片

    :return:
    """

    os.chdir(FILE_PATH_DICT['站酷花瓣图片下载地址'])
    for file in os.listdir('.'):
        fileName = fr"{FILE_PATH_DICT['站酷花瓣图片下载地址']}\{file}"
        # 判断是不是文件
        if os.path.isfile(fileName):
            try:
                os.remove(fileName)
            except Exception:
                logging.info(f'删除该图片失败：{fileName}')
                input()
                sys.stdout.flush()


FILE_PATH_DICT = {
    '浏览器程序': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '站酷花瓣': r'G:\站酷_花瓣',
    '站酷花瓣图片下载地址': r'G:\站酷_花瓣\IMG',
    '二维码去除': r'G:\站酷_花瓣\QR_code',
    '站酷用户': r'F:\Selenium_UserData\zcool',
    '花瓣用户': r'F:\Selenium_UserData\huaban',
    '无水印图片': r'G:\2345下载 - 副本'
}

if __name__ == '__main__':
    # a = ZcoolClass()
    # startId = 6457
    # # , ['18027112900', 'Mingdong1314..']
    # for userName, userPass in [['18613118817', 'mingdongman2022']]:
    #     # 请求数据
    #     successData = IllustrationWorkClassAPI().Query(articleIdInt=startId + 1, inquireIndex=100, arcrankInt=0)
    #
    #     #从这里开始对比
    #
    #
    #     if isinstance(successData, str):
    #         logging.info(f'请求失败：{successData}')
    #
    #     # 发布作品
    #     a.Zcool(userName, userPass, successData, False)
    #     # 获取作品链接
    #     # a.Zcool(userName, userPass, successData, True)
    #
    #     # 只发一个账号
    #     break

    a = HuaBanClass()
    startId = 6320
    for userName, userPass in [['18613118817', 'mingdongman2022']]:
        # 请求数据
        successData = IllustrationWorkClassAPI().Query(articleIdInt=startId + 1, inquireIndex=20, arcrankInt=0)
        if isinstance(successData, str):
            logging.info(f'请求失败：{successData}')

        # 发布作品
        a.Huaban(userName, userPass, successData, False)
        # 获取作品链接
        # a.Huaban(userName, userPass, successData, True)

        # 只发一个账号
        break

    # pass
