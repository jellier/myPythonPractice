# 使用爬虫爬取网站图片并下载到本地

from bs4 import BeautifulSoup
import requests
import re
import os
import shutil

# 定义requests请求的地址和头信息
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = 'https://www.yixieshi.com/zcgl'

# 下载图片


def download_jpg(img_url, img_localPath):
    # Requests 库封装复杂的接口，提供更人性化的 HTTP 客户端，但不直接提供下载文件的函数。
    # 需要通过为请求设置特殊参数 stream 来实现。当 stream 设为 True 时，
    # 上述请求只下载HTTP响应头，并保持连接处于打开状态，
    # 直到访问 Response.content 属性时才开始下载响应主体内容
    response = requests.get(img_url, stream = True)
    if response.status_code == 200:
        # 'wb' writebinary
        with open(img_localPath , 'wb') as f:
            #
            response.raw.deconde_Rcontent = True
            # requests库没有写入功能，需要shutil库配合使用，把response返回的内容写入到文件中
            shutil.copyfileobj(response.raw, f)


# 获取图片
def crawImg(url):
    img_response = requests.get(url, headers = headers)
    img_soup = BeautifulSoup(img_response.text, 'lxml')
    # print(img_soup)

    for img in img_soup.find_all('img', class_='wp-post-image'):
        # img 为整个图片标签，需要使用get('src')获取地址
        imgurl = img.get('src')
        # 得到如下格式的图片地址：https://img.yixieshi.com/******.jpg?imageslim****/q/70，需要去掉?后面的部分
        imgurl = re.split("\?imageslim", imgurl)[0]
        # print(imgurl)
        dir = os.path.abspath('.')
        filename = os.path.basename(imgurl)
        imgpath = os.path.join(dir, filename)
        print('开始下载 %s' % imgurl)
        download_jpg(imgurl, imgpath)



crawImg(url)