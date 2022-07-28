# -*- codeing = utf-8 -*-
# @Time :2022/7/28 0:08
# @Author:Eric
# @File : 数据的读取与筛选.py
# @Software: PyCharm
import pandas as pd
data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['r1', 'r2', 'r3'], columns=['c1', 'c2', 'c3'])
print(data)

a = data['c1']
print(a)

b = data[['c1']]
print(b)

c = data[['c1', 'c3']]
print(c)

a = data[1:3]#选取第二行和第三行的数据，左闭右开
print(a)

b = data.iloc[1:3]#也是行索引,根据序号
print(b)

c = data.iloc[-1]
print(c)
print('--------------')
d = data.loc[['r2', 'r3']]#loc根据行索引的名称来选取
print(d)
print('------------------------')

a = data[['c1', 'c3']][0:2]  # 也可写成data[0:2][['c1', 'c3']]
print(a)

b = data.iloc[0:2][['c1', 'c3']]
print(b)