import asyncio
from pyppeteer import launch
import time
import tkinter
import requests

headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'
}

def screen_size():
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return {'width': width, 'height': height}

async def main():
    browser = await launch(headless=False,ignoreDefaultArgs=['--enable-automation'],args=['--start-maximized'])

    page = await browser.newPage()
    await page.setViewport(screen_size())
    url = 'https://sf.taobao.com'
    await page.goto(url)
    #time.sleep(5)
    await page.waitForNavigation()


    print(await page.content())
    #content = await page.content()
    # content = await page.evaluate('document.body.textContent', force_expr=True)
    #print(content)
    # content = await page.evaluate('document.body.textContent', force_expr=True)
    # print(content)




asyncio.get_event_loop().run_until_complete(main())

