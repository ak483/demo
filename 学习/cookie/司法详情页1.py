# -*- codeing = utf-8 -*-
# @Time :2022/7/11 0:22
# @Author:Eric
# @File : 司法详情页1.py
# @Software: PyCharm
import re
import requests
import requests_cache
import xlrd

requests_cache.install_cache()
requests_cache.clear()

url= 'https://sf-item.taobao.com/sf_item/677385696489.htm?track_id=07e579bc-a61e-4375-a9e2-21c59419dffb'

session = requests.session()

data=xlrd.open_workbook(r'D:/python私塾/demo/cookie/广东诉讼拍卖已结束13.xls')
sheet=data.sheet_by_index(0)


for i in range(100):
    #url=sheet.cell_value(1,1)
    reso = session.get(url=url).text
    reso = re.sub('\s+', '', reso)
    print(reso)
    print(i)
    print('.................................')


