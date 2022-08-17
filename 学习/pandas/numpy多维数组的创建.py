# -*- codeing = utf-8 -*-
# @Time :2022/7/27 23:19
# @Author:Eric
# @File : numpy多维数组的创建.py
# @Software: PyCharm
import numpy as np

x = np.arange(5)

y = np.arange(5,10)

z = np.arange(5,10,0.5)

print(x)
print(y)
print(z)

c = np.random.randn(4)
print(c)

d = np.random.randn(12).reshape(3,4)
print(d)

e = np.random.randint(0,10,(4,4))
print(e)

