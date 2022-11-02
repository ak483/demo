import flask
from flask import redirect
import requests

server = flask.Flask(__name__)  # __name__代表当前的python文件，把当前这个python文件，当成一个服务

client_key = 'awvm59ryigkr44zq'  # str | 应用唯一标识
client_secret = '23ba91dce68d74a91a3238944356d6f3'


@server.route('/login', methods=['get'])
def login():
    # create an instance of the API class
    response_type = 'code'  # str | 设置为'code'这个字符串即可
    scope = 'following.list,fans.list'  # str | 应用授权作用域,多个授权作用域以英文逗号（,）分隔
    redirect_uri = 'https://sdk.cjunshu.com'  # str | 授权成功后的回调地址，必须以http/https开头。域名必须对应申请应用时填写的域名，如不清楚请联系应用申请人。
    state = 'state_example'  # str | 用于保持请求和回调的状态 (optional)
    url = 'https://open.douyin.com/platform/oauth/connect?client_key=%s&response_type=%s&scope=trial.whitelist,%s&redirect_uri=%s' % (
        client_key, response_type, scope, redirect_uri)
    return redirect(url)


@server.route('/', methods=['get'])
def index():
    url = 'https://open.douyin.com/oauth/access_token/ '
    code = flask.request.args.get('code')
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'client_secret': client_secret,
        'code': code,
        'client_key': client_key,
        'grant_type': 'authorization_code'
    }
    response_data = requests.post(url=url, data=data, headers=headers).json()

    # access_token = response_data['data']['access_token']
    # print('问客服'+access_token)
    # open_id = response_data['data']['open_id']
    # print('问客22222服'+open_id)
    # url2 = 'https://open.douyin.com/oauth/userinfo/'
    # headers2 = {
    #     'Content-Type': 'application/json',
    #     'access-token': access_token
    # }
    # data2 = {
    #     'access_token': access_token,
    #     'open_id': open_id
    # }
    # response = requests.post(url=url2, data=data2, headers=headers2).json()

    open_id = response_data['data']['open_id']
    access_token = response_data['data']['access_token']
    url3 = 'https://open.douyin.com/fans/list?count=%s&open_id=%s' % ('10', open_id)
    headers3 = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'access-token': access_token
    }
    response = requests.get(url=url3, headers=headers3).json()

    # print(response)

    # url4 = 'https://open.douyin.com/fans/list?count=%s&open_id=%s' % ('20',open_id)
    # headers4 = {
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'access-token': access_token
    # }
    # response = requests.get(url=url4,headers=headers4).json()

    return response


# 端口号要是不指定，默认为5000.debug=True,改了代码之后不用重启，会自动重启一次。后面增加host='0.0.0.0'，别人可以访问
server.run(port=9999, debug=True, host='0.0.0.0')