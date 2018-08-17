from queue import Queue
from threading import Thread
import logging
import random
import sys

sys.path.append('../')

from util import check_proxy
from getproxy import GetProxy
from myThread import CheckThread
from dbapi import SqliteOpt
from config import MY_USER_AGENTS,TARGETS

logging.basicConfig(level=logging.INFO)

class Client(GetProxy):
    def __init__(self):
        super().__init__()
        self.new_funcs = [self.xici_ip,self.kuai_ip]
        self._add_func()

    def _add_func(self):
        for func in self.new_funcs:
            self.funcs.append(func)

    @GetProxy.request_url(TARGETS['xici'])
    def xici_ip(self,soup):   #西刺代理
        tags = soup.find_all('tr')[1:]
        return tags

    @GetProxy.request_url(TARGETS['kuai'])
    def kuai_ip(self,soup):  #快代理
        tags = soup.find_all('tr')[1:]
        return tags
               
class SqliteClient(SqliteOpt,Client):

    def __init__(self,db,tbname):        
        SqliteOpt.__init__(self,db,tbname)
        Client.__init__(self)

    def insert_proxy(self,proxy):
        self.insert(proxy)

    def new_proxies(self):
        '''初始化，删除表中原有数据，获取最新可用代理'''
        self.delete()
        self.init_pool()
        self.commit()

    def more_proxies(self):
        '''爬取代理，并存入数据库'''
        self.init_pool()
        self.commit()

    def get_randproxy(self,protocol='http'):
        try:
            randproxy = random.choice(self.sel_proxies(protocol=protocol.upper()))
            ip,*arg = randproxy
            #self.delete(ip=ip)
            self.commit()
            return randproxy[2].lower() + '://'+':'.join(randproxy[:2])
        except IndexError:
            print('no more this type proxies!')

    def insert_proxy(self,proxy):
        self.insert(proxy)
  
if __name__ == '__main__':
    slt = SqliteClient('proxies.db','proxy')
        
