import logging
import random

from getproxy import GetProxy
from dbapi import SqliteOpt,SqliteDb
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
        self.db.commit()

    def more_proxies(self):
        '''爬取代理，并存入数据库'''
        self.init_pool()
        self.db.commit()

    def get_randproxy(self,protocol='http'):
        try:
            self.randproxy = random.choice(self.sel_proxies(protocol=protocol.upper()))
        except IndexError:
            print('no more this type proxies!')
            self.new_proxies()
            self.randproxy = random.choice(self.sel_proxies(protocol=protocol.upper()))
        self.ip, *arg = self.randproxy
        return self.randproxy[2].lower() + '://' + ':'.join(self.randproxy[:2])

# __name__ = '__main__'
if __name__ == '__main__':
    db = SqliteDb('proxies.db')
    a = SqliteOpt(db,'proxy')