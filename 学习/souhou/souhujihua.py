import pandas as pd
import re

mainExcelDict=pd.DataFrame=pd.read_excel(r'C:\Users\Adminitrator03\Desktop\无标题.xls',sheet_name=[
        '极画教育'
    ])

content = (mainExcelDict['极画教育'])['内容'].to_list()
title = (mainExcelDict['极画教育'])['标题'].to_list()
title_section = (mainExcelDict['极画教育'])['标题前半段'].to_list()

contet_test=content[0]

for i in range(len(content)):
    content[i] = re.sub('\n\n', '\n', content[i])
    content[i] = re.sub(title_section[i],'',content[i])

print(type(content))

a = pd.DataFrame(content)
a.to_excel('搜狐清洗后内容.xls', sheet_name='极画教育')

# ti='?极画教育告诉你！'
# title=[x for x in title if ti in x]
# print(title)

# for i in range(len(title))
#     content=[]
# contents_list=[]
# for i in range(len(content)):
#
#
#     #根据空白部分对字符串进行分段
#     a = content[i]
#     content_list = (a.split())
#
#     #排除标题前半段
#     content_list = [x for x in content_list if title_section[i] in x]
#
#     #将列表整合为字符串并进行分段
#     contents = ('\n'.join(content_list))
#
#     contents_list.append(contents)

# print(content[0])
# print(content[75])
# print('分割')

# input('请输入')
# print('提前结束')