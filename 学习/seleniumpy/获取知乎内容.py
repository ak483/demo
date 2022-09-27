import time,re,pyperclip
import pandas as pd
from selenium.webdriver.common.by import By
import pyautogui,xlwt
import pyautogui as pag



FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
}
from My_code.Toolbox.Selenium import seleniumClass
driver = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
driver.implicitly_wait(10)
driver.maximize_window()


mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\学习\seleniumpy\知乎标题绘课评1.xls',sheet_name=[
        '绘课评'
    ])

href = (mainExcelDict['绘课评'])['链接'].to_list()



href_list=[]
for i in range(len(href)):

    href_list.append('https://zhuanlan.zhihu.com/p/'+str(href[i]))

driver.get("https://zhuanlan.zhihu.com/p/529561428")

last_contents=[]
for i in range(len(href_list)):


    data = driver.page_source


    print(data)

    print('--------------------------------------------')
    # content_temp=re.findall('data-pid(.*？)>', data, re.S)
    try:
        content = re.findall('data-first-child="" (.*?)</p></div>', data, re.S)
    except:
        print('contents不行')
        print(href_list[i])
        last_contents.append(' ')
        pag.moveTo(700, 50, duration=0.8)
        pag.click(700, 50)

        pyperclip.copy(href_list[i])
        time.sleep(0.5)
        pag.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pag.press('enter')
        continue
        continue


    print(content)
    # contents = re.sub('<figure.*?<figcaption>', '', content[0])

    try:
        contents = re.sub('<figure.*?<figcaption>', '', content[0])
    except:
        print('contents不行')
        print(href_list[i])
        last_contents.append(' ')

        pag.moveTo(700, 50, duration=0.8)
        pag.click(700, 50)

        pyperclip.copy(href_list[i])
        time.sleep(0.5)
        pag.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pag.press('enter')
        continue


#按/p进行切割
    contentss=(contents.split('</p>'))

    #切割开头的字符串
    contentss[0] = re.sub('data-pid=".*?">', '', contentss[0])
    contentssss=[]
    for j in range(len(contentss)):
        contentsss = re.sub('<.*?>', '', contentss[j])
        contentssss.append(contentsss)

        contentssss[j]=contentssss[j]+'\n'


    last_content=(''.join(contentssss))
    print('href_list')
    print(last_content)
    last_contents.append(last_content)


#移动浏览器
    pag.moveTo(700, 50, duration=0.8)
    pag.click(700, 50)


    pyperclip.copy(href_list[i])
    time.sleep(0.5)
    pag.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pag.press('enter')

savepath = "绘课评内容.xls"

book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet('知乎', cell_overwrite_ok=True)
col = ("链接")
for i in range(0, 1):
    sheet.write(0, i, col[i])  # 列名
for i in range(0, len(last_contents)):
    print("第%d条" % (i + 1))
    sheet.write(i + 1, 0, last_contents[i])
book.save(savepath)  # 保存