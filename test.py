from queue import Queue
from threading import Thread
import logging

from util import check_proxy
from getproxy import getter
    
    
getter()
opool = getter.que
pool = Queue()

while not opool.empty():
    proxy = opool.get()
    if check_proxy(proxy):
        print(proxy)
