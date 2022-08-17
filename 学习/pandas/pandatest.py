# -*- codeing = utf-8 -*-
# @Time :2022/7/27 23:04
# @Author:Eric
# @File : pandatest.py
# @Software: PyCharm
import numpy as np
a = [1,2,3,4]
b = np.array([1,2,3,4])

print(a)
print(b)
print(type(a))
print(type(b))
print(a[1])
print(b[1])
print(a[0:2])
print(b[0:2])

c = a*2
d = b*2

print(c)
print(d)


e = [[1,2],[3,4],[5,6]]
f = np.array([[1,2],[3,4],[5,6]])

print(e)
print(f)

g = f*2
print(g)

print(f[1])

print('--------------------------------------')

