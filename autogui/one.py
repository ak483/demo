# -*- codeing = utf-8 -*-
# @Time :2022/7/14 23:33
# @Author:Eric
# @File : one.py
# @Software: PyCharm
import pyautogui
# screen = pyautogui.size()
# mouse = pyautogui.position()
# print(mouse)
#
# pyautogui.moveTo(10,100)
# pyautogui.moveRel(xOffset=100,yOffset=80,duration=3)
msg = pyautogui.alert(text='这是alert！',title = 'Alert',button='ok')
print(msg)