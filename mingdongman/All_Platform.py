# coding=utf-8

from demo.mingdongman.Douyin_Auto.AcFun import Add_AcFun_video
from demo.mingdongman.Douyin_Auto.Banciyuan import Add_Banciyuan_video


#AcFun
try:
    Add_AcFun_video()
except:
    input('AcFun执行错误')

#半次元
try:
    Add_Banciyuan_video()
except:
    input('半次元执行错误')










if __name__ == '__main__':
    pass


