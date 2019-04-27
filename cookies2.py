#-*-coding:utf-8-*-
import requests
import re
headers={'Cookie': '_zap=e98daa8e-016d-4e7a-b4e5-23a8172a0927; _xsrf=uMpKLcGarIf43BBiVdzSEmBy4oSAbsHO; d_c0="APBk3S8QLw6PTnKNxRCinLn-yfUtwZdFAxs=|1536456528"; capsion_ticket="2|1:0|10:1536457047|14:capsion_ticket|44:ZGE1ZDUyZjQyNTlmNGMzY2IxMTgzNjEwNTcxNmJjMjM=|252df2ab11d36a38c7367544100ae7c205e5be956314b77404f9ad9ce6f9fd7a"; z_c0="2|1:0|10:1536457059|4:z_c0|92:Mi4xNVpvd0JnQUFBQUFBOEdUZEx4QXZEaVlBQUFCZ0FsVk5ZOGVCWEFDM2t6QVppSWFOSmpTTWU0bXhHZEVOaWhkeUhR|091482d1e36cb2cd8c0f7577a94c5b0893d46814632565e2634f3d5951b74f65"; tgw_l7_route=ec452307db92a7f0fdb158e41da8e5d8; q_c1=91c90637546a48d79bdd52d1d91dcf55|1536457077000|1536457077000',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
url='https://www.zhihu.com/people/yu-kun-73/answers'
r=requests.get(url,headers=headers).text
pattern=re.compile('登录',re.S)
