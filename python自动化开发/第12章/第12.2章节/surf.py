import cv2
# 读取图片
img = cv2.imread('logo.png')
# 定义SURF对象，参数float(1000)为阈值，阈值越高，识别的特征越小。
surf = cv2.xfeatures2d.SURF_create(float(1000))
# 检测关键点并计算描述符
# 描述符是对关键点的描述，可用于图片匹配
keypoints, descriptor = surf.detectAndCompute(img, None)

# 将关键点勾画到图片上
flags = cv2.DRAW_MATCHES_FLAGS_DEFAULT
color = (0, 255, 0)
img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints, flags=flags, color=color)

# 显示图片
cv2.imshow('surf_keypoints', img)
cv2.waitKey()