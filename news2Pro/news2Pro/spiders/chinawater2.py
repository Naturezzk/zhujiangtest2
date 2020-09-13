import scrapy
from news2Pro.items import News2ProItem

class Chinawater2Spider(scrapy.Spider):
    name = 'chinawater2'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://search.news.chinanews.com/']
    url = ['http://search.news.chinanews.com/search.do?q=珠江流域&dbtype=gx&ps=20&start=%d&time_scope=0&sort=pubtime']
    page_num = 0
    def parse(self, response):
        table_list = response.xpath('//*[@id="news_list"]/table')
        for table in table_list:
            news_title = table.xpath('./tr[1]/td[2]/ul/li[1]/a/text()').extract_first()
            news_url = table.xpath('./tr[1]/td[2]/ul/li[1]/a/@href').extract_first()
            print(news_title, news_url)

            item = News2ProItem()
            item['news_title'] = news_title
            item['news_url'] = news_url

            yield item  # 提交到管道

        if self.page_num <=80:
            new_url = format(self.url%self.page_num)
            self.page_num += 20
            # 手动请求发送
            yield scrapy.Request(url=new_url,callback=self.parse)
