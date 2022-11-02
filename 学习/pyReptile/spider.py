# coding=utf-8
'''
数据爬取方式由URL地址的数据格式决定，如果URL地址的数据格式为列表，
pyReptile就会执行异步并发，并将所有请求的响应内容以列表格式返回；
如果传入的URL地址是字符串格式（即单一的URL地址），
pyReptile就直接返回相应的响应内容；
并且还支持URL去重和分布式爬虫功能。
'''
import asyncio
import aiohttp
import redis

TIMEOUT = 40

REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
}

#实例化对象，用于发送http请求
loop = asyncio.get_event_loop()

#定义装饰器，实现URL去重或分布式处理
def distributes(func):#分发
    def wrapper(self,url,**kwargs):#封装
        redis_host = kwargs.get('redis_host', '')
        if redis_host:
            port = kwargs.get('port',6379)
            db = kwargs.get('db',1)
            redis_db = redis.Redis(host=redis_host,port=port,db=db)
            redis_data_dict = 'keys'
            if not redis_db.hexists(redis_data_dict,url):
                redis_db.hest(redis_data_dict,url,0)
                return func(self,url,**kwargs)
            else:
                return {}
        else:
            return  func(self,url,**kwargs)
    return wrapper()

#定义爬虫类
class Request(object):
    #定义异步get函数
    async def httpGet(self, url, **kwargs):
        cookies = kwargs.get('cookies', {})
        params = kwargs.get('params', {})
        proxy = kwargs.get('proxy', '')
        timeout = kwargs.get('timeout',TIMEOUT)
        headers = kwargs.get('headers', REQUEST_HEADERS)
        #带代理
        if proxy:
            async with aiohttp.ClientSession(cookies=cookies)as session:
                async with session.get(url, params=params,proxy=proxy,timeout=timeout,
                                       headers=headers)as response:
                    result = dict(
                        content=await  response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result
        #不带代理ip
        else:
            async with aiohttp.ClientSession(cookies=cookies)as session:
                async with session.get(url,params=params,timeout=timeout,
                                       headers=headers)as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result


    #定义异步post函数
    async def httpsPost(self,url,**kwargs):
        cookies = kwargs.get('cookies', {})
        data = kwargs.get('data', {})
        proxy = kwargs.get('proxy', '')
        timeout = kwargs.get('timeout', TIMEOUT)
        headers = kwargs.get('headers', REQUEST_HEADERS)
        # 带代理
        if proxy:
            async with aiohttp.ClientSession(cookies=cookies)as session:
                async with session.get(url, data=data, proxy=proxy, timeout=timeout,
                                       headers=headers)as response:
                    result = dict(
                        content=await  response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result
        # 不带代理ip
        else:
            async with aiohttp.ClientSession(cookies=cookies)as session:
                async with session.get(url, data=data, timeout=timeout,
                                       headers=headers)as response:
                    result = dict(
                        content=await response.read(),
                        text=await response.text(),
                        status=response.status,
                        headers=response.headers,
                        url=response.url
                    )
                    return result


    #定义GET请求方式
    @distributes
    def get(self, url, **kwargs):
        tasks = []
        if isinstance(url, list):
            for u in url:
                task = asyncio.ensure_future(self.httpGet(u,**kwargs))
                task.append(task)
            result = loop.run_until_complete(asyncio.gather(*tasks))
        else:
            result = loop.run_until_complete(self.httpsGet(url, **kwargs))
        return  result

        # 定义POST请求方式
        @distributes
        def post(self, url, **kwargs):
            tasks = []
            if isinstance(url, list):
                for u in url:
                    task = asyncio.ensure_future(self.httpGet(u, **kwargs))
                    task.append(task)
                result = loop.run_until_complete(asyncio.gather(*tasks))
            else:
                result = loop.run_until_complete(self.httpsPost(url, **kwargs))
            return result

#实例化Request对象

request = Request()


