from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, pyperclip, sys, re, logging, MySQLdb, random, os
import pyautogui as pag
import pandas as pd

# 输出到文件
# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(funcName)s -> %(message)s',
#                     filename=rf'.\{os.path.splitext(os.path.split(__file__)[1])[0]}.log')
# 输出到屏幕
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(funcName)s -> %(message)s')
console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
sys.path.append(r'D:\untitled1')
from My_code.Toolbox.Selenium import seleniumClass
from My_code.名动漫.Mdm_API import ArticleClassAPI
from My_code.名动漫.Article_Published.Submit_SQL import Submit_Data
from My_code.名动漫.Article_Published.Get_Data_ import Data_Format





def Selenium_Login():
    # 实例化浏览器
    browser = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
    browser.maximize_window()

    browser.get('https://creator.douyin.com/creator-micro/home')
    # browser.get('https://cp.kuaishou.com/profile')
    # browser.get('https://member.bilibili.com/platform/home')
    # browser.get('https://creator.xiaohongshu.com/creator/home')
    # browser.get('https://channels.weixin.qq.com/platform')

    input('知乎登录：')


FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\BaiDu',
    '发布窗口': '',
    '编辑器': '',
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-知乎.xlsx',
    '封面图片路径': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\微信图片_20220518142115.png',
    '标题保存': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\标题2.xlsx',
    '外链列表': r'\\Win-pp19bi8ic9t\g\流量部\自动发布\知乎\知乎-外链建设\外链列表-第一批（官网150个）.xlsx',
    '原文配图': 'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/Fifth_Batch',
    '配图': {
        '3D': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/3D',
        '插画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E5%BD%B1%E8%A7%86',
        '绘画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E7%BB%98%E7%94%BB',
        '漫画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E6%BC%AB%E7%94%BB',
        '素描': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E7%B4%A0%E6%8F%8F',
        '线稿': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E7%BA%BF%E7%A8%BF',
        '影视': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E5%BD%B1%E8%A7%86',
        '游戏UI': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E6%B8%B8%E6%88%8FUI',
        '原画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/%E5%8E%9F%E7%94%BB',
    },
    '配图封面': {
        '3D': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/3D',
        '插画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E5%BD%B1%E8%A7%86',
        '绘画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E7%BB%98%E7%94%BB',
        '漫画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E6%BC%AB%E7%94%BB',
        '素描': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E7%B4%A0%E6%8F%8F',
        '线稿': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E7%BA%BF%E7%A8%BF',
        '影视': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E5%BD%B1%E8%A7%86',
        '游戏UI': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E6%B8%B8%E6%88%8FUI',
        '原画': r'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/coverImage/%E5%8E%9F%E7%94%BB',
    },
}

if __name__ == '__main__':
    MAXINDEX = 5

    Selenium_Login()

    pass
