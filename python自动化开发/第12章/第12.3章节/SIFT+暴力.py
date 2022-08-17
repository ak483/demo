import cv2
""" 实现过程1 """
img1 = cv2.imread('QQ.png')
img2 = cv2.imread('portrait.png')
# 使用SIFT算法获取图像特征的关键点和描述符
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

""" 实现过程2 """
# 定义暴力匹配器
# BFMatcher函数参数：
# normType：NORM_L1, NORM_L2, NORM_HAMMING, NORM_HAMMING2。
# NORM_L1和NORM_L2是SIFT和SURF描述符的优先选择，NORM_HAMMING和NORM_HAMMING2是用于ORB算法
bf = cv2.BFMatcher(normType=cv2.NORM_L1, crossCheck=True)
# 使用暴力算法实现图像匹配，并对匹配结果排序
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

""" 实现过程3 """
# 获取某个点的坐标位置
index = int(len(matches)/2)
x, y = kp1[matches[index].queryIdx].pt
# 将坐标位置勾画在QQ.png图片并显示图片
cv2.rectangle(img1, (int(x), int(y)), (int(x) + 5, int(y) + 5), (0, 255, 0), 2)
cv2.imshow('QQ', img1)
cv2.waitKey()
