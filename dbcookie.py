#-*-coding:utf-8-*-
import urllib.request,urllib.parse
import http.cookiejar
#创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。

file='dbcookie.txt'
cookie=http.cookiejar.MozillaCookieJar(file)#声明对象来保存cookie
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
data=urllib.parse.urlencode({'form_email':'18813295794',
      'form_password':'18898604973'
      }).encode(encoding='UTF8')#要加上utf-8这个，不然报错
url='https://movie.douban.com/'
response=opener.open(url,data)#登录豆瓣电影
cookie.save(ignore_discard=True,ignore_expires=True)#保存
print(cookie)
result=opener.open('https://www.douban.com/')#再登录豆瓣首页
print(result)



'''import urllib.request,urllib.parse
import http.cookiejar

cookie=http.cookiejar.MozillaCookieJar()#声明对象来保存cookie
cookie.load('dbcookie.txt', ignore_discard=True, ignore_expires=True)
req = urllib.request.Request("https://movie.douban.com/")
#利用urllib2的build_opener方法创建一个opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
response = opener.open(req)
print (response.read())'''