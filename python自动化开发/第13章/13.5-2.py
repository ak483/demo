# 获得手机屏幕分辨率x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

# 向上滑动
def swipeUp(t):
    local = getSize()
    x = int(local[0] * 0.5)
    y1 = int(local[1] * 0.75)
    y2 = int(local[1] * 0.25)
    driver.swipe(x, y1, x, y2, t)
	
# 向下滑动
def swipeDown(t):
    local = getSize()
    x = int(local[0] * 0.5)
    y1 = int(local[1] * 0.25)
    y2 = int(local[1] * 0.75)
    driver.swipe(x, y1, x, y2, t)
	
# 向左滑动
def swipLeft(t):
    local = getSize()
    x1 = int(local[0] * 0.75)
    y = int(local[1] * 0.5)
    x2 = int(local[0] * 0.05)
    driver.swipe(x1, y, x2, y, t)
	
# 向右滑动
def swipRight(t):
    local = getSize()
    x1 = int(local[0] * 0.05)
    y = int(local[1] * 0.5)
    x2 = int(local[0] * 0.75)
    driver.swipe(x1, y, x2, y, t)
