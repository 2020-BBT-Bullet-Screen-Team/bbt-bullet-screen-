from flask import Flask 
from flask_cors import CORS
import mysql.connector
import config
from geventwebsocket.handler import WebSocketHandler         #提供WS（websocket）协议处理
from geventwebsocket.server import WSGIServer                #websocket服务承载
#WSGIServer导入的就是gevent.pywsgi中的类
# from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket              #websocket语法提示
app=Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY']=config.app['secret_key']
from login import *
from register import *
from comment import *
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000)
    http_server=WGSIServer(('127.0.0.1',5000),application=app,handler_class=WebSocketHandler)
    http_server.serve_forever()