# 原文地址：https://zhuanlan.zhihu.com/p/61855418
# 获取古诗词网"推荐"诗词（共10页），包括诗词名、作者、朝代、诗词内容，并存储到文件中
# 使用正则表达式匹配页面元素
# 正则的关键是findall有分组

import requests
import re
import json


def parsePage(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Referer": "http://www.infoq.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    }
    # step1. 获取整个页面
    response = requests.get(url, headers)
    text = response.text

    # step2. 筛选页面信息
    # \s匹配任何空白字符，它相当于类[\t\n\r\f\v]
    # 使用.*?而不是.* ，避免贪婪模式
    # 使用.*?而不是.* ，避免贪婪模式
    # 元字符.可以匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
    '''
        以下几句都用到了findall有分组：只将匹配到的字符串里，组的部分放到列表里返回
    '''
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    '''
        .*? # 非贪婪匹配到<b>标签
        (.*?) # 非贪婪匹配从<b>到</b>标签的文字
    '''
    dynasties = re.findall(
        r'<p class="source">.*?<a.*?>(.*?)</a>',
        text,
        re.DOTALL)
    '''
        .*? # 非贪婪匹配到<a>标签
        <a.*?> # 非贪婪匹配到>标签
        (.*?)</a> # 非贪婪匹配>到</a>标签中的文字
    '''
    authors = re.findall(
        r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',
        text,
        re.DOTALL)
    '''
        .*? # P标签下面有两个a标签，一个a标签是年代，一个是名字
        <a.*?> # 第一个a标签内容
        .*? # 第一个标签a后面的内容
        <a.*?> # 匹配到第二个a标签内容
    '''
    contents_tags = re.findall(
        r'<div class="contson" .*?>(.*?)</div>',
        text,
        re.DOTALL)

    contents = []
    for content in contents_tags:
        # 去掉<br/>及<p>
        # content = re.sub('<br\s/>|<p>|</p>', '', content) # 等同于此句
        content = re.sub(r'<.*?>', '', content)
        #  strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        # 只能删除开头或是结尾的字符，不能删除中间部分的字符
        contents.append(content.strip())

    # step3. 整理数据格式,用zip将4个key打包成json格式
    poems = []
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasties': dynasty,
            'authors': author,
            'contents': content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print('---'*80)
    return poems

def saveJson(_poems):
    # step4 将json格式数据写入文件
    # 不能使用write，write不支持json或者字典格式
    # 使用json库的dump方法
    with open('crawlPoetry.json', 'w', encoding='utf-8') as file_obj:
        json.dump(_poems, file_obj, ensure_ascii=False, indent=4)
    '''
        遇到问题一：中文不能正常显示
        解决方法：encoding='utf-8'和ensure_ascii=False 配合使用，才能正常输出中文

        遇到问题二：json文件中并不是按照title/dynasties/authors/contents排序的
        解决方法：去掉json.dump中的参数——sort_keys=True
    '''


def main():
    allPoem = []
    print('采集开始')
    for page in range(1, 11):
        url = 'https://www.gushiwen.org/default_{}.aspx'.format(page)
        '''
        不同的写法：
        url = 'https://www.gushiwen.org/default_%s.aspx'%page
        '''
        poems = parsePage(url)
        allPoem.append(poems)
    print('采集完成')
    saveJson(allPoem)
    print('存储完成')


if __name__ == '__main__':
    main()

'''
向json对象添加元素也可以使用以下方法：
old = '{"status_code": 200, "data": {"key1": "value", "key2": "value"}, "key9": "OK"}'

new = json.dumps({**json.loads(old), **{"new_key": "new_value"}})

如果是Python3.6之前的版本，需要在某个地方存储dict来更新
temp = json.loads(old)
temp.update({"new_key": "new_value"})
new = json.dumps(temp)
'''
