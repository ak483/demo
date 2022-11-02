def auth(func):
    def wrapper(*args, **kwargs):
        # 1、调用原函数
        # 2、为其增加新功能
        name = input('your name>>: ').strip()
        pwd = input('your password>>: ').strip()
        if name == 'egon' and pwd == '123':
            res = func(*args, **kwargs)
            return res
        else:
            print('账号密码错误')

    return wrapper
print('1')

@auth
def index():
    print('from index')
