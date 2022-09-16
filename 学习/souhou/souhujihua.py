
# 引入requests和bs
import requests

# 使用headers是一种默认的习惯，默认你已经掌握啦~
# 发起请求，将响应的结果赋值给变量res。
url='https://cis.sohu.com/cisv4/feeds'



params = {
    'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].vessay_info;data[*].author.badge[?(type=best_answerer)].topics;data[*].author.vip_info',
    'offset': '10',
    'limit': '10',
    'sort_by': 'created'
}
headers={

    'Host': 'cis.sohu.com',
    'Referer': 'https://mp.sohu.com/profile?xpt=MWQ3MmMyZTktMDhkMy00N2I4LThmZTUtOGRjYmQ3YmRmMmE4',
    # 'referer': 'https://www.zhihu.com/org/yun-ban-gan-huo-jun/posts',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'cookie':'dnsenv=qcloud; reqtype=pc; gidinf=x099980109ee15828f210603c000d8cbac2e783a4444; clt=1658373900; cld=20220721112500; SUV=220721112500TGYV; user_id=01c09cbb9c821000; access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1aXMiLCJibGVuZF9pZCI6Ik1ERmpNRGxqWW1JNVl6Z3lNVEF3TUE9PS5jSEJoWnprNU1ERmpZbUl5T1RKak4wQnpiMmgxTG1OdmJRPT0iLCJpYXQiOjE2NjAyNzE2ODB9.jGQbY_2Sg829sl_8H4xyBAbUOUQbj6kMnZhHWYygaqU; BAIDU_SSP_lcr=https://www.baidu.com/link?url=v1n2EtKVJO-pXmVbLJJPd634cDxSb2BVIqFlFbMKq2e&wd=&eqid=a4ab1f0e0002073c0000000662f5bc67; IPLOC=CN4401; jv=d523b35ece4296079c8c29d0978379dd-VrWsth4e1662528882655; ppinf=2|1662528882|1663738482|bG9naW5pZDowOnx1c2VyaWQ6Mjg6MTE0MjA1NjAxMTY4ODI3MTg3MkBzb2h1LmNvbXxzZXJ2aWNldXNlOjMwOjAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMHxjcnQ6MTA6MjAyMi0wOS0wN3xlbXQ6MTowfGFwcGlkOjY6MTEzODA1fHRydXN0OjE6MXxwYXJ0bmVyaWQ6MTowfHJlbGF0aW9uOjA6fHV1aWQ6MTY6c2NjOGEyMGRjYzQyNWM5OXx1aWQ6MTY6c2NjOGEyMGRjYzQyNWM5OXx1bmlxbmFtZTowOnw; pprdig=02Ca3V07v-kiVLBOPOqHFAYXB0DDgFvpBfo-iggu46q8ZFYyE3koadoy1E1HCN5nJk1sAcnj6xRCT4XXRALvNH0AfcHOOqzHOeB0cBbD2eyhsv22SkdkJhnBOjEE8FMA9MJv4Vn337UlSNJ37Tkq0RHiMhG91J0PKk-vuJsYdHw; t=1663039026851; spinfo=c29odXwxMTQyMDU2MDExNjg4MjcxODcyQHNvaHUuY29tfDExNDIwNTYwMTE2ODgyNzE4NzI=; spsession=MTE0MjA1NjAxMTY4ODI3MTg3MnwtMXwxNjY1NjMxMDI3fDExNDIwNTYwMTE2ODgyNzE4NzJmZDM5Y2IwNw==-812amwua0tR9X6OZyU5NNtTyEzQ=; ppmdig=1663054137000000bbf1b6628369135b68ffee9a44fcfbfe'
}

res = requests.post(url, headers=headers).text
# 检查状态码
print(res)
# print(res.status_code)