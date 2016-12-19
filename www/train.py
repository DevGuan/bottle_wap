# coding=utf-8

from bottle import *
import json
'''
    使用POST方法 验证登录指令
'''
@post('/login',method='POST')
def login():
    params = request.body.read()
    print 'data---' + str(params)
    try:
    	params = json.loads(params)
    except Exception as e:
    	params = {}

    # postValue = request.POST.decode(encoding ='utf-8')
    userName = params.get('username')
    password = params.get('password')
        
    canLogin = checkLogin('123456','123456')
    data = {"code":"0","username":userName,'password':password}
    jsondata = json.dumps(data)

    print jsondata
    
    if canLogin:
    	# return {'code':'success'} 
        return jsondata
    else:
        return {'code':'1'}

    # return {'code':'success'}    
    # return username + '密码' + password
    

def checkLogin(username,password):
    username = username
    password = password

    if username == '123456' and password == '123456':
        return True
    else:
        return False
    

@route('/regist',method='POST')
def regist():
    postValue = bottle.request.POST.decode('utf-8')
    userName = bottle.request.POST.get('username')
    password = bottle.request.POST.get('password')
    checkCode = bottle.request.POST.get('checkCode')
    '''
    检查数据库中是否已有账号  判断是否可以注册成功
    '''
    return {'code':'success'}

run(host='0.0.0.0',port=8888)