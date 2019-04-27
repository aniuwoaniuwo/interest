#-*-coding:utf-8-*-
#flask练手程序,主页面，登录页面和登录后的页面
#不能pycharm直接运行，需要在命令行下运行

from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>welcome to flask</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password"></p>
    <p><button type="submit">登录</button></p>
    </form>
    
    '''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='aniuwo' and request.form['password']=='aniuwoflask':
        return '''
        <h1>signin successfully</h1>
        <h1>happy everyday</h1>'''
    return 'bad username or password'

if __name__=='__main__':
    app.run()
