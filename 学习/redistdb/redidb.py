# -*- codeing = utf-8 -*-
# @Time :2022/7/10 21:42
# @Author:Eric
# @File : redidb.py
# @Software: PyCharm
import redis   # 导入redis 模块

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set('name', 'runoob')  # 设置 name 对应的值
print(r['name'])
print(r.get('name'))  # 取出键 name 对应的值
print(type(r.get('name')))  # 查看类型
