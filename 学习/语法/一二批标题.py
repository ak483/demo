import xlwt, re, random
import pandas as pd
import queue
import copy

FILE_PATH_DICT = {

    '平台统计': r'C:\Users\Adminitrator03\Desktop\titletest.xlsx',
    '数据表': r'D:\untitled1\demo\学习\语法\产品词优先级2第三批.xls'

}

savepath = "第三批.xls"

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


mainExcelDict = pd.read_excel(
    FILE_PATH_DICT['平台统计'], sheet_name=[
        '地域词优先级1', '产品词优先级2', '命题组成优先级1第一顺位', '命题组成优先级1第二顺位'
    ]
)
region_ExcelData = mainExcelDict['地域词优先级1']
product_ExcelData = mainExcelDict['产品词优先级2']
mainExcelData1 = mainExcelDict['命题组成优先级1第一顺位']
mainExcelData2 = mainExcelDict['命题组成优先级1第二顺位']

# 账号数据
regionExcelData = region_ExcelData['关键词'].to_list()
productExcelData = product_ExcelData['关键词'].to_list()
type_productExcelData = product_ExcelData['类型'].to_list()
statisticsDate1 = mainExcelData1['标题规则'].to_list()
statisticsDate2 = mainExcelData2['标题规则'].to_list()


mainExcelDict1 = pd.read_excel( FILE_PATH_DICT['数据表'],sheet_name='搜狐')

All_content = []

for k in range(len(productExcelData)):

    a = mainExcelDict1[mainExcelDict1['关键词'] == productExcelData[k]]
    b = a['标题'].to_list()
    c = a['分类'].to_list()
    c = c[0]
    after2_queue = queue.Queue()  # 创建一个空队列
    temp = copy.copy(statisticsDate2)
    random.shuffle(temp)
    for t in temp:
        after2_queue.put(t)#随机取出了所有未清洗的二顺位标题

    for j in range(len(b)):#将二顺位标题不放回地替换到总标题中
        title = re.sub('\(.*?\)', f'({after2_queue.get()})', b[j])
        title1 = re.sub('{产品}', productExcelData[k], title)#将产品替换
        # title2 = re.sub('{地域}', regionExcelData[r], title1)#将地域词替换
        All_title = []
        All_title.append(title1)
        All_title.append(c)
        All_title.append(productExcelData[k])
        # All_title.append(regionExcelData[r])

        All_content.append(All_title)
print(All_content)





saveData(All_content, savepath)
