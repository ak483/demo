import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['https://www.zhihu.com/topics']
    start_urls = ['http://https://www.zhihu.com/topics/']

    def parse(self, response):

        data_ids = response.css(
            'body > div.zg-wrap.zu-main.clearfix > div.zu-main-content > div > div > ul > li:attr(data-id)').extract()
