import time,re
import pandas as pd
import xlwt


mainExcelDict=pd.DataFrame=pd.read_excel(r'G:\WeChatCache\WeChat Files\wxid_1svuuhg2lwg922\FileStorage\File\2022-09\极画.xlsx', sheet_name=[
        '极画'
    ])

content = (mainExcelDict['极画'])['内容'].to_list()
# title = (mainExcelDict['极画教育'])['标题'].to_list()
# title_section = (mainExcelDict['极画教育'])['标题前半段'].to_list()

content_list=[]
for i in range(len(content)):

    #将多余换行删除
    # content[i] = re.sub('" data-caption=.*?jpg">', '', content[i])
    content[i] = re.sub('\n\n\n\n', '\n', content[i])
    content[i] = re.sub('\n\n\n', '\n', content[i])
    content[i] = re.sub('\n\n', '\n', content[i])
    content_list.append((content[i]))


#删除首尾
content_list___=[]
for i in range(len(content_list)):
    a = content_list[i]
    content_list_ = (a.split())
    content_list__ = content_list_[1:-1]
    contents = ('\n'.join(content_list__))
    content_list___.append(contents)



savepath = "极画去首尾文章.xls"

book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
sheet = book.add_sheet('知乎', cell_overwrite_ok=True)
col = ("去首首尾文章")
for i in range(0, 1):
    sheet.write(0, i, col)  # 列名
for i in range(0, len(content_list___)):
    print("第%d条" % (i + 1))
    sheet.write(i + 1, 0, content_list___[i])
book.save(savepath)  # 保存

