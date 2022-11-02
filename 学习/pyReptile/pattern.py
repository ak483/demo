'''
数据清洗采用Scrapy框架的清洗模式，
使用方式与Scrapy框架有一定的相似之处，
目前仅支持CssSelector和Xpath定位方式。
'''

from bs4 import BeautifulSoup
import lxml
from lxml.html.soupparser import fromstring as soup_parse

class DataPattern(object):
    def cssSelector(self,response,selector,**kwargs):
        parse = kwargs.get('parser', 'html.parse')
        tempList = []
        soup = BeautifulSoup(response,parser)
        temp = soup.select(selector=selector)
        for i in temp:
            tempList.append(i.getText())
        return tempList

    def xpath(self,response,selector,**kwargs):
        parser = kwargs.get('parser','html.parser')
        try:
            soup = soup_parse(response,features=parser)
        except:
            soup = lxml.html.fromstring(response)
        temp = soup.xpath(selector)
        tempList = []
        for i in temp:
            tempList.append(i.text)
        return tempList

DataPattern = DataPattern()