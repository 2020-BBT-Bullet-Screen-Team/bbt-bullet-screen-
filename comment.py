from app import app
from flask import request
from database import commentin
from geventwebsocket.handler import WebSocketHandler         #提供WS（websocket）协议处理
from geventwebsocket.server import WSGIServer                #websocket服务承载
#WSGIServer导入的就是gevent.pywsgi中的类
# from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket              #websocket语法提示
@app.route('/comment',methods=['POST'])
def comment():
    data=request.get_json()
    rowcount=commentin(data)
    if(rowcount>0):
        return{"errcode":200,"errmsg":"评论成功"}
    else:
        return{"errcode":400,"errmsg":"评论失败"}
    