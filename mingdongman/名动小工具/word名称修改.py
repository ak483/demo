# -*- coding:utf-8 -*-
# @Author : yyzhang
import os
import time
from win32com import client


def doc_to_docx(list_dir, save_file):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    filename_list = [i for i in list_dir if i.split(".")[-1] == "doc"]
    # filename_list=[os.path.join(folder,j) for j in li ]
    # print(filename_list)
    # time.sleep(10)
    try:
        for file in filename_list:
            print("开始转换:", file)
            # print(file)
            # 将doc的文件名换成后缀为docx的文件
            name = os.path.splitext(file)[0] + '.docx'
            # 将我们的docx与文件保存位置拼接起来，获得绝对路径
            out_name = os.path.join(save_file, name)  #
            print("测试后:", name)
            print("转换后：", out_name)
            # out_file.append(out_name)
            file_path = os.path.join(folder, file)
            doc = word.Documents.Open(file_path)  # 打开word文件
            # doc.SaveAs("{}".format(out_name), 12)  # 另存为后缀为".docx"的文件，其中参数12或16指docx文件
            doc.SaveAs("{}".format(out_name), 12, False, "", True, "", False,
                       False, False,
                       False)  # 转换后的文件,12代表转换后为docx文件
            doc.Close()  # 关闭原来word文件
    except Exception as e:
        print(e)
    word.Quit()


if __name__ == "__main__":
    # 支持文件夹批量导入
    folder = 'C:\\Users\\Adminitrator03\\Desktop\\word'
    list_dir = os.listdir(folder)
    # print(list_dir)
    out_dir = 'C:\\Users\\Adminitrator03\\Desktop\\word'
    doc_to_docx(list_dir, out_dir)