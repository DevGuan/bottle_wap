# coding=utf-8

from bottle import *

'''
	使用POST方法 验证登录指令
'''
@route('/login/<name>',method='GET')
def login(name):

    # postValue = bottle.request.POST.decode('utf-8')
    # userName = bottle.request.POST.get('username')
    # password = bottle.request.POST.get('password')
        
    return 'zhengchang  --- %s'% name

run(host='0.0.0.0',port=8888)