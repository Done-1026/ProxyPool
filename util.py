import re
import logging
import requests
import logging

from settings import RULES,TESTURLS

logging.basicConfig(level=logging.INFO)

def search(string):
    proxy = []
    for k,v in RULES.items():
        proxy.append(v.search(string).group())
    return tuple(proxy)

def check_proxy(oproxy):
    '''proxy = (ip,port,protocol,type)'''
    #logging.info(oproxy)
    proxy = {oproxy[2].lower() :'%s://%s:%s'%(oproxy[2].lower(),oproxy[0],oproxy[1])}
    #logging.info(proxy)
    if oproxy[2].lower() == 'http':
        try:
            r = requests.get(TESTURLS['http'],proxies=proxy,timeout=10)
            #logging.info(r.status_code)
            if r.status_code == 200:
                logging.info('可用代理%s'%proxy['http'])
                return True
            else:
                return False
        except:
            logging.info('无效代理%s'%proxy['http'])
            return False
    if oproxy[2].lower() == 'https':
        try:
            r = requests.get(TESTURLS['http'],proxies=proxy,timeout=10,verify=False)
            #logging.info(r.status_code)
            if r.status_code == 200:
                logging.info('可用代理%s'%proxy['https'])
                return True
            else:
                return False
        except:
            logging.info('无效代理%s'%proxy['https'])
            return False
        

            
