from app import app
from flask import request
from database import loginin
@app.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    return loginin(data)
    