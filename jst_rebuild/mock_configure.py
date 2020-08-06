import json
import urllib.parse
from wsgiref.simple_server import make_server


# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。

def application(environ, start_response):


        # 定义文件请求的类型和当前请求成功的code

        start_response('200 OK', [('Content-Type', 'text/html')])

        # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get

        # 获取当前get请求的所有数据，返回是string类型

        params = urllib.parse.parse_qs(environ['QUERY_STRING'])

        # 获取get中key为name的值

        name = params.get('name', [''])[0]

        no = params.get('no', [''])[0]

        # 组成一个数组，数组中只有一个字典

        dic = {"success":"true","msg":"daf","data":{"status":"1"}}

        return [json.dumps(dic).encode('utf-8')]

if __name__ == "__main__":

        port = 5088

        httpd = make_server("172.21.222.74", port, application)

       # print("serving http on port {port1}...").format(po)

        httpd.serve_forever()
