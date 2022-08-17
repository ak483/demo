import random
# 自定义异常类
class MuchError(Exception):
    pass
class Victory(Exception):
    pass

# 定义玩家与角色
player = ['小黄', '小黑', '小白', '小红']
role = ['女巫', '猎人', '狼人', '村民',
        '守卫', '长老', '预言家', '白狼王']
# 将玩家与角色的顺序打乱并匹配
player = random.sample(player, len(player))
role = random.sample(role, len(player))
print('游戏中全部身份有：' + '、'.join(role))
matching = {}
for t in range(len(player)):
    matching[player[t]] = role[t]

# 游戏逻辑
try:
    result, err = 0, 0
    for t in player:
        for i in range(2):
            guess = input('你认为' + t + '的身份是：')
            if guess == matching[t]:
                result += 1
                print('你猜对了')
                break
            else:
                err += 1
                print('猜错了，你还有'+ str(1-i) + '次机会')
        if err > 5:
            raise MuchError('错误次数已超出5次，游戏结束')

    if result == len(player):
        raise Victory('恭喜你，全部猜对了')

except MuchError as errInfo:
    print(errInfo)
