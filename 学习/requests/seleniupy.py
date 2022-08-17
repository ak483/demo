# -*- codeing = utf-8 -*-
# @Time :2022/5/27 11:53
# @Author:Eric
# @File : seleniupy.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
#调用键盘按键操作时需要引入的keys包
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# 尝试传参
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)


driver.get('https://www.dangdang.com/')
# driver.quit()


# # # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# driver = webdriver.Chrome("./chromedriver.exe")
# # # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
# driver.get("https://www.dangdang.com/")

key = driver.find_element(By.ID,"key_S")
key.send_keys("科幻")



search = driver.find_element(By.CSS_SELECTOR,".search .button")
search.click()

#循环页数
for i in range(1):
#获得元素
    shoplist = driver.find_elements(By.CSS_SELECTOR,".shoplist li")
    print(shoplist)
 #解析元素
    for li in shoplist:

        print ("标题：",li.find_element(By.CSS_SELECTOR,"a").get_attribute("title"))
        print ("价格：",li.find_element(By.CSS_SELECTOR,".search_now_price").text)
        print ("作者：",li.find_element(By.CSS_SELECTOR,".search_book_author").text)
        print("评论数：", li.find_element(By.CSS_SELECTOR, ".search_comment_num").text)
       # print("出版社：", li.find_element(By.CSS_SELECTOR, ".search_now_price").text)

#点击
    next = driver.find_element(By.LINK_TEXT,"下一页")
    next.click()



