from __future__ import print_function
import time
from pprint import pprint
import  requests

# create an instance of the API class
client_key = 'awvm59ryigkr44zq' # str | 应用唯一标识
response_type = 'code' # str | 设置为'code'这个字符串即可
scope = 'user_info' # str | 应用授权作用域,多个授权作用域以英文逗号（,）分隔
redirect_uri = 'http://sdk.cjunshu.com' # str | 授权成功后的回调地址，必须以http/https开头。域名必须对应申请应用时填写的域名，如不清楚请联系应用申请人。
state = 'state_example' # str | 用于保持请求和回调的状态 (optional)
url= 'https://open.douyin.com/platform/oauth/connect?client_key=%s&response_type=%s&scope=%s&redirect_uri=%s'%(client_key,response_type,scope,redirect_uri)

response = requests.get(url)
print(response)



