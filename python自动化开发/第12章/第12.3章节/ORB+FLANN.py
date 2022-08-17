import cv2
""" 实现过程1 """
img1 = cv2.imread('QQ.png')
img2 = cv2.imread('portrait.png')
# 使用ORB算法获取图像特征的关键点和描述符
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

""" 实现过程2 """
# 定义FLANN匹配器
indexParams = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=2)
searchParams = dict(checks=100)
flann = cv2.FlannBasedMatcher(indexParams, searchParams)
# 使用 KNN 算法实现图像匹配，并对匹配结果排序
matches = flann.knnMatch(des1, des2, k=2)
# 清洗匹配结果
matches_temp = []
for i in matches:
    if len(i) == 2:
        matches_temp.append(i)
matches = sorted(matches_temp, key=lambda x: x[0].distance)

""" 实现过程3 """
# 去除错误匹配，0.5是系数，系数大小不同，匹配的结果也不同
goodMatches = []
for m, n in matches:
    if m.distance < 0.5 * n.distance:
        goodMatches.append(m)

""" 实现过程4 """
# 获取某个点的坐标位置
index = int(len(goodMatches)/2)
x, y = kp1[goodMatches[index].queryIdx].pt
# 将坐标位置勾画在QQ.png图片并显示图片
cv2.rectangle(img1, (int(x), int(y)), (int(x) + 5, int(y) + 5), (0, 255, 0), 2)
cv2.imshow('QQ', img1)
cv2.waitKey()