from queue import Queue
from threading import Thread
import logging

from util import check_proxy
from getproxy import getter
from myThread import CheckThread


logging.basicConfig(level=logging.INFO)
tds = []
getter()
opool = getter.que
pool = Queue()

def check(proxy):    
    if check_proxy(proxy):
        #logging.info(proxy)
        pool.put(proxy)        
        
def refresh():
    while not opool.empty():
        proxy = opool.get()
        logging.info(proxy)
        t = CheckThread(check,proxy)
        tds.append(t)

    for td in tds:
        td.start()

    for td in tds:
        td.join()


if __name__ == '__main__':
    refresh()
    
        
