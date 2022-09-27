import time,re
import pandas as pd
from selenium.webdriver.common.by import By
import pyautogui,xlwt




FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
}
from My_code.Toolbox.Selenium import seleniumClass
driver = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.zhihu.com/people/6-81-43-43/posts")
print('搜狐登录')




# driver.execute_script("arguments[0].scrollIntoView();", element)
# driver.execute_script('window.scrollBy(0,1000)')
# driver.execute_script('document.getElementById("block6").scrollIntoView()')
# driver.execute_script("arguments[0].scrollIntoView({block:'center',inline:'center'})", job)
driver.implicitly_wait(10)

data_list=[]
for i in range(45):

    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    time.sleep(1)
    data = driver.page_source

    data_list.append(data)

    time.sleep(3)

    try:
        driver.find_element(By.XPATH,'//button[contains(@class,"PaginationButton-next")]').click()

    except:
        print('没有发现元素')

    pyautogui.press('F5')

data_list = (''.join(data_list))
# print(data_list)

ti = '"Title">(.*?)</a>'
title = re.findall(ti, data_list, re.S)

hr = '<a href="//zhuanlan.zhihu.com/p/(.*?)"'
href = re.findall(hr, data_list, re.S)



a = pd.DataFrame(title)
a.to_excel('知乎标题绘课评1.xls', sheet_name='绘课评')

b = pd.DataFrame(href)
b.to_excel('知乎链接绘课评1.xls', sheet_name='绘课评')


