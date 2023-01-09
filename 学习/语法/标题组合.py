from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xlwt,re,random
import pandas as pd
import queue

FILE_PATH_DICT = {
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-名动漫官网.xlsx',
    '标题保存': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\标题2.xlsx',
    '原文配图': 'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/Fifth_Batch',
    # '平台统计': r'D:\untitled1\Excel\短视频数据统计-20221207.xlsx',
    '平台统计': r'C:\Users\Adminitrator03\Desktop\titletest.xlsx',
}

savepath = "产品词优先级2第三批.xls"
def saveData(All_datalist,savepath):#保存账号数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('火星', cell_overwrite_ok=True)
    col = ("标题",)

    for i in range(0, len(col)):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条" % (i + 1))
        # data = All_datalist[i]
        # for j in range(0, len(data)):
        sheet.write(i + 1, 0, All_datalist[i])
    book.save(savepath)  # 保存

mainExcelDict = pd.read_excel(
    FILE_PATH_DICT['平台统计'], sheet_name=[
        '地域词优先级1','产品词优先级2','命题组成优先级1第一顺位','命题组成优先级1第二顺位'
    ]
)
region_ExcelData = mainExcelDict['地域词优先级1']
product_ExcelData = mainExcelDict['产品词优先级2']
mainExcelData1 = mainExcelDict['命题组成优先级1第一顺位']
mainExcelData2 = mainExcelDict['命题组成优先级1第二顺位']

#账号数据
regionExcelData = region_ExcelData['关键词'].to_list()
productExcelData = product_ExcelData['关键词'].to_list()
type_productExcelData = product_ExcelData['类型'].to_list()
statisticsDate1 = mainExcelData1['标题规则'].to_list()
statisticsDate2 = mainExcelData2['标题规则'].to_list()

def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('搜狐', cell_overwrite_ok=True)  # 创建工作表
    col = ("标题", "分类", "关键词")
    for i in range(0, 3):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

#关键词和类型的组合
compose_product = []
for i in range(len(productExcelData)):
    compose_product.append(productExcelData[i] + f'[{type_productExcelData[i]}]')

#填充第二顺位标题产品词
temp_statisticsDate2 = []
random.shuffle(statisticsDate2)
for i in range(len(statisticsDate2)):
    # product = random.choice(compose_product)
    for j in range(len(compose_product)):
        temp_statisticsDate2.append(re.sub('产品', compose_product[j], statisticsDate2[i]))  # 第一顺位替换产品词

#填充第一顺位标题产品词
temp_statisticsDate1 = []
for i in range(len(statisticsDate1)):
    # product = random.choice(compose_product)
    for j in range(len(compose_product)):
        temp_statisticsDate1.append(re.sub('产品', compose_product[j],statisticsDate1[i]))#第一顺位替换产品词

#组合一二顺位
# after = []
# for i in range(len(statisticsDate1)):
#     key = re.findall('{(.*?)}',statisticsDate1[i])
#     while True:
#         #随机取值，但不能与前九个重复
#         title2 = random.choice(statisticsDate2)
#         key2 = re.findall('{(.*?)}', title2)
#         if key == key2:
#             # All_title2.append(title2)
#             break
#         else:
#             pass
#
#     # 随机去第二顺位标题
#     temp = statisticsDate1[i] + f'({title2})'
#     print(temp)
#     after.append(temp)
#
# print('执行完毕')
# print(after)

#提取整合
after = temp_statisticsDate1
# random.shuffle(temp_statisticsDate2)

after2_queue = queue.Queue()  # 创建一个空队列
for title in temp_statisticsDate2:
    after2_queue.put(title)

ALldatalist =[]
temp_title2 = []
for i in range(len(after)):
    All_content = []
    # 提取关键词和类型
    keytype = re.findall('{(.*?)}', after[i])
    key = re.findall('(.*?)\[.*?\]', keytype[0])
    key = key[0]#取出第一顺位关键词和类型
    type = re.findall('.*?\[(.*?)\]', keytype[0])
    type = type[0]
    after[i] = re.sub('{(.*?)}',key,after[i])#完成第一顺位替换

    #随机从第二顺位取九个标题
    # while True:
    title2 = after2_queue.get()#不放回地取出打乱的标题
    title2 = re.sub('{(.*?)}', key, title2)  # 随机出来的第二顺位替换产品词

        # if title2 not in temp_title2:
        #     temp_title2.append(title2)
        #     break
        # else:
        #     pass

    after[i] = after[i] + f'({title2})'

    # if title2 not in temp_title2:
    #     temp_title2.append(title2)
    # else:
    #     pass


    All_content.append(after[i])
    All_content.append(type)
    All_content.append(key)
    ALldatalist.append(All_content)


saveData(ALldatalist, savepath)