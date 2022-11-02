import requests
from lxml import html
etree = html.etree

if __name__ == "__main__":
    headers =  {
        "User-Agent": 'Mozilla / 5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }

    url = 'http://search.dangdang.com/?key=%BF%C6%BB%C3&act=input'
    page_text = requests.get(url=url,headers=headers).text
    print( page_text)
    tree = etree.HTML(page_text)

    fp = open('dangdang.txt','w',encoding='utf-8')

    div_list = tree.xpath('//div[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
    print(div_list)
    for div in div_list:
        title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
        print(title)
        fp.write(title+'\n')

    fps = open