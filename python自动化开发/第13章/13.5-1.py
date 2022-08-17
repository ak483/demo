from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'deviceName': 'huawei-lld_al20-30KNW18730002140',
    'appPackage': 'com.sankuai.meituan',
    'appActivity': 'com.meituan.android.pt.homepage.activity.MainActivity',
    # 设置中文输入
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
# 向Appium-Server发送请求实现连接
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(3)
# 点击系统提示框
for i in range(2):
    resourceId = 'com.android.packageinstaller:id/permission_allow_button'
    driver.find_element_by_id(resourceId).click()
    time.sleep(3)
# 点击首页输入框
resourceId = 'com.sankuai.meituan:id/search_edit'
driver.find_element_by_id(resourceId).click()
time.sleep(3)
# 输入搜索内容
resourceId = 'com.sankuai.meituan:id/search_edit'
driver.find_element_by_id(resourceId).send_keys('广州长隆')