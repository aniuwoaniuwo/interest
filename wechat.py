#-*-coding:utf-8-*-
import time
import re
import requests
import os
import itchat
def creat_joke():
    start=time.time()
    print("开始爬取joke")
    for j in range(1,51):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
        url = 'http://www.qiushibaike.com/hot/page/{}/'.format(str(j))  # format放在引号外面
        response = requests.get(url, headers=headers).text
        print(url)
        pattern = re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>', re.S)
        items = re.findall(pattern, response)


        for i in range(0, len(items)):
            a = items[i].replace('<br/>', '')
            with open("qiushi.txt","a",encoding='utf-8') as f:#a是追加,要加上第三个参数，否则读取不了
                f.write(a + "\n")
        #time.sleep(3)
    print("joke爬取完成")
    print((time.time()-start))
def send_news():
    file=open("qiushi.txt","r",encoding = 'utf-8')
    new=file.readlines()
    for a in new:
        if a!='\n':
            print(a)
            itchat.auto_login(hotReload=True)#热启动，不需要多次扫描
            my_friends=itchat.search_friends(name=u'黄睿')#备注就可以了
            my_friend=my_friends[0]["UserName"]#发送的对象
            print(my_friend)
            message='''
            亲爱的{}：
            我现在给你讲一个笑话：
            {}
            '''.format("狗蛋",a)
            itchat.send(message,toUserName=my_friend)
            print('发送完毕')
            return#强制退出，不然一直循环
def main():
    if not os.path.exists('qiushi.txt'):
        print("文件不存在")
        creat_joke()
    send_news()
'''if __name__=='__main__':
    while True:
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        love_time = curr_time.split(" ")[1]
        if love_time == "21:06:20":#一直挂着就是每天这个点发送，如果想每个小时都发送，可以考虑在条件那里用到‘或’条件，不过不美观，建议提取时与分出来，直接切除前面几个字符love_time[3:8]就可以了
            main()
            time.sleep(60)
        else:
            print("再等等吧" + love_time)'''

creat_joke()
#send_news()