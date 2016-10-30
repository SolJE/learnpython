#WSGI:Web Server Gateway Interface

def application(environ,start_response):
    start_response("200 OK" , [("Content-Type","text/html")])
    return [b'<h1>Hello,web!</h1>']

def application_2(environ,start_response):
    start_response("200 OK" , [("Content-Type","text/html")])
    body = "<h1>Hello,%s!" % (environ["PATH_INFO"][1:] or "web")
    return [body.encode("utf-8")]


#Server.py
#从wsgi模块导入：
from wsgiref.simple_server import make_server

#创建一个服务，IP地址为空，端口是8000，处理函数是application:
httpd = make_server("",8000,application_2)
print("Servering HTTP on port 8000...")
#开始监听HTTP请求：
httpd.serve_forever()
