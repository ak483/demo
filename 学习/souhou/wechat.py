# coding=utf-8
import requests, re, time, os, psutil, getpass, threading, shutil, asyncio, pyperclip, sys, random, logging
from lxml import etree



def Run_Scrapy(url, letterStr):
    """
    1、运行 scrapy 下载图片

    :param url: 链接
    :param letterStr: 用于命名的字母
    :return:
    """

    async def diaoyon(url, letterStr):
        os.system('activate conda_py37')
        os.chdir(FILE_PATH_DICT['scrapy'])
        cmd = f'scrapy crawl ImagesSpider -a mediaSpiderUrl={url} -a imageNameAdditional={letterStr} -a imageDownloadPath={FILE_PATH_DICT["图片下载路径"]} --nolog'
        # input('开始爬取！！！')
        os.system(cmd)

    while True:
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(diaoyon(url, letterStr))]
        dones, pendings = loop.run_until_complete(asyncio.wait(tasks))
        for task in dones:
            task.result()

        if letterStr in [str(i)[0] for i in os.listdir(FILE_PATH_DICT['图片下载路径'])]:
            break
        else:
            logging.info('未能下载微信公众号图片！！！')
            logging.info('即将重新下载！！！')

FILE_PATH_DICT = {

    '运行文件夹': fr'C:\Users\{getpass.getuser()}\Desktop\脚本运行产生的文件',
    '图片下载路径': r'\\Desktop-j6ecv53\img',
    'scrapy': r'D:\untitled1\My_code\NewScrapySpider\ImagesScrapySpider',
    '水印图片路径': r'D:\untitled1\out\shuiyin.png',
    '无水印图片路径': r'\\Hwindows\IMG'
}

if __name__ == '__main__':
    url = 'https://mp.weixin.qq.com/s/WeKovLSRPos6FL2X-fPALg'
    Run_Scrapy(url, 'A')