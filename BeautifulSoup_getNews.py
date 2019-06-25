# 使用爬虫爬取新闻网站
from bs4 import BeautifulSoup
import requests

# 伪装成合法浏览器
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'https://www.yixieshi.com/kjqy'


def crawNews(url):
    news_response = requests.get(url, headers=headers)
    news_soup = BeautifulSoup(news_response.text, 'lxml')
    # print(news_soup)

    for inx, title in enumerate(news_soup.find_all('div', class_='col-md-8')):
        # print([title.a.get('title')])
        print(inx + 1, title.a.text)


crawNews(url)
