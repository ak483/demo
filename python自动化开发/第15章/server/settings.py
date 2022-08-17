from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babelex import Babel

# Flask实例化，生成对象app
app = Flask(__name__)
# 本地化，将Admin改为中文显示
babel = Babel(app)
# 设置app的配置信息
URI = 'mysql+pymysql://root:1234@localhost:3306/automation?charset=utf8'
app.config.update(
    # 设置SQLAlchemy连接数据库
    SQLALCHEMY_DATABASE_URI=URI,
    # 设置中文
    BABEL_DEFAULT_LOCALE='zh_CN',
    # 设置密钥值，用于Session、Cookies以及扩展模块
    SECRET_KEY='213sd4156s51',
	# 解决Json乱码
	JSON_AS_ASCII=False
)
# 将Flask与SQLAlchemy绑定
db = SQLAlchemy(app)

# 定义admin后台
admin = Admin(app, name='自动化管理系统', template_mode='bootstrap3')
