import pyautogui
import time
import win32clipboard
import win32con
# 向粘贴板发送数据，用于Ctrl + C
def settext(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
    win32clipboard.CloseClipboard()

# 设置点击功能
def mouseClick(image, xoffset=0, interval=1, duration=1):
    x, y = pyautogui.locateCenterOnScreen(image)
    pyautogui.click(x+xoffset, y, interval=interval, duration=duration)
    time.sleep(1)

# 打开浏览器，进入用户账号密码登录界面
mouseClick('chrome.png')
mouseClick('url.png', 100)
pyautogui.typewrite('https://www.baidu.com/', interval=0.1)
pyautogui.hotkey('enter')
time.sleep(2)
mouseClick('login.png')
mouseClick('userLogin.png')

# 输入账号、密码、验证码
while 1:
    try:
        mouseClick('logo.png')
        # 账号
        pyautogui.hotkey('tab')
        username = pyautogui.prompt(text='输入百度账号', title='账号')
        pyautogui.typewrite(username, interval=0.2)

        # 密码
        pyautogui.hotkey('tab')
        pyautogui.hotkey('ctrl', 'a')
        password = pyautogui.password(text='输入百度密码', title='密码', mask='*')
        pyautogui.typewrite(password, interval=0.2)

        # 验证码
        try:
            x, y = pyautogui.locateCenterOnScreen('code.png')
            pyautogui.hotkey('tab')
            code = pyautogui.prompt(text='输入验证码', title='验证码')
            settext(code)
            pyautogui.hotkey('ctrl', 'v')
        except: pass
        # 点击登录按钮
        mouseClick('su.png')
        mouseClick('su.png')
    except:
        print('登录成功')
        break


