# coding=utf-8
import xlwt


def save1():#保存账号数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('知乎', cell_overwrite_ok=True)
    col = ("数据日期", "账号", "所属平台", "发布量", "播放量", "点赞量", "点赞率", "评论量", "评论率", "转发量", "转发率", "关注量", "累计关注量")

    for i in range(0, 13):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist)):
        print("第%d条" % (i + 1))
        data = All_datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)  # 保存

def save2():#保存短视频数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('抖音', cell_overwrite_ok=True)
    col = ("数据日期", "视频标题", "所属账号", "所属平台", "发布日期", "发布天数", "播放量（总）", "完播率", "平均播放时长(s)", "点赞量（总）", "点赞率（点赞/播放）", "评论量（总）", "评论率（评论/播放）", "转发量（总）", "转发率（准发/播放）", "视频带粉数（总）")

    for i in range(0, 16):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(All_datalist1)):
        print("第%d条视频" % (i + 1))
        data = All_datalist1[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(savepath1)  # 保存