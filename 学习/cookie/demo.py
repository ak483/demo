import requests
from lxml import etree
import re
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import datetime
import xlwt

headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'referer': 'https://sf.taobao.com/',
    'cookie': 't=ff25ac54b11addfe155f470545b61874; thw=cn; _tb_token_=315be083ebbe7; _samesite_flag_=true; enc=e8Z6i2YhprGpJUtkTh%2FUtIEEYM3ZRG%2BaiGit7YM51LH0UrPz4uCFB42NlYD2GCxswVmh9kqDVszDZ3gd4eDV8A%3D%3D; cookie2=22d180181859475cabdbb70239ca50cf; _m_h5_tk=f3235ce2aceb5494a0253be80ba8ebac_1657271280112; _m_h5_tk_enc=d3d18b9c5255351db99f5b7ec0bcdf3f; sgcookie=E100Fskrp74NBp7D%2BGf7eeE8U%2ByEEH02dK82xCu7%2BtRT42WQh1uOPxlbMtak%2BxnKwHLxB6XlhtKXaAETmbBIHRYWrJ304nrYWhRdzHBM7mM5s2CQBsEZjZpIIsDngUMcPTJ%2F; xlly_s=1; mt=ci=0_0; tracknick=; cna=NBs+Goz8KCoCAXBgQCBeU5dD; uc1=cookie14=UoexNTIugexf9g%3D%3D; x5sec=7b22676f7661756374696f6e3b32223a22333330333962383032663331666236383135313332613334373138356565616143496a45705a5947454e54306c594737714d375171414561444449354e7a6b324d7a63354e4455374d5443307236764642773d3d222c22617365727665723b32223a22363635343066346264386636623564303864373335353766666532616462326643493352705a5947454d71496c39546f694b36727041457738377a646c2f762f2f2f2f2f41546f43617a453d227d; isg=BJCQT2ObxtovxZrQ7wDSDZcbYd7iWXSjfYC7LophXOu-xTBvMmlEM-Z3mY0lDix7; l=eBT7S5HqLf0qtNfsBOfanurza77OSIRYYuPzaNbMiOCP_71B5LI1W6A1DuT6C3GVh6VeR3Wrj_IwBeYBq7VonxvTPNOwbhkmn; tfstk=cv91BP0JEP4_i0rEPtiE_b2uepBAwk0Cxf_9f2Q4rlKPQa10C87S-9R0-tSAA'
}
url = 'https://sf.taobao.com/list/0__4__%B9%E3%B6%AB.htm?spm=a213w.7398504.filter.87.65064566KNQREo&auction_source=0&item_biz_type=6&st_param=-1&auction_start_seg=-1'
# res = requests.get(url=url,headers=headers).text
# print(res)


    #2.逐步解析数据
res = requests.get(url=url, headers=headers).text
print(res)

# title = re.findall('"title":"(.*?)",',res) # re库用来通过正则表达式查找指定的字符串
# itemUrl = re.findall('"itemUrl":.*?"(.*?)",', res,re.S)
# currentPrice = re.findall('"currentPrice":(.*?),', res)
# status = re.findall('"status":.*?"(.*?)",', res,re.S)
# start = re.findall('"status":.*?"(.*?)",', res,re.S)
# end = re.findall('"end":.*?(.*?),', res,re.S)
#
# new_ends = [];
# for i in end:
#     new_ends[i] = end[i].strip()
# end = new_ends
#
#
# print(title)
# print(itemUrl)
# print(currentPrice)
# print(status)
# print(end)



