# coding=utf-8
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

def Mouse_Move():

    # 控制
    pag.moveTo(1000, 600, duration=0.8)
    pag.click(1000, 600)
    time.sleep(0.5)

    pyperclip.copy(r'G:\2345下载 - 副本'+f'\{worksNameStr}.jpg')
    pag.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(1)
    pag.moveTo(900, 500, duration=0.8)
    pag.click(900, 500)

    print("经过Mouse_Move")
    # time.sleep(0.5)
    # pag.hotkey('ctrl', 'a')
    # time.sleep(0.5)
    # pag.moveTo(1200, 635, duration=0.8)
    # pag.click(1200, 635)
    time.sleep(8)

class HuaBanClass:

    def __init__(self):
        # 描述对应作品ID
        self.worksIdDict = {}


    def Huaban(self, userName: str, userPass: str, worksDataList: list, getImgUrl=False):



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

        input('上传完毕，是否退出：')

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

    def Works(self, browser: webdriver.Chrome, worksDataDict: dict, getImgUrl=False) -> [str]:

         # 作品名称
        global worksNameStr
        worksNameStr = str(worksDataDict['nameStr'])
        categoryStr_ = str(worksDataDict['categoryStr'])
        worksNameStrr = f'{worksNameStr}' + f'({categoryStr_})'
        self.worksIdDict[worksNameStrr] = int(worksDataDict['idInt'])
        if getImgUrl:
            return worksNameStrr
        # 添加单个作品
        logging.info(f'当前作品ID为：{worksDataDict["idInt"]}')


        miaosuList, urlList, huaBanList = [], [], []

        worksClassData = str(worksDataDict['categoryStr'])
        if worksClassData == '商业插画':
             worksClass_ = '插画'
             worksClass__ = '商业插画'
        elif worksClassData == 'CG美术基础':
             worksClass_ = '插画'
             worksClass__ = 'CG美术基础'
        elif worksClassData == '角色原画':
             worksClass_ = '插画'
             worksClass__ = '角色原画'
        elif worksClassData == '场景概念':
             worksClass_ = '插画'
             worksClass__ = '场景概念'
        elif worksClassData == 'CG漫画':
             worksClass_ = '动漫'
             worksClass__ = 'CG漫画'
        elif worksClassData == '游戏UI':
             worksClass_ = '游戏UI'
             worksClass__ = '游戏UI'
        elif worksClassData == '3D模型':
             worksClass_ = '三维'
             worksClass__ = '其他三维'

        else:
             logging.info(f'没有找到该分类画板：')
             worksClass__ = ''

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

        Mouse_Move()
        time.sleep(2)

        # 选择画板
        try:
            # 当前画板与需要选择的画板不一致
            if str(browser.find_element(By.XPATH,'//div[contains(@class,"__3ahyndY3 dy9VYUod")]/div/div/span[2]').get_attribute('title')) != worksClass__:
                browser.find_element(By.XPATH,'//div[contains(@class,"__3ahyndY3 dy9VYUod")]/div/div/span[2]').click()
                time.sleep(1)
                ActionChains(browser).move_to_element(
                    (browser.find_elements(By.XPATH,f'//div[text()="{worksClass__}"]'))[-1]
                ).perform()
                browser.find_element(By.XPATH,f'//div[text()="{worksClass__}"]').click()
                time.sleep(1)
        except Exception:
            logging.info(worksClass__)
            logging.info('花瓣上传图片有问题 或 选择画板有问题：请手动选择画板')
            input('继续：')
            sys.stdout.flush()
            time.sleep(2)



        # 添加描述
        imgIndex = 1

        try:
            # 添加描述
            str_explainStr = str(worksDataDict['explainStr'])
            str_explainStr = re.sub('名动漫', '', str_explainStr)
            browser.find_element(By.XPATH, '//*[@placeholder="填写作品相关的描述"]').send_keys(str_explainStr)
            time.sleep(1)

        except Exception:
            try:
                pprint.pprint(str_explainStr)
            except IndexError:
                pass

            logging.info('添加描述失败 -> 手动添加')
            input('继续：')
            sys.stdout.flush()
            time.sleep(2)

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

        return worksNameStrr



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

    a = HuaBanClass()
    startId = 6340
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
