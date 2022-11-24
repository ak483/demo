import requests
import re,urllib
import xlwt
from lxml import html
etree = html.etree

headers={
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'referer': 'https://www.sogou.com/'
}

url = 'https://mp.weixin.qq.com/s/Dcz4mc7UlXwywvS_xmS9YA'
res = requests.get(url, headers=headers).text
print(res)


imgs = re.findall('cdn_url: \'(.*?)\'',res)
print(imgs)
x= 0
paths = r'D:\untitled1\demo\学习\seleniumpy'+'\\'
for i in range(len(imgs)):
    # filename = str(i) + '.jpg'
    # response1 = requests.get(imgs[i],headers=headers)#访问图片url内容
    # bytes_data = response1.content#获取图片url内容
    # with open(filename,'wb')as f:
    #     f.write(bytes_data)


    urllib.request.urlretrieve(imgs[i],'{0}{1}.jpg'.format(paths,x))  #打开imglist中保存的图片网址，并下载图片保存在本地，format格式化字符串
    x = x + 1