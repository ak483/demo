# 发送请求
import requests
# 将数据存入数据库
import MySQLdb
# 每次请求停1s，太快会被B站拦截。
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 连接数据库
# conn = MySQLdb.connect(host="localhost", user='root', password='admin', db='scholldatabase', charset='utf8')
conn = MySQLdb.connect('127.0.0.1', 'root', '159357', 'bilibili_comment', charset='utf8', port=3306)
cursor = conn.cursor()
# 预编译语句
sql = "insert into bilibili_comment_221029(rpid,root,name,avatar,content) values (%s,%s,%s,%s,%s)"


# 爬虫类（面向对象）
class JsonProcess:
    def __init__(self):
        self.Json_data = ''
        # 请求头
        self. headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            'cookie':''
        }

    # 发送爬取请求
    def spider(self, URL):
        url = URL
        time.sleep(2)
        response = requests.get(url, headers=self.headers, verify=False)
        response.encoding = 'utf-8'
        self.Json_data = response.json()['data']['replies']


# 爬取子评论
def getSecondReplies(root):
    reply = JsonProcess()
    # 页数
    pn = 1
    # 不知道具体有多少页的评论，所以使用死循环一直爬
    while True:
        # url = f'https://api.bilibili.com/x/v2/reply/reply?jsonp=jsonp&pn={pn}&type=1&oid=979849123&ps=10&root={root}&_=1647581648753'
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=813782653&pn={pn}&ps=10&root={root}&type=1'#big马哈鱼
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=714952791&pn={pn}&ps=10&root={root}&type=1'#MZM
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=462256305&pn={pn}&ps=10&root={root}&type=1' #Big马厚涂研究室
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=855791344&pn={pn}&ps=10&root={root}&type=1'  # 抖抖村
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=805456319&pn={pn}&ps=10&root={root}&type=1'  # 东馆日常
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=288756707&pn={pn}&ps=10&root={root}&type=1'  # CG伊绘
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=292709736&pn={pn}&ps=10&root={root}&type=1'  # CG伊绘——镭射效果是怎么做出来的？
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=808870443&pn={pn}&ps=10&root={root}&type=1'  # 光翼学院公开课
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61236f69da2eb272cc49699d77d3d449&oid=671588373&pn={pn}&ps=10&root={root}&type=1'  # quan
        # url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61531f3cc3db67c2072fbf766d93a222&oid=758879239&pn={pn}&ps=10&root={root}&type=1'  # 插画教程
        url = f'https://api.bilibili.com/x/v2/reply/reply?csrf=61531f3cc3db67c2072fbf766d93a222&oid=380939825&pn={pn}&ps=10&root={root}&type=1'  # 轻微课

        # 没爬一次就睡1秒
        time.sleep(2)
        reply.spider(url)
        # 如果当前页为空（爬到头了），跳出子评论
        if reply.Json_data is None:
            break
        # 组装数据，存入数据库
        for node in reply.Json_data:
            rpid = node['rpid']
            name = node['member']['uname']
            avatar = node['member']['avatar']
            content = node['content']['message']
            data = (rpid, root, name, avatar, content)
            try:
                cursor.execute(sql, data)
                conn.commit()
            except:
                pass
            print(rpid, ' ', name, ' ', content, ' ', avatar, ' ', root)
        # 每爬完一次，页数加1
        pn += 1


# 爬取根评论
def getReplies(jp, i):
    # 不知道具体有多少页的评论，所以使用死循环一直爬
    while True:
        # url = f'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={i}&type=1&oid=805456319&mode=3&plat=1&_=1647577851745'
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=813782653&plat=1&type=1'#big马哈鱼
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=714952791&plat=1&type=1'#MZM
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=462256305&plat=1&type=1'#Big马厚涂研究室
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=855791344&plat=1&type=1'  # 抖抖村
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=805456319&plat=1&type=1'  # 东馆日常
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=288756707&plat=1&type=1'  # CG伊绘
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=292709736&plat=1&type=1'  # CG伊绘——镭射效果是怎么做出来的？
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=808870443&plat=1&type=1'  # 光翼学院公开课
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61236f69da2eb272cc49699d77d3d449&mode=3&next={i}&oid=671588373&plat=1&type=1'  # quan
        # url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61531f3cc3db67c2072fbf766d93a222&mode=3&next={i}&oid=758879239&plat=1&type=1'  # 插画教程
        url = f'https://api.bilibili.com/x/v2/reply/main?csrf=61531f3cc3db67c2072fbf766d93a222&mode=3&next={i}&oid=380939825&plat=1&type=1'  # 轻微课
        jp.spider(url)
        # 如果当前页为空（爬到头了），跳出循环，程序结束。
        # print(len(jp.Json_data))
        if len(jp.Json_data) == 0:

            break
        # 组装数据，存入数据库。
        for node in jp.Json_data:
            print('===================')
            rpid = node['rpid']
            name = node['member']['uname']
            avatar = node['member']['avatar']
            content = node['content']['message']
            data = (rpid, '0', name, avatar, content)
            try:
                cursor.execute(sql, data)
                conn.commit()
                print('存储成功')
            except:
                print('存入失败')
                pass
            print(rpid, ' ', name, ' ', content, ' ', avatar)
            # 如果有子评论，爬取子评论
            if node['replies'] is not None:
                print('>>>>>>>>>')
                getSecondReplies(rpid)
        # 每爬完一页，页数加1
        i += 1
        print(i)


if __name__ == '__main__':
    JP = JsonProcess()
    getReplies(JP, 1)
    print('\n================存储完成================\n')
    conn.close()

