import scrapy
from news1Pro.items import  News1ProItem


class ChinawaterSpider(scrapy.Spider):
    name = 'chinawater'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.chinawater.com.cn/newscenter/ly/zj']

    def parse(self, response):
    # 解析中国水利网的珠江流域新闻：标题：链接
        tr_list = response.xpath('/html/body/table/tr/td/div/div/div[1]/table/tr/td[2]/table/tr/td/table[3]/tr')
        for tr in tr_list:
            news_title = tr.xpath('.//td[1]/a/text()').extract_first()
            news_url = tr.xpath('.//td[1]/a/@href').extract_first()
            print(news_title,news_url)

            item = News1ProItem()
            item['news_title'] = news_title
            item['news_url'] = news_url

            yield item