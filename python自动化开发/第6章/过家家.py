import random
class Family():
    # 自定义初始化方法
    def __init__(self, surname, address, income):
        """ 设置家庭姓氏 """
        self.surname = surname
        self.address = address
        self.income = income

class Father(Family):
    def __init__(self, name, age):
        """ 继承父类的动态属性 """
        super(Family, self).__init__()
        # 定义动态属性
        self.name = name
        self.age = age
        self.__secret = '我外面有人'
    def action(self):
        money = random.randint(100, 1000)
        return money

class Mother(Family):
    def __init__(self, name, age):
        """ 继承父类的动态属性 """
        super(Family, self).__init__()
        # 定义动态属性
        self.name = name
        self.age = age
        self.__secret = '我存有很多私房钱'
    def action(self):
        money = random.randint(100, 500)
        return -money

class Son(Family):
    def __init__(self, name, age):
        """ 继承父类的动态属性 """
        super(Family, self).__init__()
        # 定义动态属性
        self.name = name
        self.age = age
        self.__secret = '我喜欢隔离的小花'
    def action(self):
        money = random.randint(0, 100)
        return -money

if __name__ == '__main__':
    # 将四个类实例化，生成对象
    family = Family('李', '广州市', 1000)
    father = Father('利海', 35)
    mother = Mother('郝玫丽', 33)
    son = Son('豪烨', 10)

    # 家庭的自我介绍
    print('这是一个姓' + family.surname + '的家庭，他们生活在' + family.address)
    print('我是父亲—' + family.surname + father.name + ',今年' + str(father.age) + '岁。')
    print('我是母亲—' + mother.name + ',今年' + str(mother.age) + '岁。')
    print('我是儿子—' + family.surname + son.name + ',今年' + str(son.age) + '岁。')

    # 家庭费用开支
    father_money = father.action()
    family.income += father_money
    print('父亲今天赚了' + str(father_money) + '元，家庭资产剩余' + str(family.income))
    mother_money = mother.action()
    family.income += mother_money
    print('母亲今天花了' + str(-mother_money) + '元，家庭资产剩余' + str(family.income))
    son_money = son.action()
    family.income += son_money
    print('儿子今天花了' + str(-son_money) + '元，家庭资产剩余' + str(family.income))

    # 家庭成员的小秘密
    print('父亲告诉你一个小秘密：' + father._Father__secret)
    print('母亲告诉你一个小秘密：' + mother._Mother__secret)
    print('儿子告诉你一个小秘密：' + son._Son__secret)
