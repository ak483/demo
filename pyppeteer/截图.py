# -*- codeing = utf-8 -*-
# @Time :2022/7/9 11:36
# @Author:Eric
# @File : 截图.py
# @Software: PyCharm
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)  # 关闭无头浏览器
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')  # 跳转
    await page.screenshot({'path': 'example1.png'})  # 截图
    await browser.close()  # 关闭


asyncio.get_event_loop().run_until_complete(main())
