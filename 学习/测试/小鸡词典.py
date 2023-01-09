import PIL
import time
import numpy
import tqdm
import random
import parsel
import requests
import wordcloud
import matplotlib.pyplot as plt
from urllib.parse import quote

header = {
    'Host': 'jikipedia.com',
    'Connection': 'keep-alive',
    'Origin': 'https://jikipedia.com',
    'Referer': 'https://jikipedia.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Cookie': '填写自己的 Cookies '
}
proxy = ['HTTP://117.114.149.66:55443',
        'HTTP://112.14.47.6:52024',
        'HTTP://61.164.39.68:53281',
        'HTTP://121.13.252.61:41564',
        'HTTP://61.216.156.222:60808',
        'HTTP://222.74.73.202:42055',
        'HTTP://27.42.168.46:55481',
        'HTTP://121.13.252.60:41564',
        'HTTP://121.13.252.58:41564',
        'HTTP://121.13.252.62:41564',
        'HTTP://183.236.232.160:8080',
        'HTTP://61.216.185.88:60808',
        'HTTP://210.5.10.87:53281'
         ]

data = {}
num1 = 100


def request(num2, url):
    try:
        proxies = {'http': random.choice(proxy)}
        r = requests.get(url=url, headers=header, proxies=proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r
    except:
        pass
        # warning(num2, 0)


def fun(num2, url):
    likes = []
    try:
        time.sleep(3)
        html = request(num2, url).text
        words = parsel.Selector(html).xpath('//a[@class="card-content"]//strong/text()').extract()
        like_html = parsel.Selector(html).xpath('//div[@class="like button hoverable"]').extract()
        for li in like_html:
            like = parsel.Selector(li).xpath('//div/text()').extract()[-1]
            if like != ' ':
                likes.append(like)
            else:
                likes.append(0)
        for num in range(20):
            data[words[num]] = int(likes[num])
    except:
        pass
        # warning(num2, 0)


def draw():
    mask1 = numpy.array(PIL.Image.open('C:/Users/Adminitrator03/Desktop/艾莎.jpg'))
    wcloud = wordcloud.WordCloud(background_color='white', mask=mask1, font_path='‪C:/Windows/Fonts/STXINGKA.TTF')
    wcloud.generate_from_frequencies(frequencies=data)

    plt.figure(dpi=1200)
    plt.imshow(wcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def warning(num1, flag=1):  # 0  失败    1  成功
    par = {"num": str(num1)}
    if flag == 1:
        temp = '477464252017283072'
    else:
        temp = '477464742239145984'
    Parameters = {
        'secretKey': '**************************',
        'appCode': '477462730265071616',
        'templateCode': temp,
        'params': quote(str(par))
    }
    URL = 'https://api.******.com/api/alarm'
    r = requests.get(URL, params=Parameters)
    print(r.text)


if __name__ == '__main__':
    url = 'https://jikipedia.com/'
    for num in tqdm.tqdm(range(num1),desc="正在统计："):
        fun(num, url)
    # warning(num1)
    draw()
