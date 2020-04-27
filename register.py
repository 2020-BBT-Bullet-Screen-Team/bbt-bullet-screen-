from app import app
from flask import request
from database import subtimein,findUser
@app.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    if findUser(data['username']):
        return{'errcode':400,'errmsg':'您已经注册'},400
    if(subtimein(data)>0):
        return{"errcode":200,"errmag":"注册成功"}