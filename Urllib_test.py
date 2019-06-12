# urllib 是 python 标准库 ，提供了一系列用于操作URL的功能。
# https://docs.python.org/3/library/urllib.html
# 包括以下模块： urllib.request 、 urllib.error 、urllib.parse、 urllib.robotparser

# http://httpbin.org 进行http测试的网站 收藏

# request库需要用from导入，不能直接import urllib
from urllib import request #发起请求的
from urllib import parse  # 处理数据的
from urllib import error

# ======================urlopen的基本用法=================================
# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1) #需要设置超时时间，避免一直等待，不写timeout也能正常执行，但超时会卡死
# # print(response.read()) #打印出来的是网页编码utf-8格式的
# print(response.read().decode('utf-8'))

response = request.urlopen('http://www.baidu.com')
print("查看 response 的返回类型：",type(response))
print("查看反应地址信息: ",response)
print("查看头部信息1(http header)：\n",response.info())
print("查看头部信息2(http header)：\n",response.getheaders())
print("输出头部属性信息：",response.getheader("Server"))
print("查看响应状态信息1(http status)：\n",response.status)
print("查看响应状态信息2(http status)：\n",response.getcode())
print("查看响应 url 地址：\n",response.geturl())

# 返回结果太长，暂时注释掉
# page = response.read()
# print("输出网页源码:",page.decode('utf-8'))

# ============================get 和 post的差别及在urllib中的用法========================================
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


# imeout参数可以设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间还没有得到响应，就会抛出异常，如果不指定，就会使用全局默认时间。
# 它支持 HTTP 、 HTTPS 、 FTP 请求。
# 我们试着给timeout一个更小的值,例如timeout=0.1,此时抛出 urllib.error.URLError 异常，错误原因为 time out 。
# 因为常理下 0.1 s 内根本就不可能得到服务器响应。所以通过设置参数 timeout 的值对于应对网页响应的速度具有一定的意义。
# 同时，可以通过设置这个超长时间来控制一个网页如果长时间未响应就跳过它的抓取（可以通过try-catch 语句）。

import socket
try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.01)
# 这里的 error 是 urllib.error
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('Time out')

# 在 urlopen 参数 data 不为 None 时，urlopen() 数据提交方式 为 Post。
# urllib.parse.urlencode()方法将参数字典转化为字符串。
# 提交的网址是httpbin.org，它可以提供HTTP请求测试。
# https://httpbin.org/post 这个地址可以用来测试 POST 请求，它可以输出请求和响应信息，其中就包含我们传递的 data 参数。




# 使用urllib时头部信息
# =========================使用urllib伪装成浏览器去请求================================

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
# 如果要传bytes（字节流）类型的，如果是一个字典，先用urllib.parse.urlencode()编码。
data4 = bytes(parse.urlencode(dict), encoding='utf8')
# 提交时重新定义头部信息，headers使用自定义的头部信息来伪装成浏览器
req = request.Request(url=url, data=data4, headers=headers, method='POST')
response4 = request.urlopen(req)
# print( response4.read().decode('utf-8'))


# 请求方式的含义：
# get 和 post比较常见 GET请求将提交的数据放置在HTTP请求协议头中
# POST提交的数据则放在实体数据中
# GET： 请求指定的页面信息，并返回实体主体。
# HEAD： 只请求页面的首部。
# POST： 请求服务器接受所指定的文档作为对所标识的URI的新的从属实体。
# PUT： 从客户端向服务器传送的数据取代指定的文档的内容。
# DELETE： 请求服务器删除指定的页面。



response5 = request.urlopen('http://www.163.com')
print(response5.status)
print(response5.getheaders())
print(response5.getheader('Server'))
# print(response5.read().decode('gbk'))


#================================parse=================================================
# parse_qs这个函数主要用于分析URL中query组件的参数，返回一个key-value对应的字典格式
print(parse.parse_qs("FuncNo=9009001&username=1"))
# 返回值：{'FuncNo': ['9009001'], 'username': ['1']}

# 这个函数和urllib.parse.parse_qs（）作用一样，唯一的区别就是这个函数返回值是list形式
print(parse.parse_qsl("FuncNo=9009001&username=1"))
# 返回值： [('FuncNo', '9009001'), ('username', '1')]


# print(parse.parse_qsl("FuncNo=9009001&username=1"))  

parsed=parse.urlparse("https://www.zhihu.com/question/50056807/answer/223566912")

print(parsed)
# 返回值：ParseResult(scheme='https', netloc='www.zhihu.com', path='/question/50056807/answer/223566912', params='', query='', fragment='')

# print(parse.parse_qs("https://www.zhihu.com/question/50056807/answer/223566912"))  
# print(parse.parse_qs("FuncNo=9009001&username=1"))  

t = parsed[:]
print(parse.urlunparse(t))
#返回值：https://www.zhihu.com/question/50056807/answer/223566912

# urllib.parse.urlsplit(urlstring, scheme=”, allow_fragments=True)
# 这个函数和urlparse()功能类似，唯一的区别是这个函数不会将url中的param分离出来；就是说相比urlparse()少一个param元素，
# 返回的元组元素参照urlparse()的元组表，少了一个param元素；

print(parse.urlsplit("https://www.zhihu.com/question/50056807/answer/223566912"))


# urllib.parse.urlunsplit(parts)
# 与urlunparse()相似，切与urlsplit()相对应；

parsed=parse.urlsplit("https://www.zhihu.com/question/50056807/answer/223566912")
t=parsed[:]
print(parse.urlunsplit(t))

# urllib.parse.urljoin(base, url, allow_fragments=True)
# 这个函数用于讲一个基本的URL和其他的URL组装成成一个完成的URL；
print(parse.urljoin("https://www.baidu.com/Python.html","Java.html"))