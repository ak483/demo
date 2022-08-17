# 导入Flask
from flask import Flask
from flask import request
# 创建一个Flask实例
app = Flask(__name__)

# 设置路由地址，即网页地址，也称为url
@app.route('/')
# url的处理函数
def hello_world():
    # 返回的网页
    return 'Hello World!'

# 路由地址：http://127.0.0.1:5000/user/
@app.route('/user/', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return 'This is user center'
    else:
        return 'This is My center'

# 路由地址：http://127.0.0.1:5000/user/xxx
# xxx是任意内容
@app.route('/user/<types>', methods=['GET', 'POST'])
def userCenter(types):
    # 获取GET的请求参数
    if request.method == 'GET':
        name = request.args.get('name')
        password = request.args.get('password')
    # 获取POST的请求参数
    else:
        name = request.form.get('name')
        password = request.form.get('password')
    return "This is " + types + "Your name is " + name

# 响应内容为字符串
@app.route('/str')
def MyStr():
    return "The response is string!"

# 响应内容为Json
from flask import jsonify
@app.route('/Json')
def MyJson():
    json = {
        'response': 'Json'
    }
    return jsonify(json)
    # 等价于
    # return jsonify(response='Json')

# 响应内容为HTML文件
from flask import render_template
@app.route('/html')
def MyHtml():
    name = 'Python Flask'
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
