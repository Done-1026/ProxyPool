import random
import logging

from bs4 import BeautifulSoup
import requests

from settings import MY_USER_AGENTS

logging.basicConfig(level=logging.INFO)

url = 'http://www.xicidaili.com/nn/'
url1 = 'https://www.kuaidaili.com/free/inha/1'
headers = {}
headers['user-agent'] = random.choice(MY_USER_AGENTS)

resp = requests.get(url1,headers=headers)
resp.encoding = 'utf-8'
logging.info(resp)
soup = BeautifulSoup(resp.content,'html.parser')
ips = soup.find_all('tr')[1:]
for i in ips:
    print(i.text)
