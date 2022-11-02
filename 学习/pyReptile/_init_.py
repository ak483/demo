# coding=utf-8
'''
初始化文件是整个框架的入口，
它导入了整个框架的功能。
在使用框架的时候，
只需在初始化文件调用相关的功能模块即可。
功能文件pattern.py、spider.py和storage.py支撑整个框架的运行
'''

__version__ = '1.0.0'
from .storage import *
from .spider import *
from .pattern import *
