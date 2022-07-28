# -*- codeing = utf-8 -*-
# @Time :2022/7/20 19:59
# @Author:Eric
# @File : yututest.py
# @Software: PyCharm
import requests
import re
from lxml import etree

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

answerlist = []
def yutu(i):
    url = 'https://www.yutu.cn/soft/tag_15742_'+str(i)+'.html'
    print(url)
    r = requests.get(url=url, headers=headers)
    r.encoding = 'utf-8'
    res=r.text
   # print(res)
    title = re.findall('<p class="h2-tite">(.*?)</p>',res)
    href = re.findall('<a class="comm-item" target="_blank" href="(.*?)">',res)
    print(title)
    print(href)

    for q in range(len(href)):
        qr = requests.get(url=href[q], headers=headers)
        qr.encoding = 'utf-8'
        ress = qr.text
        tree = etree.HTML(ress)
        answer = []
       #提取元素并清除空列表以及列表元素为空格
        div_list = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/p')
        descript = tree.xpath('/html/head/meta[6]/@content')
        answer.append(title[q])
        answer.append(title[0])
        print(len(div_list))
        if len(div_list)==0:
            div_list = tree.xpath('/html/body/div[2]/div/div[2]/div[1]/div[4]/div[2]/div/div[2]/div[2]/div/text()')
            answer.append(div_list[0])
            answerlist.append(answer)

        else:
            for p in div_list:
                answer_t = p.xpath('./text()')
                if len(answer_t) == 0:
                    del answer_t
                elif  answer_t[0] == ' ':
                    del answer_t
                else:
                    answer.append(answer_t[0])
                    answerlist.append(answer)
            print(answer)
            print("---------------")
    print(answerlist)

if __name__ == "__main__":
    for i in range(12):
        i = i+1
        yutu(i)
        print('页数：',i)