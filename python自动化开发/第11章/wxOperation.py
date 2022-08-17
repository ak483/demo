from pywinauto.application import Application
import time
# 实例化Application并连接wxGUI软件
app = Application(backend='win32')
dlg = app.connect(title_re='Pywinauto*', class_name_re='wxWindowNR*')
# 连接软件的主窗口
dlg_spec = dlg.window(title_re='Pywinauto', class_name='wxWindowNR')
# 输出软件窗口的控件信息
dlg_spec.print_control_identifiers()
# 设置焦点，激活软件窗口
dlg_spec.set_focus()
# 文本框输入数据
dlg_spec['姓名Edit'].type_keys('张三')
dlg_spec.姓名Edit.set_edit_text('小黄')
# 获取文本框数据
print('文本框数据：', dlg_spec.Edit.window_text())
print('文本框数据：', dlg_spec.Edit.text_block())
print('文本框数据：', dlg_spec.Edit.texts())
time.sleep(1)

# 依次点击单选框
dlg_spec.女RadioButton.click()
dlg_spec.男RadioButton.click_input()
# 读取单选框
print('单选框数据：', dlg_spec.女RadioButton.texts())
print('单选框数据：', dlg_spec.男RadioButton.window_text())
time.sleep(1)

# 选择下拉框ComboBox的数据（所在省份）
# 使用select()方法，参数是下拉列表的值或索引
dlg_spec.ComboBox.select(2)
dlg_spec.ComboBox.select('广东省')
# 获取下拉框ComboBox的数据
print('下拉框ComboBox的全部数据：', dlg_spec.ComboBox.texts())
# 获取当前下拉框所选的数据
print('当前下拉框所选的数据：', dlg_spec.ComboBox.window_text())
time.sleep(1)

# 选择下拉框ComboBox的数据（所在城市）
dlg_spec.ComboBox2.select(2)
# 在下拉框ComboBox写入数据
dlg_spec.ComboBox2.Edit2.set_edit_text('珠海市')
# 获取下拉框ComboBox的数据
print('下拉框ComboBox的全部数据：', dlg_spec.ComboBox2.texts())
# 获取当前下拉框所选的数据
print('当前下拉框所选的数据：', dlg_spec.ComboBox2.window_text())
time.sleep(1)

# 点击勾选框
dlg_spec.我已阅读有关事项Button.click()
dlg_spec.我已阅读有关事项Button.click_input()
# 读取勾选框数据
print('勾选框数据：', dlg_spec.我已阅读有关事项Button.window_text())
print('勾选框数据：', dlg_spec.我已阅读有关事项Button.texts())
time.sleep(1)
# 点击注册按钮
dlg_spec.注册Button.click()
dlg_spec.注册Button.click_input()
# 读取注册按钮数据
print('注册按钮数据：', dlg_spec.注册Button.window_text())
print('注册按钮数据：', dlg_spec.注册Button.texts())
time.sleep(1)

# 绑定连接提示框
msg = dlg.window(title_re='注册成功')
# 输出提示框的控件信息
msg.print_control_identifiers()
# 点击"是"按钮
msg['是(&Y)Button'].click()
