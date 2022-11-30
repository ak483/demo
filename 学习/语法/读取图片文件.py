# encoding: utf-8
import os,re
from My_code.名动漫.Mdm_API import IllustrationWorkClassAPI

def to_text(src, dst1):
    txt = []
    filenames = os.listdir(src)
    clear_img = []
    for i in range(len(filenames)):
        tmp = re.sub('\.jpg', '',filenames[i])
        # tmp = re.sub('m', '', tmp)
        # tmp = re.sub('\.png', '', tmp)
        # tmp = re.sub('\.bmp', '', tmp)
        clear_img.append(tmp)
    # print(clear_img)
    return clear_img


    #
    # fo = open(dst1, 'w')
    # for item in txt:
    #     fo.write(str(item) + '\n')


if __name__ == "__main__":
    src = r'G:\2345下载 - 副本'
    dst1 = r'D:\untitled1\demo\学习\语法\file.txt'
    nameStr = []
    idStr = []
    startId = 6320
    successData = IllustrationWorkClassAPI().Query(articleIdInt=startId + 1, inquireIndex=900, arcrankInt=0)

    for workdict in successData:
        tmp = workdict['nameStr']
        ID_tmp = workdict['idInt']
        nameStr.append(tmp)
        idStr.append(ID_tmp)

    name_img = to_text(src, dst1)

    a = [x for x in nameStr if x not in name_img]
    b = [x for x in name_img if x not in nameStr]
    print(a)
    print(len(a))
    print(b)

    # for i in range(len(nameStr)):
    #     for j in range(len(name_img)):
    #         if nameStr[i] == name_img[j]:
    #             pass
    #         else:
    #             print(nameStr[i],idStr[i])

