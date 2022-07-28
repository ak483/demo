# -*- codeing = utf-8 -*-
# @Time :2022/7/27 23:35
# @Author:Eric
# @File : 二维数据表格dataframe的创建.py
# @Software: PyCharm
import pandas as pd

a = pd.DataFrame([[1, 2],[3, 4],[5, 6]])
print(a)

a = pd.DataFrame()
date = [1,3,5]
score = [2,4,6]
a['data'] = date
a['score'] = score
print(a)

b = pd.DataFrame({'a':[1,3,5], 'b':[2,4,6]},index=['x','y','z'])
print(b)



#行索引
c = pd.DataFrame.from_dict({'a':[1,3,5],'b':[2,4,6]},orient='index')
print(c)

import numpy as np
d = pd.DataFrame(np.arange(12).reshape(3,4),index=[1,2,3],columns=['A','B','C','D'])
print(d)


#添加行索引的名称
a = pd.DataFrame([[1,2],[3,4],[5,6]], columns=['date','score'],index=['A','B','C'])
a.index.name = '公司'
#a.columns.name = '数据项'
print(a)

a = a.rename(index={'A': '万科', 'B': '阿里', 'C': '百度'}, columns={'date': '日期','score': '分数'})
print(a)

a = a.reset_index()
print(a)


#将‘日期设置为行索引
a = a.set_index('日期')
print(a)