import urllib.request
import http.cookiejar
cookie=http.cookiejar.MozillaCookieJar('cookie.txt')
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
result=opener.open('https://www.douban.com/')#再登录豆瓣首页
print(result.read())

response=opener.open('https://movie.douban.com/')
print(cookie)
for item in cookie:
    print(item.name,item.value)
cookie.save(ignore_discard=True,ignore_expires=True)
import requests
response=requests.get('http://www.baidu.com')

print(response.cookies)