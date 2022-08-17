from pywinauto.application import Application
from pywinauto.keyboard import SendKeys
import time
import os
# 获取文件夹的所有txt文件路径
def file_name(file_dir):
    temp = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                temp.append(os.path.join(root, file))
    return temp
file_path = r'C:\Users\000\Desktop\article'
file_list = file_name(file_path)

for i in file_list:
    word_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
    app = Application(backend='uia').start(word_path)
    # 绑定连接Word窗口
    dlg_spec = app.window(class_name='OpusApp')
    # dlg_spec.print_control_identifiers()
    # 点击打开空白文档
    dlg_spec.空白文档ListItem.click_input()

    # 撰写新闻标题，并设置格式
    dlg_spec.加粗.click_input()
    # 设置双击
    dlg_spec.增大字号.click_input(double=True)
    dlg_spec.居中.click_input()
    title = i.split('\\')[-1].split('.')[0]
    dlg_spec.Edit.type_keys(title)
    time.sleep(0.2)

    # 换行并设置正文内容格式
    SendKeys('{ENTER}')
    dlg_spec.加粗.click_input()
    time.sleep(1)
    # 设置双击
    dlg_spec.缩小字号.click_input(double=True)
    time.sleep(1)
    dlg_spec.左对齐.click_input()
    # 输入正文内容
    f = open(i, 'r')
    text = f.read()
    f.close()
    for k in text.split('\n'):
        # 判断内容是否为空
        if k.strip():
            SendKeys('{TAB}')
            dlg_spec.Edit.type_keys(k.strip())
            SendKeys('{ENTER}')
            time.sleep(0.2)

    # 插入图片
    dlg_spec.居中.click_input()
    dlg_spec.插入.click_input()
    # 重新捕捉软件控件信息
    # dlg_spec.print_control_identifiers()
    dlg_spec['图片...Button'].click_input()
    # 进入图片对话框
    fileDialog = dlg_spec.child_window(title='插入图片')
    # 查看子窗口控件信息
    # fileDialog.print_control_identifiers()
    # 设置等待时间，等待文件选择框出现
    fileDialog.wait('enabled', timeout=300)
    # 判断文件选择框是否出现
    if fileDialog.is_enabled():
        pic_path = r'C:\Users\000\Desktop\article\logo.jpg'
        fileDialog.Edit.set_edit_text(pic_path)
        fileDialog.SplitButton2.click_input()


    # 文件另存为
    dlg_spec['“文件”选项卡Button'].click_input()
    # 查看窗口控件变化情况
    # dlg_spec.print_control_identifiers()
    dlg_spec.另存为ListItem.click_input()
    dlg_spec.桌面ListItem.click_input()
    dlg_spec['保存(S)Button'].click_input()
    # 关闭Word文档
    dlg_spec.关闭Button3.click_input()




