# -*- codeing = utf-8 -*-
# @Time :2022/7/6 16:09
# @Author:Eric
# @File : big_topic.py
# @Software: PyCharm

import requests

cookies = {
    '_zap': '9c9bfd14-f05c-4016-9036-aa49c45d8099',
    'd_c0': '"AGDQNY5WKxSPTgJ4TAoRglP1j0ZMwg2KWKE=|1639285754"',
    '_9755xjdesxxd_': '32',
    'YD00517437729195%3AWM_TID': 'BAjnzjFt9YBBBBFUQEd%2B4%2FhCntpaCe2v',
    '__snaker__id': 'pQQjFDvtJ6va6Mbk',
    '_xsrf': '29ea3983-d129-4db0-a3d3-a5d3ea851f96',
    'q_c1': 'af26b405ada0427db3d355eaf527924a|1652172046000|1652172046000',
    '__utmz': '51854390.1652285689.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/532176205',
    '__utmc': '51854390',
    'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1655012694',
    'tst': 'r',
    'SESSIONID': 'abD6VPX7NkX8zjk9N5WkA1gZddlP4g1pk8FsrS7lmfQ',
    'osd': 'VlAXAE7TKB1wqH8MNtTlRxGD1S4kvkBYQP8jXgCcT09J1BRrBQQs3xWleQcxOhpPItjeOVDbXp3tEsHWC-eZZwk=',
    'JOID': 'VF4SA0LRJhhzpH0CM9fpRR-G1iImsEVbTP0tWwOQTUFM1xhpCwEv0xerfAQ9OBRKIdTcN1XYUp_jF8LaCemcZAU=',
    'q_c1': 'af26b405ada0427db3d355eaf527924a|1657081817000|1652172046000',
    'YD00517437729195%3AWM_NI': 'd9DcQPDzq73HEl57KdHjDx9z0CyhUhtfMgia3xBUw%2FFzMuOc776qt5uByWhkLZh4rJASXKxEBCudG7843n%2BZUI6n3%2B91Wtd%2FPrlJXr%2Bpng1YFM6Kv%2Fa%2BpQvi91BImKfgZVA%3D',
    'YD00517437729195%3AWM_NIKE': '9ca17ae2e6ffcda170e2e6eed3e47cb393af95d74b8f968eb3d14e929a8bacd85ab2969891d63baa889f88b82af0fea7c3b92aa8e78c84d45c88a6bfd8b24487b4fbd8ca708cb68c99bc72f49db789d864b8ba8388ec6bf1a88eb6f62586a68396ce69f5e9fa92f73fb79eb7b8eb619086a8d5f142838d98acfb4f829dbb85c63dfcecfd8faa529797fa8fb221fbef9995e72594aea4abdb7ae9b0a288b4538693faacf525a3f5c0b2f563fbef8eaaf041a6b996b7c437e2a3',
    'l_n_c': '1',
    'n_c': '1',
    '__utmv': '51854390.000--|2=registration_date=20160417=1^3=entry_date=20220510=1',
    '__utma': '51854390.722443503.1652285689.1657083232.1657094005.4',
    '__utmb': '51854390.0.10.1657094005',
    'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1657094040',
    'captcha_session_v2': '2|1:0|10:1657094042|18:captcha_session_v2|88:czFDVXhhZ0ZSSzhuZnY3eVBwNzJSWFhyTDVzZW5oM0J0WStjelV6amxtSlRWRUUxOXRUNFdENTlMSUNmWDJxeA==|22a4b0f709597d787dda4c3b5c58662c2698f6c2cd0aa73fa5a54c65cc27d0c3',
    'gdxidpyhxdE': '68o6zYkOhocdPRXfrZ%2FSulSGbfc4Z3x8Sz05czqZPtJ6CYnflKvNM6iBBi%2BfTKUUg0eIa81fMwEYdLPikhj%2BEnDup5sgPEEqEOI7xlEygqZw1QHkyakLnOZJh13heRdWBkUQLAo%2BswDTYs8N7sG9UJ1sOX9YLGGSDAUqxW%5Ciw%5C%2BoLmR4%3A1657096570812',
    'l_cap_id': '"N2NiYmY3NzVkMGM3NGM4NTg2ZTgzNGQzMzE4NWEwZTI=|1657095869|7148b04b19c655fb3046115a8128d286c50af658"',
    'r_cap_id': '"NTk5ZTNmN2VkMjAzNDk1MjlkYjgzMzVkMzY2MjdkYTk=|1657095869|7bd83d2262df27c3357e38ea896a5bf0307bbabf"',
    'cap_id': '"N2M3Yzk1Mjg5M2YzNGFjZDhhOGNkY2MzNDc4NjgxNmE=|1657095868|1e6cb4e356c5e9091caa4c94eb897cec637f9e8c"',
    'KLBRSID': '9d75f80756f65c61b0a50d80b4ca9b13|1657095988|1657081803',
}

headers = {
    'authority': 'www.zhihu.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_zap=9c9bfd14-f05c-4016-9036-aa49c45d8099; d_c0="AGDQNY5WKxSPTgJ4TAoRglP1j0ZMwg2KWKE=|1639285754"; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=BAjnzjFt9YBBBBFUQEd%2B4%2FhCntpaCe2v; __snaker__id=pQQjFDvtJ6va6Mbk; _xsrf=29ea3983-d129-4db0-a3d3-a5d3ea851f96; q_c1=af26b405ada0427db3d355eaf527924a|1652172046000|1652172046000; __utmz=51854390.1652285689.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/532176205; __utmc=51854390; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1655012694; tst=r; SESSIONID=abD6VPX7NkX8zjk9N5WkA1gZddlP4g1pk8FsrS7lmfQ; osd=VlAXAE7TKB1wqH8MNtTlRxGD1S4kvkBYQP8jXgCcT09J1BRrBQQs3xWleQcxOhpPItjeOVDbXp3tEsHWC-eZZwk=; JOID=VF4SA0LRJhhzpH0CM9fpRR-G1iImsEVbTP0tWwOQTUFM1xhpCwEv0xerfAQ9OBRKIdTcN1XYUp_jF8LaCemcZAU=; q_c1=af26b405ada0427db3d355eaf527924a|1657081817000|1652172046000; YD00517437729195%3AWM_NI=d9DcQPDzq73HEl57KdHjDx9z0CyhUhtfMgia3xBUw%2FFzMuOc776qt5uByWhkLZh4rJASXKxEBCudG7843n%2BZUI6n3%2B91Wtd%2FPrlJXr%2Bpng1YFM6Kv%2Fa%2BpQvi91BImKfgZVA%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed3e47cb393af95d74b8f968eb3d14e929a8bacd85ab2969891d63baa889f88b82af0fea7c3b92aa8e78c84d45c88a6bfd8b24487b4fbd8ca708cb68c99bc72f49db789d864b8ba8388ec6bf1a88eb6f62586a68396ce69f5e9fa92f73fb79eb7b8eb619086a8d5f142838d98acfb4f829dbb85c63dfcecfd8faa529797fa8fb221fbef9995e72594aea4abdb7ae9b0a288b4538693faacf525a3f5c0b2f563fbef8eaaf041a6b996b7c437e2a3; l_n_c=1; n_c=1; __utmv=51854390.000--|2=registration_date=20160417=1^3=entry_date=20220510=1; __utma=51854390.722443503.1652285689.1657083232.1657094005.4; __utmb=51854390.0.10.1657094005; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1657094040; captcha_session_v2=2|1:0|10:1657094042|18:captcha_session_v2|88:czFDVXhhZ0ZSSzhuZnY3eVBwNzJSWFhyTDVzZW5oM0J0WStjelV6amxtSlRWRUUxOXRUNFdENTlMSUNmWDJxeA==|22a4b0f709597d787dda4c3b5c58662c2698f6c2cd0aa73fa5a54c65cc27d0c3; gdxidpyhxdE=68o6zYkOhocdPRXfrZ%2FSulSGbfc4Z3x8Sz05czqZPtJ6CYnflKvNM6iBBi%2BfTKUUg0eIa81fMwEYdLPikhj%2BEnDup5sgPEEqEOI7xlEygqZw1QHkyakLnOZJh13heRdWBkUQLAo%2BswDTYs8N7sG9UJ1sOX9YLGGSDAUqxW%5Ciw%5C%2BoLmR4%3A1657096570812; l_cap_id="N2NiYmY3NzVkMGM3NGM4NTg2ZTgzNGQzMzE4NWEwZTI=|1657095869|7148b04b19c655fb3046115a8128d286c50af658"; r_cap_id="NTk5ZTNmN2VkMjAzNDk1MjlkYjgzMzVkMzY2MjdkYTk=|1657095869|7bd83d2262df27c3357e38ea896a5bf0307bbabf"; cap_id="N2M3Yzk1Mjg5M2YzNGFjZDhhOGNkY2MzNDc4NjgxNmE=|1657095868|1e6cb4e356c5e9091caa4c94eb897cec637f9e8c"; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1657095988|1657081803',
    'pragma': 'no-cache',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.get('https://www.zhihu.com/topics', cookies=cookies, headers=headers)
print(response.text)