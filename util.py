import re
import logging

from settings import RULES

class Util():

    @staticmethod
    def search(string):
        proxy = []
        for k,v in RULES.items():
            proxy.append(v.search(string).group())
        return tuple(proxy)

    def check_proxy(proxy):
        pass
            
