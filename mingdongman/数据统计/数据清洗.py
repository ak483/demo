import re

douyin_data = '2022年09月05日 19:37'
kuaishou_data = '发布于 2022-09-05 19:37:47'
xiaohongshu_data = '发布于 2022-09-05'
shipinhao_data = '2022/09/09'
bilibili_data = '20-02-29 02:40:30'

douyin_data = re.sub('年','/',douyin_data)
douyin_data = re.sub('月','/',douyin_data)
douyin_data = re.sub('日.*$','',douyin_data)
print(douyin_data)

kuaishou_data = re.sub('发布于 ','',kuaishou_data)
kuaishou_data = re.sub('-','/',kuaishou_data)
kuaishou_data = re.sub(' .*$','',kuaishou_data)
print(kuaishou_data)

xiaohongshu_data = re.sub('发布于 ','',xiaohongshu_data)
xiaohongshu_data = re.sub('-','/',xiaohongshu_data)
print(xiaohongshu_data)


bilibili_data = re.sub('-','/',bilibili_data)
bilibili_data = re.sub(' .*$','',bilibili_data)
print(bilibili_data)


shipinhao_time = '2.81秒'
shipinhao = re.sub('\..*$','',shipinhao_time)
print(shipinhao)

xiaohongshu_time = '4min'
xiaohongshu_time = re.sub('s','',xiaohongshu_time)
if 'min' in xiaohongshu_time:
    xiaohongshu_time = re.sub('min','',xiaohongshu_time)
    xiaohongshu_time = int(xiaohongshu_time)*60

print(xiaohongshu_time)

