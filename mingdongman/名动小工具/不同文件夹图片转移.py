# -*- codeing = utf-8 -*-
# @Time :2022/11/23 0:47
# @Author:Eric
# @File : 图片合并.py
# @Software: PyCharm

import shutil#这个库复制文件比较省事
import os,re
from PIL import Image
import pandas as pd

FILE_PATH_DICT = {
    # 本地
    '公用路径2': r'\\Hwindows\公用2',
    '本地资源': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Resource',
    '视频图片保存路径': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Tutorial\image',
    '视频截屏保存路径': r'\\DESKTOP-J6ECV53\python_file\Resource_Tutorial\Tutorial',
    '浏览器驱动': r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',
    '浏览器个人配置':r'G:\Selenium_UserData\Mdm\one',
    '图片路径': r'C:\Users\Adminitrator03\Desktop\作品详情表（成成）.xlsx',
    '共享盘资源': r'C:\Users\Adminitrator03\Desktop\baikeform',

}
#读取路径
mainExcelDict = pd.read_excel(
    FILE_PATH_DICT['图片路径'], sheet_name=[
        '新作品详情（1.7开始用）'
    ]
)
mainExcelData = mainExcelDict['新作品详情（1.7开始用）']

# 筛选
mainExcelData_shuiyin = mainExcelData['存储路径（去水印）'].to_list()

for i in range(len(mainExcelData_shuiyin)):

    mainExcelData_shuiyin[i] = re.sub(r'\\', '/', mainExcelData_shuiyin[i])


for j in range(len(mainExcelData_shuiyin)):
    dirname_read=mainExcelData_shuiyin[j]  # 注意后面的斜杠
    dirname_write="G:/2345下载"
    names_all=os.listdir(dirname_read)

    def file_filter(f):
        if f[-4:] in ['.jpg', '.png', '.bmp']:
            return True
        else:
            return False

    picture_nmmes = list(filter(file_filter, names_all))

    print(picture_nmmes)
    print(len(picture_nmmes))
    print(dirname_read)
    for i in picture_nmmes:
        new_obj_name = i
        print(new_obj_name)
        shutil.copy(dirname_read + '/' + new_obj_name, dirname_write + '/' + new_obj_name)
