import time,re,xlwt,requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import html
etree = html.etree
import pandas as pd

FILE_PATH_DICT = {
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置': r'G:\Selenium_UserData\Mdm\one',
}
from My_code.Toolbox.Selenium import seleniumClass
browser = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
browser.implicitly_wait(5)

mainExcelDict=pd.DataFrame=pd.read_excel(r'D:\untitled1\demo\Excel杂货间\七麦数据.xlsx',sheet_name=[
        '七麦','1','200','400'
    ])
All_url= (mainExcelDict['400'])['url'].to_list()



def get_info():
    from My_code.Toolbox.Selenium import seleniumClass
    driver = seleniumClass().Selenium_Initialization_Chrome(FILE_PATH_DICT['浏览器驱动'], chromeUser=FILE_PATH_DICT['浏览器个人配置'])
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.qimai.cn/rank/index/brand/free/country/cn/genre/6014/device/iphone")

    input("登录")

    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        try:
            WebDriverWait(driver, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(text(),"没有数据了~")]')))
            time.sleep(3)
            break
        except Exception:
            continue
    data = driver.page_source
    tree = etree.HTML(data)#转化为xpath对象

    #选取元素
    All_neme = tree.xpath('//a[@class="app-name"]')
    All_rank = tree.xpath('//tr[@class="t-tr"]/td[4]//a')
    All_category = tree.xpath('//tr[@class="t-tr"]/td[5]//p[2]')
    All_url = tree.xpath('//tr[@class="t-tr"]//div[@class="app-info"]/a')

    #解析元素

    All_datalist=[]
    for i in range(len(All_neme)):
        data_list = []
        name = (All_neme[i].text).strip()
        rank = (All_rank[i].text).strip()
        category = All_category[i].text
        url = All_url[i].xpath('@href')


        url = re.sub('/app/rank','https://www.qimai.cn/app/baseinfo',url[0])
        #添加元素
        data_list.append(name)
        data_list.append(rank)
        data_list.append(category)
        data_list.append(url)
        All_datalist.append(data_list)

    print(All_datalist)
    return All_datalist

def save(All_datalist):#保存账号数据
    savepath = r'D:\untitled1\demo\Excel杂货间\七麦数据.xlsx'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('七麦', cell_overwrite_ok=True)
    col = ("名称", "游戏榜排名", "分类", "url")

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条" % (i + 1))
        data = All_datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

def save1(All_datalist):#保存账号数据
    savepath = r'D:\untitled1\demo\Excel杂货间\七麦数据信息3.xlsx'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('七麦', cell_overwrite_ok=True)
    col = ("信息")

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        # print("第%d条" % (i + 1))
        # data = All_datalist[i]
        # for j in range(0, len(data)):
        sheet.write(i + 1, 0, All_datalist[i])
    book.save(savepath)  # 保存

def description():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        'refer': 'https://www.qimai.cn/rank/index/brand/free/country/cn/genre/6014/device/iphone',
        'cookie': 'Hm_lvt_ff3eefaf44c797b33945945d0de0e370=1665727096; PHPSESSID=rq6cp9vsk6dn59gfshce75qp70; qm_check=A1sdRUIQChtxen8tJ0NMNi8zcX5zHBl+YnElKyJEPxw8WkVRVRl3YGBBVVZUWC0TFXNbQlxTQAslU1JEDgolAGgCEElDaw0+Uk9EPEo+BAYbEhUSV1AEAQhGQltKGQceABUAGAhDHw%3D%3D; gr_user_id=8076650a-7067-4adf-9891-47c6138821d6; USERINFO=n8ITXCgN1EK21OwwmkS90of7%2B%2FkFNXQShM1M0LTZe%2B2dlHVk8eVZhrC%2FivabRN95zn7JaWqJF451BUr9j7ArcgNdtp7hin%2Ba1x3iCBLQm0J7GyzntDXwm3yTN4Te73qv4BkNiZVJO9FSlzB05LdaNg%3D%3D; ada35577182650f1_gr_last_sent_cs1=qm16597700046; aso_ucenter=e7d12kld9s951c%2BdFj7tECiJ7Y45Nn8GsHbXvedSV5PdWFiZ%2FvbZSj0dbJHKtyIAAuA; AUTHKEY=8jLyUuN0%2FIe0KOyAxVY8mPR%2B7XNNUchM%2BA%2BaHuQLKslFm3UBHjlCGvbbPO9c9Ctv2RT36gG8KvAonYtJui146Gjg9V7ZEVWJfkdNWGuBC%2BMXb7BxXbQjag%3D%3D; synct=1665988190.913; syncd=-1202; Hm_lpvt_ff3eefaf44c797b33945945d0de0e370=1665988192; ada35577182650f1_gr_cs1=qm16597700046'

    }

    url = 'https://www.qimai.cn/app/baseinfo/appid/1637377185/country/cn'

    res = requests.get(url, headers=headers).text
    print(res)

def switch_(url):#url转换
    browser.switch_to.default_content()
    # 获取所有窗口句柄集合
    handles = browser.window_handles
    # 创建页面
    handles = seleniumClass().Create_New_Page(browser=browser, newPageUrl=url)

All_description = []
def selenium_description():

    for i in range(len(All_url)):
        switch_(All_url[i])
        descr = browser.find_element(By.XPATH, '//div[@class="description"]').text
        All_description.append(descr)





if __name__ == '__main__':

    # All_datalist=get_info()
    # save(All_datalist)
    # description()
    selenium_description()
    save1(All_description)






