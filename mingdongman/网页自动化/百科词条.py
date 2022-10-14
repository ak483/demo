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

def Selenium_Control():
    """
    1、操作Selenium控制后台

    :return:
    """

    nonlocal addDataDict, mod#不只是对嵌套函数起作用

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
    browser.get('http://new.admin.mingdongman.com/#/login?redirect=%2Findex')
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
    if mod == 'Z' or mod == 'SZ':
        browser.find_element(By.XPATH, '//span[contains(text(),"资源列表")]/../../..').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[contains(text(),"资源列表")]').click()
    elif mod == 'J' or mod == 'SJ':
        browser.find_element(By.XPATH, '//span[contains(text(),"教程列表")]/../../..').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[contains(text(),"教程列表")]').click()
    elif mod == 'BK' or mod == 'BKK':
        browser.find_element(By.XPATH, '//span[contains(text(),"百科列表")]/../../..').click()
        time.sleep(1)
        browser.find_element(By.XPATH, '//span[contains(text(),"百科列表")]').click()
    time.sleep(3)

    # 浏览器
    for _, i in addDataDict.items():
        # 标题
        title = i['title']

        # id
        try:
            id = int(i['id'])
        except Exception:
            # 获取网页中的ID
            id = int(
                (
                    browser.find_element(By.XPATH, f'//div[contains(text(),"{title}")]/../..')
                )[2].find_element(By.XPATH, './td[2]/div').get_attribute('innerHTML')
            )

        # 封面图路径
        if i['cover'] == '':
            if mod == 'Bk' or mod == 'BKK':
                # 资源图片路径
                coverPath = rf"{FILE_PATH_DICT['共享盘资源']}\{title}\{title}.jpg"
            else:
                pass
        else:
            coverPath = i['cover']

        # 内容图片路径
        if mod == 'BK':
            # 目录
            contentImgPath = rf"{FILE_PATH_DICT['本地资源']}\{title}-正文"
        else:
            # 单文件
            contentImgPath = rf"{FILE_PATH_DICT['视频图片保存路径']}\{title}-正文.jpg"


        # 查询原内容做备份
        if mod == 'Bk':
            msg = sectionClassAPI.Query_Resource(resourceId=id, inquireIndex=1)
        else:
            msg = sectionClassAPI.Query_Tutorial(tutorialId=id, inquireIndex=1)
        if isinstance(msg, list):
            sourceContent = msg[0]['contentStr']
        else:
            logging.info(fr'获取资源原内容失败 -> {title} -> {msg}')
            logging.info(fr'是否覆盖？ -> y')
            if str(input()) != 'y':
                sourceContent = input('原内容：')
            else:
                sourceContent = ''
        time.sleep(1)

        # 清除原内容用于上传图片（有内容则清除）
        if sourceContent != '' and sourceContent != '<br />':
            if mod == 'Z' or mod == 'SZ':
                msg = sectionClassAPI.Update_Resource(resourceId=id, contentStr='<br />')
            else:
                msg = sectionClassAPI.Update_Tutorial(tutorialId=id, contentStr='<br />')
            if isinstance(msg, list):
                logging.info(rf'已清空正文内容 -> {id}')
            else:
                logging.info(fr'清空正文内容失败 -> ID：{id} -> 原因：{msg}')
            time.sleep(1)

        # 点击编辑
        ActionChains(browser).move_to_element(
            browser.find_element(By.XPATH,
                                 f'//div[@class="el-table__fixed-right"]//div[contains(text(),"{title}")]')).perform()
        browser.find_element(By.XPATH,
                             f'//div[@class="el-table__fixed-right"]//div[contains(text(),"{title}")]/../../td[last()]/div/button[1]').click()
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
        Move(contentImgPath)
        time.sleep(3)
        browser.find_element(By.XPATH, '//button[@class="upall primary"]').click()
        time.sleep(5)
        browser.switch_to.default_content()
        browser.find_element(By.XPATH, '//button[@title="保存"]').click()
        time.sleep(2)

        # 确定
        browser.find_element(By.XPATH, '//div[@class="el-dialog__footer"]//button[2]').click()
        time.sleep(3)
        browser.refresh()

        # 查询新内容
        if mod == 'Z' or mod == 'SZ':
            sourceContentNew = (sectionClassAPI.Query_Resource(resourceId=id, inquireIndex=1))[0]['contentStr']
        else:
            sourceContentNew = (sectionClassAPI.Query_Tutorial(tutorialId=id, inquireIndex=1))[0]['contentStr']
        time.sleep(1)

        # 原内容与新内容合成并更新
        if mod == 'Z' or mod == 'SZ':
            msg = sectionClassAPI.Update_Resource(resourceId=id, contentStr=f'{sourceContentNew}<br />{sourceContent}')
        else:
            msg = sectionClassAPI.Update_Tutorial(tutorialId=id, contentStr=f'{sourceContentNew}<br />{sourceContent}')
        if isinstance(msg, list):
            logging.info(rf'已更新正文内容 -> {id}')
        else:
            logging.info(fr'更新正文内容失败 -> ID：{id} -> 原因：{msg}')



FILE_PATH_DICT = {
    # 本地
    '公用路径2': r'\\Hwindows\公用2',
    '本地资源': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Resource',
    '视频图片保存路径': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Tutorial\image',
    '视频截屏保存路径': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Tutorial',
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置':r'G:\Selenium_UserData\Mdm\one',
    '资源压缩包': [
        r'\\Desktop-j6ecv53\python_file\资源压缩包\绘画好课推荐.url',
        r'\\Desktop-j6ecv53\python_file\资源压缩包\解压说明.txt',
        r'\\Desktop-j6ecv53\python_file\资源压缩包\快速提升绘画水平.url',
        r'\\Desktop-j6ecv53\python_file\资源压缩包\免费绘画教程资源.url',
    ],
    '百科词条封面': r'\\Desktop-j6ecv53\Users\Adminitrator03\Desktop\词条整理下载后.xlsx',
    '资源教程添加介绍': r'\\Desktop-j6ecv53\Users\Adminitrator03\Desktop\教程资源更新内容.xlsx',
    '教程资源内容查询': r'\\Desktop-j6ecv53\Users\Adminitrator03\Desktop\教程资源内容查询.xlsx',
    # 共享盘
    '画师巴士资源': r'\\Win-pp19bi8ic9t\g\流量部\官网改版\绘画自学&社区&百科\内容储备\资源\官网资源列表.xlsx',
    '共享盘资源': r'\\Win-pp19bi8ic9t\M\画师巴士\资源下载',
    '画师巴士外网视频': r'\\Win-pp19bi8ic9t\g\流量部\官网改版\绘画自学&社区&百科\内容储备\教程\外网教程视频.xlsx',
    '画师巴士外网视频存储': r'\\Win-pp19bi8ic9t\M\画师巴士\视频教程\非原创\外网视频',
    '画师巴士原创教程': r'\\Win-pp19bi8ic9t\g\流量部\官网改版\绘画自学&社区&百科\内容储备\教程\新板块-原创教程视频.xlsx',
    '画师巴士其他原创视频存储': r'\\Win-pp19bi8ic9t\J\官网视频教程\原创视频\其他原创视频',
    '百科词条': r'\\Win-pp19bi8ic9t\g\流量部\官网改版\绘画自学&社区&百科\内容储备\百科\百科词条.xlsx',
}

# selenium控制
Selenium_Control()

