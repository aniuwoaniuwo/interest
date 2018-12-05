#-*-coding:utf-8-*-
'''打印出99乘法口则，首先知道乘法口则的具体形状，然后拆分，可以循环，换行，加空格表示，用到了join的函数'''
p='\n'.join(' '.join(['%s*%s=%s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10))
print(p)