# beautifulSoup库的使用，也是第三方库
# pip3 install bs4
# pip3 install lxml

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())

# 找到title标签
print('找到title标签:', soup.title)
# 找到title里面的内容
print('找到title里面的内容:', soup.title.string)
# 找到p标签
print('找到p标签:', soup.p)
# 找到第一个a标签
print('找到第一个a标签:', soup.a)
# 找到所有的a标签
print('找到所有的a标签:', soup.find_all('a'))

# 找到id为link3的的标签
print('找到id为link3的的标签:', soup.find(id="link3"))

# 使用 enumerate 函数 可以返回for in循环的下标
for inx, link in enumerate(soup.find_all('a')):
    print('得到 %s 个 a 标签的链接 %s : ' % (inx + 1, link.get('href')))
