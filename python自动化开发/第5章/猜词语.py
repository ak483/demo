import time
# 每组队伍的游戏过程
def guess(i):
    correct = 0
    start=time.time()
    for k in range(len(i)):
        # 显示词语
        print(('%d.%s') % (k + 1, i[k]))
        flag = input('请答题,答对请输入y,跳过请输入任意键')
        sec = time.time() - start
        # 统计用时
        if (50 <= sec <= 60):
            print('还有10秒钟')
        if (sec >= 60):
            print('时间到！游戏结束')
            break
        # 答对就累加1
        if (flag == 'y'):
            correct += 1
            continue
        else:
            continue
    return correct

# 遍历每组队伍，调用answer函数实现游戏
def team(guessWord):
    for i in guessWord:
        correct = guess(i)
        str_temp = ('恭喜你，你答对了%d道题') % (correct)
        print(str_temp)
        print('##############下一组##############')

# 主程序定义游戏内容，然后调用team函数开始游戏
if __name__ == '__main__':
    guessWord = []
    guessWord.append(['娇媚', '金鸡独立', '狼吞虎咽', '鹤立鸡群', '手舞足蹈', '卓别林', '穿越火线'])
    guessWord.append(['扭秧歌', '偷看美女', '大摇大摆', '回眸一笑', '市场营销', '自恋', '处女座'])
    guessWord.append(['狗急跳墙', '捧腹大笑', '目不转睛', '愁眉苦脸', '暗恋', '臭袜子', '趁火打劫'])
    team(guessWord)
