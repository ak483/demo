import re, os, time, logging, shutil, sys, random, cv2, threading, pyperclip
import pandas as pd
import pyautogui as pag
from prettytable import PrettyTable
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(r'D:\untitled1')
from My_code.Toolbox.Selenium import seleniumClass
from My_code.Toolbox.Compression_File import Compression_File_, Compression_File_Password
from My_code.Toolbox.Byte_Conversion import Byte_Conversion
from My_code.名动漫.Mdm_API import SectionClassAPI, EntryAPI

FILE_PATH_DICT = {
    # 本地
    '公用路径2': r'\\Hwindows\公用2',
    '本地资源': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Resource',
    '视频图片保存路径': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Tutorial\image',
    '视频截屏保存路径': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Tutorial',
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置':r'G:\Selenium_UserData\Mdm\one',
    '百科词条': r'\\Win-pp19bi8ic9t\g\流量部\官网改版\绘画自学&社区&百科\内容储备\百科\百科词条.xlsx',
    '共享盘资源': r'C:\Users\Adminitrator03\Desktop\baike',

}


mainExcelDict = pd.read_excel(
    FILE_PATH_DICT['百科词条'], sheet_name=[
        'ACGN百科'
    ]
)
mainExcelData = mainExcelDict['ACGN百科']

# 筛选
mainExcelData = mainExcelData[(mainExcelData['发布状态'] == 2)]

titleList = mainExcelData['词条名称'].to_list()

def Selenium_Control():


    def Move(imgPath: str):
        pyperclip.copy(imgPath)
        if os.path.isdir(imgPath):
            pag.moveTo(1000, 600, duration=0.5)
            pag.click(1000, 600)
            pag.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pag.press('enter')
            time.sleep(1)
            pag.moveTo(900, 500, duration=0.5)
            pag.click(900, 500)
            time.sleep(0.5)
            pag.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pag.moveTo(1200, 635, duration=0.5)
            pag.click(1200, 635)
        else:
            pag.moveTo(1000, 600, duration=0.5)
            pag.click(1000, 600)
            pag.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pag.press('enter')

    # 实例化浏览器
    seleniumClass_ = seleniumClass()
    browser = seleniumClass_.Selenium_Initialization_Chrome(chromeExe=FILE_PATH_DICT['浏览器驱动'])

    # 登录
    browser.get('https://admin4fg.mingdongman.com/#/wenda/question')
    browser.maximize_window()
    time.sleep(2)
    # 用户名
    browser.find_element(By.XPATH, '//input[@placeholder="用户名"]').send_keys('mahongye')
    time.sleep(1)
    # 密码
    browser.find_element(By.XPATH, '//input[@placeholder="密码"]').send_keys('mahy0725')
    time.sleep(1)
    logging.info(f'等待输入验证码（手动点击登录）...')
    while True:
        try:
            WebDriverWait(browser, 15, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(text(),"名动后台管理系统")]')))
            break
        except Exception:
            continue

    time.sleep(3)
    browser.find_element(By.XPATH, '//span[contains(text(),"百科列表")]/../../..').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//span[contains(text(),"百科列表")]').click()
    time.sleep(3)

    # 浏览器
    for i in range(len(titleList)):
        # 标题

        # 百科图片路径
        coverPath = rf"{FILE_PATH_DICT['共享盘资源']}\{titleList[i]}.jpg"


        # 点击编辑
        ActionChains(browser).move_to_element(
            browser.find_element(By.XPATH,
                                 f'//div[@class="el-table__fixed-right"]//div[contains(text(),"{titleList[i]}")]')).perform()
        browser.find_element(By.XPATH,
                             f'//div[@class="el-table__fixed-right"]//div[contains(text(),"{titleList[i]}")]/../../td[last()]/div/button[1]').click()
        time.sleep(2)

        # 上传封面图
        browser.find_element(By.XPATH, '//div[@class="el-upload el-upload--picture"]//button').click()
        time.sleep(2)
        Move(coverPath)
        time.sleep(3)

        # 内容页
        browser.find_element(By.XPATH, '//div[@class="el-dialog__body"]//div[@class="el-tabs__nav-scroll"]/div/div[2]').click()
        time.sleep(2)

        # 上传图片
        browser.find_element(By.XPATH, '//button[@aria-label="多图片上传"]').click()
        time.sleep(2)
        browser.switch_to.frame(browser.find_element(By.XPATH, '//div[@class="tox-navobj"]/iframe'))
        time.sleep(0.5)
        browser.find_element(By.XPATH, '//button[@class="addfile primary"]').click()
        time.sleep(2)
        Move(coverPath)
        time.sleep(3)
        browser.find_element(By.XPATH, '//button[@class="upall primary"]').click()
        time.sleep(5)
        browser.switch_to.default_content()
        browser.find_element(By.XPATH, '//button[@title="保存"]').click()
        time.sleep(2)
        pag.press('enter')
        # pag.press('space')

        # 确定
        browser.find_element(By.XPATH, '//div[@class="el-dialog__footer"]//button[2]').click()
        time.sleep(2)
        browser.refresh()
        time.sleep(2)

# selenium控制
Selenium_Control()

