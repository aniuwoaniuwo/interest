#-*-coding:utf-8-*-



#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import random


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append( ip)
        
    proxy_ip = random.choice(proxy_list)
    print(proxy_ip)
    proxies = {'http': proxy_ip}
    print(proxies)
    return proxies

if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    ip_list = ['http://106.75.226.36:808','http://118.190.95.35:9001',
'http://101.132.98.70:808','http://61.135.217.7:80']

    proxies = get_random_ip(ip_list)
    print(proxies)
    url='http://www.baidu.com/'
    proxies1={'http': 'http://59.110.240.249:8080'}

    res=requests.get(url,proxies=proxies)
    print(res.text)
