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


# 爬取图片链接
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

