import subprocess
import cv2
import pyautogui
import time
import os
# 获取文件夹的所有PDF文件路径
def file_name(file_dir):
    temp = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.pdf':
                temp.append(os.path.join(root, file))
    return temp

# 图像识别与定位
def get_position(local):
    # 将当前屏幕截图，作为目标图像
    pyautogui.screenshot('computer.png')
    img1 = cv2.imread('computer.png')
    img2 = cv2.imread(local)
    # 获取图像特征的关键点和描述符
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # 定义暴力匹配器
    bf = cv2.BFMatcher(normType=cv2.NORM_L1, crossCheck=True)
    # 使用暴力算法实现图像匹配，并对匹配结果排序
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)
    # 获取某个点的坐标位置
    index = int(len(matches) / 2)
    x, y = kp1[matches[index].queryIdx].pt
    return (x, y)

if __name__ == '__main__':
    # 运行Adobe Reader软件
    sf = r"C:\Program Files (x86)\Adobe\Reader\Reader\AcroRd32.exe"
    subprocess.Popen(sf)
    time.sleep(3)
    # 获取文件夹里面所有PDF文件
    file_path = r"C:\Users\000\Desktop\pdf"
    file_list = file_name(file_path)

    for f in file_list:
        # 点击“打开”图标
        position = get_position('open.png')
        pyautogui.click(x=position[0], y=position[1], interval=1)
        # 点击“我的电脑”图标
        position = get_position('myPC.png')
        pyautogui.click(x=position[0], y=position[1], interval=1)
        # 点击“浏览”图标
        position = get_position('browse.png')
        pyautogui.click(x=position[0], y=position[1], interval=1)
        # 输入PDF文件路径
        pyautogui.typewrite(f)
        # 点击“打开”按钮
        position = get_position('openFile.png')
        pyautogui.click(x=position[0], y=position[1], interval=1)
        # 点击“打印”图标，进入打印预览
        position = get_position('openPrint.png')
        pyautogui.click(x=position[0], y=position[1], interval=1)
        # 点击“打印”按钮
        position = get_position('print.png')
        pyautogui.click(x=position[0], y=position[1], interval=1)
        # 快捷键关闭当前PDF文档
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'w')