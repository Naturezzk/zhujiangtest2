# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class News1ProPipeline:
    #专门处理items类型对象；该方法可以接收爬虫文件提交过来的item对象
    fp = None
    #重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫。。')
        self.fp = open('./chinawater.txt','w',encoding='utf-8')

    #专门处理items类型对象；该方法可以接收爬虫文件提交过来的item对象
    def process_item(self, item, spider):
        news_title = item['news_title']
        news_url = item['news_url']
        self.fp.write(news_title+':'+news_url+'\n')
        return item  #就会传递给下一个即将被执行的管道类

    def close_spider(self,spider):
        print('结束爬虫。。')
        self.fp.close()

class mysqlPipeline:
    #专门处理items类型对象；该方法可以接收爬虫文件提交过来的item对象
    conn = None
    cursor = None
    #重写父类的一个方法：该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',post=3306,user='localhost',password='1207081779',db='spidertest',charset = 'utf8mb4')

    #专门处理items类型对象；该方法可以接收爬虫文件提交过来的item对象
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into chinawater values("%s","%s")'%(item["new_title"],item["new_url"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
