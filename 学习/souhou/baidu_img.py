# -*- coding: UTF-8 -*-"""
import requests
import tqdm


def configs(search, page, number):
    """

    :param search:
    :param page:
    :param number:
    :return:
    """
    url = 'https://image.baidu.com/search/acjson'
    params = {
        "tn": "resultjson_com",
        "logid": "11555092689241190059",
        "ipn": "rj",
        "ct": "201326592",
        "is": "",
        "fp": "result",
        "queryWord": search,
        "cl": "2",
        "lm": "-1",
        "ie": "utf-8",
        "oe": "utf-8",
        "adpicid": "",
        "st": "-1",
        "z": "",
        "ic": "0",
        "hd": "",
        "latest": "",
        "copyright": "",
        "word": search,
        "s": "",
        "se": "",
        "tab": "",
        "width": "",
        "height": "",
        "face": "0",
        "istype": "2",
        "qc": "",
        "nc": "1",
        "fr": "",
        "expermode": "",
        "force": "",
        "pn": str(60 * page),
        "rn": number,
        "gsm": "1e",
        "1617626956685": ""
    }
    return url, params


def loadpic(number, page):
    """

    :param number:
    :param page:
    :return:
    """
    while (True):
        if number == 0:
            break
        url, params = configs(search, page, number)
        result = requests.get(url, headers=header, params=params).json()
        url_list = []
        for data in result['data'][:-1]:
            url_list.append(data['thumbURL'])
        for i in range(len(url_list)):
            getImg(url_list[i], 60 * page + i, path)
            bar.update(1)
            number -= 1
            if number == 0:
                break
        page += 1
    print("\nfinish!")


def getImg(url, idx, path):
    """

    :param url:
    :param idx:
    :param path:
    :return:
    """
    img = requests.get(url, headers=header)
    file = open(path + 'maintenanceWorker_' + str(idx + 1) + '.jpg', 'wb')
    file.write(img.content)
    file.close()


if __name__ == '__main__':
    search = input("请输入搜索内容：")
    number = int(input("请输入需求数量："))
    path = 'E:\data\MaintenanceWorker/'
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    bar = tqdm.tqdm(total=number)
    page = 0
    loadpic(number, page)
