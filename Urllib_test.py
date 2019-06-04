# urllib 是 python 标准库 ，提供了一系列用于操作URL的功能。
# https://docs.python.org/3/library/urllib.html
# 包括以下模块： urllib.request 、 urllib.error 、urllib.parse、 urllib.robotparser

# http://httpbin.org 进行http测试的网站

# request库需要用from导入，不能直接import urllib
from urllib import request #发起请求的
from urllib import parse  # 处理数据的
from urllib import error


# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1) #需要设置超时时间，避免一直等待，不写timeout也能正常执行，但超时会卡死
# # print(response.read()) #打印出来的是网页编码utf-8格式的
# print(response.read().decode('utf-8'))



# 请求网页方式：get 和 post
# get方式：请求网址时直接将参数写在?后面，比如 http://httpbin.org/get?a=123
# 传递的数据量小，4kb左右（不同浏览器会有差异）/安全性低，会将信息显示在地址栏/速度快，通常用于对安全性要求不高的请求。
# post方式：POST就是发送、提交。可以向指定的资源提交要被处理的数据。如果使用表单方式进行提交，表单的method必须设置为POST
# post提交数据相对于get的安全性高一些。（注意：抓包软件也会抓到post的内容，安全性要求高可以进行加密）
# 传递数据量大，请求对数据长度没有要求。
# 请求不会被缓存，也不会保留在浏览器的历史记录中。
# 用于密码等安全性要求高的场合，提交数据量较大的场合，如上传文件，发布文章等。
# POST方式提交数据上限默认为8M（可以在PHP的配置文件post_max_size选项中修改）

# post 的数据需要parse.urlencode封装
data = bytes(parse.urlencode({'word':'hello'}),encoding='utf8')

response1 = request.urlopen('http://httpbin.org/post', data= data)
print('post方式：' , response1.read().decode('utf-8'))

response2 = request.urlopen('http://httpbin.org/get', timeout=1)
print('get方式：' , response2.read().decode('utf-8'))


# response3 = request.urlopen('http://httpbin.org/get', timeout=0.01)
# print('get方式超时测试：' , response3.read().decode('utf-8'))
import socket
try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.01)
# 这里的 error 是 urllib.error
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')


# 使用urllib时头部信息
# 使用urllib伪装成浏览器去请求

url = 'http://httpbin.org/post'

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8",
"Connection": "close",
"Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
"Referer": "http://httpbin.org/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

dict = {
'name': 'value'
}

data4 = bytes(parse.urlencode(dict), encoding='utf8')
# 提交时重新定义头部信息，headers使用自定义的头部信息来伪装成浏览器
req = request.Request(url=url, data=data4, headers=headers, method='POST')
response4 = request.urlopen(req)
print( response4.read().decode('utf-8'))