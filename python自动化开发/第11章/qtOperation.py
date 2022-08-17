from pywinauto.application import Application
import time
# 实例化Application并连接qtGUI软件
app = Application(backend='uia')
dlg = app.connect(title_re='Pywinauto', class_name='QMainWindow')
# 绑定qtGUI软件窗口
dlg_spec = dlg.window(title_re='Pywinauto', class_name='QMainWindow')
# 输出qtGUI软件的窗口信息
dlg_spec.print_control_identifiers()
# 设置焦点，使其处于活动状态
dlg_spec.set_focus()
# 文本框输入数据
dlg_spec.Edit0.set_edit_text('Hello Python')
dlg_spec['Edit0'].type_keys('Hi Python')
# 获取文本框数据内容
print('文本框数据：', dlg_spec['Edit0'].texts())
print('文本框数据：', dlg_spec['Edit0'].text_block())
print('文本框数据：', dlg_spec['Edit0'].window_text())
time.sleep(1)

# 点击单选框
dlg_spec.RadioButton0.select()
dlg_spec.RadioButton2.click_input()
# 读取单选框
print('单选框数据：', dlg_spec.RadioButton0.texts())
print('单选框数据：', dlg_spec.RadioButton0.window_text())
time.sleep(1)

""" 下拉框支持编辑 """
# 设置下拉框的可选值
dlg_spec.ComboBox.Edit.set_edit_text('浙江省')
""" 下拉框不支持编辑 """
# 在qtGUI.py设置self.comboBox.setEditable(False)可实现无法编辑
# 点击下拉框，打开下拉列表
# dlg_spec.ComboBox.click_input()
# 点击下拉列表某个值
# dlg_spec['浙江省'].click_input()
# 读取下拉框当前的数据
print('下拉框数据：', dlg_spec.ListBox.texts())
time.sleep(1)
# 输出：下拉框数据： [['广东省'], ['浙江省'], ['湖南省']]

# 读取并点击CheckBox勾选框
dlg_spec.CheckBox.click_input()
dlg_spec.CheckBox.click()
print('勾选框数据：', dlg_spec.CheckBox.texts())
print('勾选框数据：', dlg_spec.CheckBox.window_text())
time.sleep(1)

# 读取数据表的所有数据
print('数据表的所有数据：', dlg_spec.Table.children_texts())
index = 1
result = []
while 1:
    try:
        if dlg_spec['DataItem' + str(index)].texts() in result:
            break
        result.append(dlg_spec['DataItem' + str(index)].texts())
        index += 1
    except: break
print('数据表的表格数据', result)

# # 修改数据表表格数据
dlg_spec['DataItem'].click_input()
dlg_spec['DataItem'].type_keys('小黄')
time.sleep(1)

# 最大化、最小化和关闭按钮的操作
dlg_spec.TitleBar.最大化.click()
# dlg_spec.TitleBar.最小化.click()
# dlg_spec.TitleBar.关闭.click()

# 读取并点击关闭按钮
print('按钮数据：', dlg_spec.Button4.window_text())
print('按钮数据：', dlg_spec.Button4.texts())
dlg_spec.Button4.click_input()
# dlg_spec.Button4.click()
