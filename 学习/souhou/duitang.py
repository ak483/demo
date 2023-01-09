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
    pag.moveTo(1000, 600)
    time.sleep(3)
    pag.click(1000, 600)
    time.sleep(1)

    pyperclip.copy(r'G:\2345下载 - 副本'+f'\{worksNameStr}.jpg')
    time.sleep(1)
    pag.hotkey('ctrl', 'v')
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    # pag.moveTo(900, 500, duration=0.8)
    # pag.click(900, 500)

    print("经过Mouse_Move")
    # time.sleep(0.5)
    # pag.hotkey('ctrl', 'a')
    # time.sleep(0.5)
    # pag.moveTo(1200, 635, duration=0.8)
    # pag.click(1200, 635)
    time.sleep(8)


class DuiTangClass:
    def __init__(self):
        # 描述对应作品ID
        self.worksIdDict = {}

    def Duitang(self, userName: str, userPass: str, worksDataList: list, getImgUrl=False):

        # 登录
        browser = self.Selenium_Login(userName, userPass)

        # 返回的标题
        titleList = []
        # 作品ID
        idList = []
        # 发布
        for worksDataDict in worksDataList:

            # 如果没有图片则跳过
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

        browser = Selenium.seleniumClass().Selenium_Initialization_Chrome(chromeExe=FILE_PATH_DICT['浏览器程序'], chromeUser=FILE_PATH_DICT['花瓣用户'])

        browser.maximize_window()
        browser.get('https://www.duitang.com/')
        # 已登录退出
        input('请登录')

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

        #标签
        Key_List = worksDataDict['labelsList']

        worksClassData = str(worksDataDict['categoryStr'])
        if worksClassData == '商业插画':
            worksClass__ = '商业插画'
        elif worksClassData == 'CG美术基础':
            worksClass__ = 'CG美术基础'
        elif worksClassData == '角色原画':
            worksClass__ = '角色原画'
        elif worksClassData == '场景概念':
            worksClass__ = '场景概念'
        elif worksClassData == 'CG漫画':
            worksClass__ = 'CG漫画'
        elif worksClassData == '游戏UI':
            worksClass__ = '游戏UI'
        elif worksClassData == '3D模型':
            worksClass__ = '3D模型'
        else:
            logging.info(f'没有找到该分类画板：')
            worksClass__ = ''


        # 点击发布
        while True:
            ActionChains(browser).move_to_element(browser.find_element(By.XPATH, '//*[@id="dt-add"]/a')).perform()
            time.sleep(2)
            try:
                browser.find_element(By.XPATH, '//*[@class="icon-add"]').click()
                # WebDriverWait(browser, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="blockUI blockMsg blockPage"]/div')))
                break
            except Exception:
                continue
        time.sleep(2)
        # 点击上传
        browser.find_element(By.XPATH, '//*[@id="sgcoll-upbtn"]').click()
        time.sleep(0.8)

        # 操控电脑鼠标
        Mouse_Move()
        time.sleep(2)

        try:
            # 点击专辑
            browser.find_element(By.XPATH,'//*[@id="sgcoll-albumsel"]/a').click()
        except Exception as e:
            print(e)
            input('未知问题 手动上传图片')
            time.sleep(3)
        time.sleep(1)

        try:
            browser.find_element(By.XPATH, '//*[@id="myalbums-albs"]/a[text()="{}"]'.format(worksClass__)).click()
        except Exception:
            print('点击专辑失败')
            print('请手动点击专辑')
            print('当前专辑：{}'.format(worksClass__))
            input()
            time.sleep(2)
        time.sleep(1)

        # 添加描述
        try:
            str_explainStr = str(worksDataDict['explainStr'])
            str_explainStr = re.sub('名动漫', '', str_explainStr)
            browser.find_element(By.XPATH, '//*[@id="sgcoll-txa"]').send_keys(str_explainStr)
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

        # 添加标签
        for j in range(len(Key_List[:10])):
            if Key_List[j] != '' and str(Key_List[j]) != 'None':
                browser.find_element(By.XPATH,'//*[@id="sgcoll-tags-inp"]').send_keys(Key_List[j])
                time.sleep(0.5)


                pag.press('enter')


        time.sleep(1)

        try:
            # 发布
            browser.find_element(By.XPATH, '//*[@id="sgcoll-abtnpost"]').click()
        except Exception:
            print('点击发布失败（OK后点击发布)')
            input()
            print('好的')
        try:
            # 关闭发布成功页面
            WebDriverWait(browser, 20, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="mask-body width-full"]/div/a')))
            browser.find_element(By.XPATH,'//div[@class="mask-body width-full"]/div/a').click()
        except Exception:
            print('点击X失败(OK后点击X)')
            input()
            print('好的')

        # 获取图片链接

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

    a = DuiTangClass()
    startId = 6880
    for userName, userPass in [['18613118817', 'mingdongman2022']]:
        # 请求数据
        successData = IllustrationWorkClassAPI().Query(articleIdInt=startId + 1, inquireIndex=100, arcrankInt=0)
        if isinstance(successData, str):
            logging.info(f'请求失败：{successData}')

        # 发布作品
        a.Duitang(userName, userPass, successData, False)
        # 获取作品链接
        # a.Huaban(userName, userPass, successData, True)

        # 只发一个账号
        break
