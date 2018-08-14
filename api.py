from queue import Queue
from threading import Thread
import logging

from util import check_proxy
from getproxy import getter
from myThread import CheckThread
from dbapi import SqliteOpt

logging.basicConfig(level=logging.INFO)

class Client():    
    def check(self,proxy):
        '''检查代理，存入数据库'''
        if check_proxy(proxy):
            #logging.info(proxy)
            try:
                self.insert_proxy(proxy)
            except:
                print('未存储')

    def insert_proxy(self,proxy):
        self.insert(proxy)
                
    def refresh_opool(self):
        '''爬取代理网站，并存入队列中'''
        getter()
        self.opool = getter.que
        
    def refresh(self):
        '''从队列中取出代理，多线证验证，通过的写入数据库中'''
        self.refresh_opool()
        tds = []
        while not self.opool.empty():
            proxy = self.opool.get()
            #logging.info(proxy)
            t = CheckThread(self.check,proxy)
            tds.append(t)
        for td in tds:
            td.start()
        for td in tds:
            td.join()
                
class SqliteClient(SqliteOpt,Client):

    def __init__(self,db,tbname):        
        SqliteOpt.__init__(self,db,tbname)
        Client.__init__(self)

    def new_proxies(self):
        '''初始化，删除表中原有数据，获取最新可用代理'''
        self.delete()
        self.refresh()
        self.commit()

    def more_proxies(self):
        '''爬取代理，并存入数据库'''
        self.refresh()
        self.commit()

if __name__ == '__main__':
    slt = SqliteClient('1.db','proxy')
    
        
