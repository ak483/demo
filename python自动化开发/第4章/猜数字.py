# 导入标准库random，实现随机数的生成
import random
number = random.randint(0, 20)
while 1:
    # 内置input函数是给用户提供数值的输入。
    # 由input函数是生成字符串，因此需要将字符串转换成数字。
    getNum = int(input('请输入你的数字：'))
    # 判断输入值和随机数的大小
    if getNum == number:
        # 判断成功就终止整个while循环
        print('恭喜你，你猜对了')
        break
    elif getNum > number:
        print('你的数字比结果大了')
    else:
        print('你的数字比结果小了')
