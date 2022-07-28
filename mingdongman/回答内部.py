# -*- codeing = utf-8 -*-
# @Time :2022/7/20 19:51
# @Author:Eric
# @File : 回答内部.py
# @Software: PyCharm
import requests
import re
from lxml import etree

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

def yutu():

    for q in range(1):
        qr = requests.get(url='https://www.yutu.cn/question/tiwen_160154.html', headers=headers)
        qr.encoding = 'utf-8'
        ress = qr.text
        tree = etree.HTML(ress)
        answer = []
        print(ress)

       #提取元素并清除空列表以及列表元素为空格
        div_list = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/p')
        # descript = tree.xpath('/html/head/meta[6]/@content')
        # print(descript)
        answerlist1=[]
        for p in div_list:
            # answer_t = p.xpath('./span/text()')
            # print(answer_t)
            # answer.append(answer_t[0])
            answer_t = p.xpath('./text()')
            # print(answer_t)
            # answer.append(answer_t[0])
            # print(answer)
            if len(answer_t) == 0:
                del answer_t
            elif  answer_t[0] == ' ':
                del answer_t
            else:
                answer.append(answer_t[0])
        answerlist1.append(answer)
        print(answer)
        #
        # print(answer)
        print("---------------")

yutu()