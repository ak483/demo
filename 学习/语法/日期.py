# coding=utf-8

import time

day = time.strftime('%Y/%m/%d',time.localtime(time.time()))
yesterday = time.strftime('%Y/%m/%d', time.localtime(time.time() - 86400))
print(day)
print(yesterday)
print(type(day))