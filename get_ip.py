#-*-coding:utf-8-*-
'''爬取了西刺前面5页的ip，然后逐个试了选出有用的ip'''
from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip):
    proxy_list = []
    proxy_list.append('http://' + ip)

    proxy_ip = random.choice(proxy_list)

    proxies = {'http': proxy_ip}

    return proxies

if __name__ == '__main__':
    for i in range(1,6):
        url = 'http://www.xicidaili.com/nn/{}'.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        ip_list = get_ip_list(url, headers=headers)
        url = 'http://www.baidu.com/'
        for ip in ip_list:
            proxies = get_random_ip(ip)
            res = requests.get(url, proxies=proxies)
            if res.status_code==200:
                print(ip)
    print('done')






