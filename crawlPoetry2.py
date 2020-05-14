# 获取古诗词网唐代作者信息
# 使用BeautifulSoup匹配页面元素
import requests
import codecs
import json
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'https://so.gushiwen.org/authors/Default.aspx?p=1&c=%E5%94%90%E4%BB%A3'

# step1. 获取页面html
def download_page(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Referer": "http://www.infoq.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    }
    data = requests.get(url, headers=headers).content
    return data

# step2. 获取下一页的链接nextPage 和 每一条信息中所有的链接生成数组，并返回
# 这里主要是BeautifulSoup的用法
def parseHtml(html):
    # print(1)
    soup = BeautifulSoup(html, features="html.parser")

    nextUrl = soup.find('a', attrs={'class': 'amore'}).get('href')
    if nextUrl :
        nextPage = 'https://so.gushiwen.org' + nextUrl
    else:
        nextPage = ''

    leftDiv = soup.find('div', attrs={'class': 'main3'}).find('div', attrs={'class': 'left'})
    data = []
    for item in leftDiv.find_all('div', attrs={'class': 'sonspic'}):
        # data.append('https://so.gushiwen.org' + item.find('a')['href'])
        data.append(item.find('a')['href'])
    return data, nextPage
#
def buildJson(keys, values):
    # 映射函数的方式创建字典
    # 如：dict(zip(['one', 'two', 'three'], [1, 2, 3]))  返回{'three': 3, 'two': 2, 'one': 1}
    dictionary = dict(zip(keys, values))

    # json.dumps 用于将 Python 对象编码成 JSON 字符串。
    # 将中文写入txt文件时，可能会造成乱码，需要在转json时就关闭ascii编码格式，并且写入时encoding='utf-8'
    return json.dumps(dictionary, ensure_ascii=False)

def parseAuthorHtml(html):
    soup = BeautifulSoup(html, features="html.parser")
    all = soup.find('div', attrs={'class': 'main3'}).find('div', attrs={'class': 'left'})
    author = all.find('div', attrs={'class': 'sonspic'}).find('div', attrs={'class': 'cont'}).find('b').getText()
    desc = all.find('div', attrs={'class': 'sonspic'}).find('div', attrs={'class': 'cont'}).find('p').getText()
    sons = all.find('div',attrs={'class': 'sons'})
    # print('author')
    yishiUrl = None
    if sons:
        yishiUrl = sons.get('id')
        if yishiUrl:
            yishiUrl = 'https://so.gushiwen.org/authors/ajaxziliao.aspx?id=' + all.find('div',attrs={'class': 'sons'})['id'].replace('fanyi','')
        else:
            yishiUrl = None
    print('author:%s desc:%s yisiurl:%s' % (author, desc, yishiUrl))
    return author, desc, yishiUrl

def parseAuthorMore(html):
    soup = BeautifulSoup(html, features='html.parser')
    yishi = []
    if soup.find('div', attrs={'clase', 'contyishang'}):
        for p in soup.find('div', attrs={'clase', 'contyishang'}).find_all('p'):
            yishi.append(p.getText())
    return ''.join(yishi)

def main():
    url = DOWNLOAD_URL
    keys = ['author', 'desc', 'story']
    # with codecs.open('author.json', 'w', encoding='utf-8') as fp:
    #     fp.write('[')
    # 将json写入.txt文件,写入时使用utf编码
    file1 = open('crawlPoetry2.txt', 'w', encoding='utf-8')
    while url:
        html = download_page(url)
        data, url = parseHtml(html)

        for item in data:
            authorHtml = download_page(item)
            author, desc, yishiUrl = parseAuthorHtml(authorHtml)
            if yishiUrl:
                yishiHtml = download_page(yishiUrl)
                yishi = parseAuthorMore(yishiHtml)
            else:
                yishi = ""

            file1.write(buildJson(keys, [author, desc, yishi]))
            file1.write(',')
            file1.write('\n\n\n')
        #         fp.write(buildJson(keys, [author, desc,yishi]))
        #         fp.write(',')
        # fp.write(']')
    file1.close()

if __name__ == '__main__':
    main()