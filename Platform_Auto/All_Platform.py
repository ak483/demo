# coding=utf-8

from mingdongman.Platform_Auto.AcFun import Add_AcFun_video
from mingdongman.Platform_Auto.Banciyuan import Add_Banciyuan_video


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

