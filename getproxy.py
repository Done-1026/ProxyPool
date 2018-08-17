import sqlite3
import re
import random
from queue import Queue
import os
import logging
import time
import threading
from functools import wraps

import requests
from bs4 import BeautifulSoup

from config import MY_USER_AGENTS,TARGETS
import util
from myThread import MyThread,CheckThread

logging.basicConfig(level=logging.INFO)

class GetProxy():
    _headers = {}
    _que = Queue()   
    funcs = []
        
    def __call__(self):
        self._get_proxy()

    @classmethod        
    def request_url(cls,info):       
        def request_params(get_ip):
            '''各个代理网站的参数，请求及存入队列写入'''
            @wraps(get_ip)
            def req(self):                
                for i in range(info[1]):
                    new_url = info[0] + str(i+1)
                    #logging.info(new_url)
                    self._headers['user-agent'] = random.choice(MY_USER_AGENTS)
                    resp = requests.get(new_url,headers=self._headers)
                    time.sleep(random.random())
                    resp.encoding = 'utf-8'
                    soup = BeautifulSoup(resp.content,'html.parser')
                    tags = get_ip(self,soup)  #元组(ip,port,type,protocol)
                    for tag in tags:
                        #logging.info(tag)
                        proxy = util.search(tag.text)
                        logging.info(proxy)                        
                        self._que.put(proxy)
            return req
        return request_params        
    
    def _get_proxy(self):
        '''爬取代理网站，存入属性que（Queue对象中）'''
        tds = []        
        for func in self.funcs:
            #logging.info(func.__name__)
            t = MyThread(func)
            tds.append(t)
        for td in tds:
            td.start()
        for td in tds:
            td.join()

    def _check(self,proxy):
        '''检查代理，存入数据库'''
        if util.check_proxy(proxy):
            #logging.info(proxy)
            try:
                self.insert_proxy(proxy)
            except:
                print('未存储')

    def insert_proxy(self,proxy):
        '''存入数据库方法，根据数据库不同变化，在子类中重写'''
        pass

    def _refresh(self):
        '''从队列中取出代理，多线证验证，通过的写入数据库中'''
        tds = []
        while not self._que.empty():
            proxy = self._que.get()
            #logging.info(proxy)
            t = CheckThread(self._check,proxy)
            tds.append(t)
        for td in tds:
            td.start()
        for td in tds:
            td.join()
    
    def init_pool(self):
        self._get_proxy()
        self._refresh()

if __name__ == '__main__':
    getter = GetProxy()
    #getter()
    

