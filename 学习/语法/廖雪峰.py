#判断对象是否可迭代，用collection模块的iterable类型判断
# from collections.abc import Iterable
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))

#enumerate函数把一个list变成索引-元素对，在for循环中同时迭代索引和元素本身
# for i , value in enumerate(['a','b','c']):
#     print(i,value)
#     print(i)

#只要是可迭代对象，无论有无下标都可以迭代,默认迭代key
# d = {'a':1,'b':2,'c':3}
# for key in d:
#     print(key)
#
# #迭代value使用values方法
# for value in d.values():
#     print(value)

#同时迭代key 和 value，其中k输出value,v输出索引
# for k,v in d.items():
    # print(v)


#生成器：generator，一边循环一边计算

#创建方式1:将列表生成式的[]改成（）
# L = [x*x for x in range(10)]
# print(L)
# print(type(L))
#
# g = (x*x for x in range(10))
# print(g)
# print(type(g))
#
# for n in g:
#     print(n)

#创建方式2，用yield关键字,调用
import sys
print(1)
#菜鸟例子
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

#map和reduce的应用、
#filter()函数返回的是一个iterrator，是一个惰性序列
#sort()可以接受一个key函数自定义排序规则
#可变参数* 和关键字参数**


#asyncio 提供了完善的异步 IO 支持；
#异步操作需要在 coroutine 中通过 yield from 完成；
#多个 coroutine 可以封装成一组 Task 然后并发执行。

#async/await是协程和生成器生成的异步操作的简化:
#1. 把@asyncio.coroutine 替换为 async；
#2. 把 yield from 替换为 await。


#metaclass:元类
#允许你创建类或者修改类，你可以把类看成是metaclass创建出来的实例