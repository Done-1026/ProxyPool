import sqlite3
import re
import random
from queue import Queue
import os
import logging
import time
import threading

import requests
from bs4 import BeautifulSoup

from settings import MY_USER_AGENTS,TARGETS
from util import Util

logging.basicConfig(level=logging.INFO)

class GetProxyIp():
    headers = {}
    que = []


    def request_url(info):
        def request_params(get_ip):
            '''各个代理网站的参数，请求及存入队列写入'''
            def req(self):
                self.headers['user-agent'] = random.choice(MY_USER_AGENTS)
                for i in range(info[1]):
                    new_url = info[0] + str(i+1)
                    #logging.info(new_url)
                    resp = requests.get(new_url,headers=self.headers)
                    time.sleep(random.random())
                    resp.encoding = 'utf-8'
                    soup = BeautifulSoup(resp.content,'html.parser')
                    tags = get_ip(self,soup)  #元组(ip,port,type,protocol)
                    for tag in tags:
                        #logging.info(tag)
                        proxy = Util.search(tag.text)
                        logging.info(proxy)
                        self.que.append(proxy)
            return req
        return request_params        

    @request_url(TARGETS['xici'])
    def xici_ip(self,soup):
        '''西刺代理'''
        tags = soup.find_all('tr')[1:]
        return tags

    @request_url(TARGETS['kuai'])
    def kuai_ip(self,soup):
        '''快代理'''
        tags = soup.find_all('tr')[1:]
        return tags

    @staticmethod
    def thread_get_ip(self):
        funcs = [self.xici_ip,self.kuai_ip]
        for func in funcs:
            t = threading.Thread(target=func)
            t.start()

        
if __name__ == '__main__':
    getip = GetProxyIp()
