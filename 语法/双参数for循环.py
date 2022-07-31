if __name__ == '__main__':
    # zip函数
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]
    p = zip(a, b)
    for x in p:
        print(x)
    '''结果
        (1, 4)
        (2, 5)
        (3, 6)
    '''
    w=zip(a,c)
    for x in w:
        print(w)

    '''结果
    <zip object at 0x000001D629E1F108>
    <zip object at 0x000001D629E1F108>
    <zip object at 0x000001D629E1F108>
    '''
    #     两个参数,谁先结束了,循环也就结束了
    for x,c in zip(range(0,6),range(0,5)):
        print(x,c)

    '''结果
    0 0
    1 1
    2 2
    3 3
    4 4
    '''
