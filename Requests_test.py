# requests库的使用，也是第三方库，对urllib的封装
# pip3 install requests

import requests
# url = 'http://httpbin.org/get'
# data = {'key':'value', 'abc': 'def'}
# # .get是使用get方式请求url，字典类型的data不用进行额外处理
# response = requests.get(url, data)
# print(response.text)
#
#
# url_post = 'http://httpbin.org/post'
# response_post = requests.post(url_post, data)
# # 返回类型可以设为json格式
# print(response_post.json())


# 一个爬取图片链接的小例子
import re
# 随便搜一个结构简单的带图片页面
content = requests.get('http://m.sohu.com/a/258728604_652515').text
# print(content)

# 原例子：
# < div class ="grid-item work-thumbnail" >
# < a href="(.*?)".*?title">(.*?)</div>
# < div class ="author" > LynnWei < / div >

# 我找的页面的图片结构
# <p><img class="content-image" data-src="//5b0988e595225.cdn.sohucs.com/q_70,c_zoom,w_640/images/20181011/01f73103f5fc45dc8c686061dd9307d9.jpeg"></p>
# <p>让我们以新时代少年的名义起誓，从小学习做人，从小学习立志，从小学习创造！让我们面向五星红旗，向伟大的祖国母亲致敬 ！</p>
# 改成以下：
# <p><img .*? data-src="(.*?)">.*?(.*?)</p>

# re.S叫做单行模式，简单来说，就是你用正则要匹配的内容在多行里，会增加你要匹配的难度，这时候使用re.S把每行最后的换行符\n当做正常的一个字符串来进行匹配的一种小技巧
pattern = re.compile(r'<p><img .*? data-src="(.*?)">.*?(.*?)</p>', re.S)
results = re.findall(pattern, content)
print(results)

# 把结果格式化
for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))

# 关于爬虫
# 一、爬虫基本流程
# 1、发起请求：通过HTTP库向目标站点发起请求，即发送一个Request，请求可以包含额外的headers等信息，等待服务器响应。
# 2、获取响应内容：如果服务器能正常响应，会得到一个Response，Response的内容便是所要获取的页面内容，类型可能有HTML，Json字符串，二进制数据（如图片视频）等类型。
# 3、解析内容：得到的内容可能是HTML，可以用正则表达式、网页解析库进行解析。可能是Json，可以直接转为Json对象解析，可能是二进制数据，可以做保存或者进一步的处理。
# 4、保存数据：保存形式多样，可以存为文本，也可以保存至数据库，或者保存特定格式的文件。

# 二、Request和Response
# Request：浏览器就发送消息给该网址所在的服务器，这个过程叫做HTTP Request。
# Response:服务器收到浏览器发送的消息后，能够根据浏览器发送消息的内容，做相应处理，然后把消息回传给浏览器。这个过程叫做HTTP Response。浏览器收到服务器的Response信息后，会对信息进行相应处理，然后展示。

# 三、Request详解
# 请求方式：主要有GET、POST两种类型，另外还有HEAD、PUT、DELETE、OPTIONS等。
# 请求URL：URL全称统一资源定位符，如一个网页文档、一张图片、一个视频等都可以用URL唯一来确定。
# 请求头：包含请求时的头部信息，如User-Agent、Host、Cookies等信息。
# 请求体：请求时额外携带的数据如表单提交时的表单数据

# 四、Response详解
# 响应状态：有多种响应状态，如200代表成功、301跳转、404找不到页面、502服务器错误
# 响应头：如内容类型、内容长度、服务器信息、设置Cookie等等。
# 响应体：最主要的部分，包含了请求资源的内容，如网页HTML、图片二进制数据等。

# 五、能抓取哪些数据
# 网页文本:如HTML文档、Json格式文本等。
# 图片:获取到的是二进制文件，保存为图片格式。
# 视频:同为二进制文件，保存为视频格式即可。
# And so on:只要是能请求到的，都能获取。

# 六、解析方式
# 直接处理
# Json解析
# 正则表达式
# BeautifulSoup
# PyQuery
# XPath

# 参考文档：
# https://blog.csdn.net/Byweiker/article/details/79234854



