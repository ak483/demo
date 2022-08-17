from selenium import webdriver
from selenium.webdriver.common.by import By
import json, time
# 百度用户登录并保存登录Cookies
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element(By.XPATH,'//*[@id="u1"]/a[7]').click()
time.sleep(3)
driver.find_element(By.ID,'TANGRAM__PSP_10__footerULoginBtn').click()
time.sleep(3)
# 设置用户的账号和密码
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_10__userName"]').send_keys('XXXX')
driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_10__password"]').send_keys('XXXX')
try:
    verifyCode = driver.find_element(By.NAME,'verifyCode')
    code_number = input('请输入图片验证码：')
    verifyCode.send_keys(str(code_number))
except: pass

driver.find_element(By.XPATH,'//*[@id="TANGRAM__PSP_10__submit"]').click()
time.sleep(3)
try:
    driver.find_element(By.XPATH,'//*[@id="TANGRAM__36__button_send_mobile"]').click()
    code_photo = input('请输入短信验证码：')
    driver.find_element(By.XPATH,'//*[@id="TANGRAM__36__input_vcode"]').send_keys(str(code_photo))
    driver.find_element(By.XPATH,'//*[@id="TANGRAM__36__button_submit"]').click()
    time.sleep(3)
except: pass
cookies = driver.get_cookies()
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookies))
f1.close()