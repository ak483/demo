# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time,re
import pandas as pd

FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
}
from My_code.Toolbox.Selenium import seleniumClass
driver = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://mp.sohu.com/profile?xpt=MWQ3MmMyZTktMDhkMy00N2I4LThmZTUtOGRjYmQ3YmRmMmE4")
print('搜狐登录')



time.sleep(5)


# driver.execute_script("arguments[0].scrollIntoView();", element)
# driver.execute_script('window.scrollBy(0,1000)')
# driver.execute_script('document.getElementById("block6").scrollIntoView()')
# driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center'})", job)

for i in range(20):
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


time.sleep(5)

data = driver.page_source
print(data)

hr = 'href="(.*?)"'
href = re.findall(hr, data, re.S)
print(href)

a = pd.DataFrame(href)
a.to_excel('未清洗搜狐链接1.xls', sheet_name='极画教育')


# a="https://www.sohu.com/a/"
#
# hrefs=[x for x in href if a in x]
# # d=[y for y in (a+b) if y not in c]
# print(hrefs)
#
#
# b = pd.DataFrame(hrefs)
# b.to_excel('搜狐链接.xls', sheet_name='极画教育')
#
#
#
# input('回车结束')





