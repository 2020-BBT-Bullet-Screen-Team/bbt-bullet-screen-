from config import db
from flask import session
import mysql.connector
from utils import encrypt,checkPwd
from flask import request
conn=mysql.connector.connect(host=db['host'],user=db['user'],passwd=db['password'],database=db['database'],charset='utf8mb4')
db=conn.cursor()
def findUser(username):
    try:
        db.execute('select * from users where `username`=%s',(username,))
    except Exception as e:
        abort(408,message=str(e))
    result=db.fetchall()
    return result
    
def subtimein(data):
    username=data['username']
    password=encrypt(data['password'])
    db.execute('insert into users (`username`,`password`)values(%s,%s)',(username,password))
    try:
        conn.commit()
    except Exception as e:
        abort(408,message=str(e))
    return db.rowcount
    
def loginin(data):
    username=data['username']
    password=encrypt(data['password'])
    db.execute('select * from users where `username`=%s',(username,))
    result=db.fetchone()
    if (result)and checkPwd(password,result[2]):
        session['user_id']=result[0]
        return{"errcode":200,"errmsg":"登录成功"}
    else:
        return{"errcode":400,"errmsg":"登录失败"}
def commentin(data):
    username=data['username']
    comment=data['comment']
    time=data['time']
    import ahocorasick
    A=ahocorasick.Automaton()
    file=open('C:/Users/Williams/screen/text.txt','r',encoding="utf-8")
    a=file.read()
    text=a.split( )
    
    #test = ['abcdefg', 'abcdef', 'abcde','abcd','abc','ab','a','abdcef','兼职']
    
    for line in text:
        bkw=str(line.strip())
        A.add_word(bkw,(1,bkw))
    A.make_automaton()
    ecomment=comment
    for k,(i,t) in A.iter(comment):
        ecomment=comment.replace(t,"*"*len(t))
    db.execute('insert into comments (`username`,`comment`,`time`)values(%s,%s,%s)',(username,ecomment,time))
    try:
        conn.commit()
    except Exception as e:
        abort(408,message=str(e))
    broadcast(comment)
    return db.rowcount

def broadcast(message):
    if request.environ.get('wsgi.websocket'):
        ws=request.environ['wsgi.websocket']#获取websocket连接
        if ws is None:
            abort(404)
        else:
            for client in ws.handler.active_client.values():
                client.ws.send(message)
    
    