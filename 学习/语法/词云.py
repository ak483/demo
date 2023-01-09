from wordcloud import WordCloud
import matplotlib.pyplot as plt
import xlwt,re
import pandas as pd

FILE_PATH_DICT = {
    '半自动洗稿项目': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\半自动洗稿项目-名动漫官网.xlsx',
    '标题保存': r'\\DESKTOP-J6ECV53\Users\Adminitrator03\Desktop\脚本运行产生的文件\半自动洗稿\标题2.xlsx',
    '原文配图': 'https://mdm-article.oss-cn-shenzhen.aliyuncs.com/Article_Image/Fifth_Batch',
    # '平台统计': r'D:\untitled1\Excel\短视频数据统计-20221207.xlsx',
    '平台统计': r'C:\Users\Adminitrator03\Desktop\修饰词提炼.xlsx',
}

savepath = "火星标题词未清洗.xls"
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
        '地域词','产品词','火星原始表','命题参考','未清洗'
    ]
)
region_ExcelData = mainExcelDict['地域词']
product_ExcelData = mainExcelDict['产品词']
mainExcelData = mainExcelDict['火星原始表']
#账号数据
regionExcelData = region_ExcelData['关键词'].to_list()
productExcelData = product_ExcelData['产品关键词'].to_list()
statisticsDate = mainExcelData['标题'].to_list()
str_regionExcelData = '|'.join(regionExcelData)#拼接地域词
productExcelData = map(re.escape, productExcelData)#对产品词进行格式化
str_productExcelData = '|'.join(productExcelData)#拼接产品词

for i in range(len(statisticsDate)):
    statisticsDate[i] = re.sub(f'{str_regionExcelData}','{地域}',statisticsDate[i])
    statisticsDate[i] = re.sub(f'{str_productExcelData}', '{产品}', statisticsDate[i])

# print(statisticsDate)
# saveData(statisticsDate,savepath)
# #
unclean= []
clean = []
for i in range(len(statisticsDate)):
    if '{地域}'in statisticsDate[i]:
        clean.append(statisticsDate[i])
        continue
    elif '{产品}'in statisticsDate[i]:
        clean.append(statisticsDate[i])
        continue
    else:
        unclean.append(statisticsDate[i])


print(unclean)
print('-----------')
print(clean)


saveData(unclean,savepath)



