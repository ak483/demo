from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xlwt, re, random
import pandas as pd
import queue
import copy

FILE_PATH_DICT = {

    '平台统计': r'C:\Users\Adminitrator03\Desktop\titletest.xlsx',
}

savepath = "优先级2第一二顺位第四批.xls"


def saveData(All_datalist, savepath):  # 保存账号数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('火星', cell_overwrite_ok=True)
    col = ("标题", "分类", "关键词", "地域词",)

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
        '地域词优先级1', '产品词优先级2', '命题组成优先级2第一顺位', '命题组成优先级2第二顺位'
    ]
)
region_ExcelData = mainExcelDict['地域词优先级1']
product_ExcelData = mainExcelDict['产品词优先级2']
mainExcelData1 = mainExcelDict['命题组成优先级2第一顺位']
mainExcelData2 = mainExcelDict['命题组成优先级2第二顺位']

# 账号数据
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


ALldatalist = []
temp_title2 = []

# 关键词和类型的组合
compose_product = []
for i in range(len(productExcelData)):
    compose_product.append(productExcelData[i] + f'[{type_productExcelData[i]}]')


#用于第一顺位无地域词的情况下
after2_queue = queue.Queue()  # 创建一个空队列
tempregionExcelData = regionExcelData*4
for title in tempregionExcelData:
    after2_queue.put(title)
 # 不放回地取出打乱的标题

# 填充第一顺位标题产品词
temp_statisticsDate1 = []
for i in range(len(statisticsDate1)):
    tempstatisticsDate1 = statisticsDate1[i]
    random.shuffle(statisticsDate2)
    for j in range(len(compose_product)):
        tempstatisticsDate2= f'{tempstatisticsDate1}' + f'-{statisticsDate2[j]}-'

        tempstatisticsDate2 = re.sub('{地域}', '【地域】', tempstatisticsDate2)
        temp_statisticsDate1.append(re.sub('产品', compose_product[j], tempstatisticsDate2))  # 第一顺位替换产品词


# temp_statisticsDate3 =copy.copy(temp_statisticsDate1)

for i in range(len(temp_statisticsDate1)):  # 取出一个产品词
    after = temp_statisticsDate1[i]
    # after2_queue1 = queue.Queue()  # 创建一个空队列
    # random.shuffle(temp_statisticsDate3)
    #
    # for title in temp_statisticsDate3:
    #     after2_queue1.put(title)

    # 提取关键词和类型
    for j in range(len(regionExcelData)):  # 用这个产品词加上15个地域词生成生成15个第一顺位的标题

        All_content = []
        # region_after = re.sub('【(.*?)】', regionExcelData[j], after[i]) #取出地域词替换上
        keytype = re.findall('{(.*?)}', after)  # 取出第一顺位的关键词和类型
        key = re.findall('(.*?)\[.*?\]', keytype[0])
        key = key[0]  # 取出第一顺位关键词和类型
        type = re.findall('.*?\[(.*?)\]', keytype[0])
        type = type[0]

        region_after = re.sub('{(.*?)}', key, after)  # 完成产品词的替换

        #随机取二顺位
        # region_after2 = after2_queue1.get()


        title2 = re.findall('.*?-(.*?)-', region_after)
        title2 = title2[0]#单独取出顺位2
        region_after1 = re.findall('(.*?)-.*?', region_after)
        region_after = region_after1[0]#单独取出顺位1

        # 如果每个都有地域词则一直遍历，没有地域词的则完成这一轮一二顺位并跳出循环，继续下一个产品词
        if '【地域】' in region_after:
            pass
            region_after = re.sub('【地域】', regionExcelData[j], region_after)  # 取出地域词替换上
        else:
            # 随机从第二顺位取九个标题

            regionkey = after2_queue.get()
            region_after = re.sub('【地域】', regionkey, region_after)

            title2 = re.sub('{(.*?)}', key, title2)  # 随机出来的第二顺位替换产品词
            title2 = re.sub('【(.*?)】', regionkey, title2)  # 地域词
            region_after = region_after + f'({title2})'
            All_content.append(region_after)
            All_content.append(type)
            All_content.append(key)
            All_content.append(regionkey)
            print(All_content)
            ALldatalist.append(All_content)
            break

        # 随机从第二顺位取九个标题
        title2 = re.sub('{(.*?)}', key, title2)  # 随机出来的第二顺位替换产品词
        title2 = re.sub('【(.*?)】', regionExcelData[j], title2)

        region_after = region_after + f'({title2})'
        All_content.append(region_after)
        All_content.append(type)
        All_content.append(key)
        All_content.append(regionExcelData[j])
        print(All_content)
        ALldatalist.append(All_content)
    pass

saveData(ALldatalist, savepath)