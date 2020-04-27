from werkzeug.security import generate_password_hash, check_password_hash

def encrypt(passwd):#加密
    return generate_password_hash(passwd)

def checkPwd(pwd, hashedPwd):#检查密码
    return check_password_hash(hashedPwd, pwd)