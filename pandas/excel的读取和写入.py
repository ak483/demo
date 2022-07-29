# -*- codeing = utf-8 -*-
# @Time :2022/7/28 22:43
# @Author:Eric
# @File : excel的读取和写入.py
# @Software: PyCharm
import pandas as pd
data = pd.read_excel('data.xlsx')
print(data)

data = pd.DataFrame([[1,2],[3,4],[5,6]],columns=['A列','B列'])
# data.to_excel('data_0.xlsx')

data.to_excel('data_1.xlsx',columns=['A列'],index=False)
