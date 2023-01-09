import pandas as pd
import re, requests, xlwt, time
from lxml import html

etree = html.etree

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    # 'cookie': 'XID=bdb30eda-61c1-4beb-90be-8ccd8270c00c; Hm_lvt_63a8941b9af78a70fb9a9951990bbcbd=1670470461; __gads=ID=f0aaf1fbba130d0d-22caf8a2cbd80025:T=1670470461:RT=1670470461:S=ALNI_Masqmi_al_1hNUkJKHJAB2wMbesTQ; __gpi=UID=00000b8c60034962:T=1670470461:RT=1671158210:S=ALNI_MaZLSYoV52YZ-jFWA3tJEx9IvcE2w; user=%7B%22id%22:591408246,%22name%22:%22%E5%B0%8F%E9%B8%A163915f16a5ca2%22,%22token%22:%22121b59a72b0fa350a7cd9f6421caac0ba622ca8a37c737f1b8ee55da6afe86ae%22,%22user_id%22:591408246,%22user_name%22:%22%E5%B0%8F%E9%B8%A163915f16a5ca2%22,%22avatar%22:%22%22,%22scaled_avatar%22:%22%22,%22user_role%22:%22editor%22,%22badge%22:%7B%7D,%22badge_full_image%22:%22%22%7D; Hm_lpvt_63a8941b9af78a70fb9a9951990bbcbd=1671169352'
}

Alldatalist = []


def getData(p):
    url = f'https://www.ycpai.cn/huihua/index_{p}.html'
    res = requests.get(url, headers=headers, timeout=10).text

    # 用xpath提取文章内容
    restree = etree.HTML(res)
    div_list = restree.xpath('//div[@class="pc_list"]')
    for div in div_list:
        datalist = []
        title = div.xpath('./div[@class="slt"]/a/@title')[0]
        content_url = div.xpath('./div[@class="slt"]/a/@href')[0]
        label = div.xpath('./div[2]/div/span[@class="spn"]/a/text()')
        label = ','.join(label)
        label = re.sub('\n', '', label)
        label = re.sub(' ', '', label)

        # 获取文章内容
        contenturl = 'https://www.ycpai.cn' + content_url
        res = requests.get(contenturl, headers=headers, timeout=10).text


        datalist.append(title)
        datalist.append(content_url)
        datalist.append(label)
        Alldatalist.append(datalist)

        print(datalist)
    return datalist


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('搜狐', cell_overwrite_ok=True)  # 创建工作表
    col = ("标题", "时间", "链接", "分类")
    for i in range(0, 4):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    # 调用函数

    for p in range(444):
        print(p)
        getData(p + 1)
        time.sleep(1)
    print(Alldatalist)

    savepath = "优草派.xls"
    # 3.保存数据
    saveData(Alldatalist, savepath)
    print("爬取完毕！")

