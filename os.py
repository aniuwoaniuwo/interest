#-*-coding:utf-8-*-
import os
file='C:\spider\lx'
file1='C:\\spider\\lx\\os\\'#双斜线是比单好点，单的话后面必须跟文件夹名，而双可以不跟
if os.path.exists(file1):#判断是否存在
    print('存在此文件夹')
else:
    print('不存在此文件夹')
    os.makedirs(file1)#创建文件夹
if os.path.exists(file1):
    print('存在此文件夹')
else:
    print('不存在此文件夹')
f=open(file1+'os'+'.txt','a')
print(os.getcwd())#获取当前文件路径
print(os.path.abspath('eason.py'))#获取绝对路径，包括文件名
print(os.path.abspath(''))
print(os.path.dirname('eason.py'))

