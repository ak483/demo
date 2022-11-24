from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import json


def browser_initial():
    """"
    进行浏览器初始化
    """
    # options = Options()
    # options.add_experimental_option('useAutomationExtension', False)
    # options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # browser = webdriver.Chrome(options=options)
    # # s = Service("chromedriver.exe")

    browser = webdriver.Chrome()
    log_url = 'https://wx.zsxq.com/dweb2/login'
    return log_url, browser


def get_cookies(log_url, browser):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    # input('扫码')  # 进行扫码
    dictCookies = browser.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

    with open('cookies.txt', 'w') as f:
        f.write(jsonCookies)
    # print('cookies保存成功！')


if __name__ == "__main__":
    tur = browser_initial()
    get_cookies(tur[0], tur[1])
