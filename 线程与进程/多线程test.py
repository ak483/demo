# -*- codeing = utf-8 -*-
# @Time :2022/6/28 9:36
# @Author:Eric
# @File : 多线程test.py
# @Software: PyCharm
import multiprocessing

import time
import threading

def test1():
    print('任务1进行中，任务1持续3秒')
    time.sleep(3)
    print('任务1结束')

def test2():
    print('任务2进行中，任务2持续2秒')
    time.sleep(2)

start_time = time.time()
test1()
test2()
end_time = time.time()

print (multiprocessing.cpu_count())










