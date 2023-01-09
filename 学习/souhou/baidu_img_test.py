import requests
import time,xlwt
import jsonpath,random

All_url = []

def save(All_datalist):#保存账号数据
    savepath = r'D:\untitled1\demo\Excel杂货间\原画.xlsx'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('插图', cell_overwrite_ok=True)
    col = ("信息",)

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条" % (i + 1))
        # data = All_datalist[i]
        # for j in range(0, len(data)):
        sheet.write(i + 1, 0, All_datalist[i])
    book.save(savepath)  # 保存


if __name__ == '__main__':
    content = input('请输入要搜索的内容：')
    pages = int(input('请输入要爬取的页数：'))
    for i in range(pages):
        pn = (i+1)*30
        # 确认图片页面的url
        # url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={content}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={content}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={pn}&rn=30&gsm={str(hex(pn))[-2:]}&{str(int(time.time())*1000)}='
        gsm = f'{str(hex(pn))[2:]}'+'0000000000000000'
        gsm = gsm[:14] + f'{str(hex(pn))[2:]}'
        url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9265861672548773086&ipn=rj&ct=201326592&is=&fp=result&fr=&word={content}&queryWord={content}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={pn}&rn=30&gsm={gsm}&{str(int(time.time())*1000)}='
        # 创建请求头参数
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
            }
        # 发送请求获取响应

        print(i)
        print(url)
        # url=f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8938851843525749483&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E6%8F%92%E7%94%BB&queryWord=%E6%8F%92%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=570&rn=30&gsm=23a0000000000023a&{str(int(time.time())*1000)}='
        response = requests.get(url,headers=headers)
        # 判断数据类型(为json类型）
        try:
            py_data = response.json()
        except:
            print('啊这url不行',url)
            continue

        # 提取数据中图片的url
        img_url = jsonpath.jsonpath(py_data,'$.data[*].fromURLHost')
        print(img_url)
        try:
            for j in range(len(img_url)):
                All_url.append(img_url[j])
        except:
            print('这url不行',url)
            continue

        # time.sleep(random.randint(5,10))


    save(All_url)


        # print(len(img_url))
        # for i in py_data['data']:
        #     if i:
        #         img_url = i['middleURL']
        #         response1 = requests.get(img_url,headers=headers)
        #         bytes_data = response1.content
        #         # 保存数据
        #         with open(f'{content}.{int(time.time()*1000)}.jpg','wb')as f:
        #             f.write(bytes_data)
