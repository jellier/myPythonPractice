#获取当前页面的URL--current_url
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')

#打印网页标题
print(browser.current_url)
#输出内容：https://www.baidu.com/

items = browser.find_element_by_class_name('item-title')