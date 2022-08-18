# coding=utf-8

from demo.Platform_Auto.AcFun import Add_AcFun_video
from demo.Platform_Auto.Banciyuan import Add_Banciyuan_video
from demo.Platform_Auto.Bilibili import Add_Bilibili_video
from demo.Platform_Auto.Douyin import Add_Douyin_video
from demo.Platform_Auto.Haokan import Add_Haokan_video
from demo.Platform_Auto.iQIYI import Add_iQIYI_video
from demo.Platform_Auto.Kuaishou_Add_Video import Add_Kuaishou_video
from demo.Platform_Auto.LOFTER import Add_LOFTER_video
from demo.Platform_Auto.Pipixia import Add_Pipixia_video
from demo.Platform_Auto.Qiehao import Add_Qiehao_video
from demo.Platform_Auto.Shipinhao import Add_Shipinhao_video
from demo.Platform_Auto.Sohu import Add_Sohu_video
#from demo.Platform_Auto.Tencent import Add_Tencent_video
from demo.Platform_Auto.Wangyi import Add_Wangyi_video
from demo.Platform_Auto.Weibo import Add_Weibo_video
from demo.Platform_Auto.Xiaohongshu import Add_Xiaohongshu_video
from demo.Platform_Auto.Xigua import Add_Xigua_video
from demo.Platform_Auto.Youku import Add_Youku_video
from demo.Platform_Auto.Zhihu import Add_Zhihu_video

#1、AcFun
try:
    Add_AcFun_video()
except:
    input('AcFun执行错误')

#2、半次元
try:
    Add_Banciyuan_video()
except:
    input('半次元执行错误')

#3、Bilibili
try:
    Add_Bilibili_video()
except:
    input('Bilibili执行错误')

#4、抖音
try:
    Add_Douyin_video()
except:
    input('抖音执行错误')

#5、好看视频
try:
    Add_Haokan_video()
except:
    input('好看视频执行错误')

#6、爱奇艺
try:
    Add_iQIYI_video()
except:
    input('爱奇艺执行错误')

#7、快手
try:
    Add_Kuaishou_video()
except:
    input('快手执行错误')

#8、LOFTER
try:
    Add_LOFTER_video()
except:
    input('LOFTER执行错误')

#9、皮皮虾
try:
    Add_Pipixia_video()
except:
    input('皮皮虾执行错误')

#10、企鹅号
try:
    Add_Qiehao_video()
except:
    input('企鹅号执行错误')

#11、视频号
try:
    Add_Shipinhao_video()
except:
    input('视频号执行错误')

#12、搜狐
try:
    Add_Sohu_video()
except:
    input('搜狐执行错误')

# 13、腾讯视频
# try:
#     Add_Tencent_video()
# except:
#     input('腾讯视频执行错误')

# 14、网易
try:
    Add_Wangyi_video()
except:
    input('网易执行错误')

# 15、微博
try:
    Add_Weibo_video()
except:
    input('微博执行错误')

# 16、小红书
try:
    Add_Xiaohongshu_video()
except:
    input('小红书执行错误')

# 17、西瓜
try:
    Add_Xigua_video()
except:
    input('西瓜视频执行错误')

# 18、优酷
try:
    Add_Youku_video()
except:
    input('优酷执行错误')

# 19、知乎
try:
    Add_Zhihu_video()
except:
    input('知乎执行错误')


if __name__ == '__main__':
    pass
