# 获取1688热销商品
import requests
import json


def getUrls():
    '''
        step1.获取前5页商品的所有地址
        search_url:搜索结果接口
        key_word：搜索关键字，比如"地摊玩具"
        begin_page：当前页，页面底部的分页，高亮的是当前页
        start_index：一页共展示60个商品，页面加载时同步加载前20个，后面40个为接口分2次异步返回，每次20个
        return: 地址列表
    '''
    url_list = []
    search_url = "https://search.1688.com/service/marketOfferResultViewService?"
    key_word = "%B5%D8%CC%AF%CD%E6%BE%DF"  # 地摊玩具
    key_word = "%B5%D8%CC%AF%CD%E6%BE%DF+%B7%A2%B9%E2"  # 地摊玩具+发光
    begin_page = 1
    for i in range(5):
        start_index = 0

        for j in range(3):
            goods_url = search_url + "keywords=" + key_word + "&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0&async=true&asyncCount=20&beginPage=" + \
                str(begin_page) + "&pageSize=60&requestId=1217115422001591266530370000520&startIndex=" + str(start_index)
            url_list.append(goods_url)
            start_index += 20

        begin_page += 1
    return url_list


def downloadData(url):
    '''
        step2.获取商品接口地址数据
        :param url: 接口地址，一次返回20个商品
        :return: 接口返回数据是json,直接返回该json
    '''
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Referer": "http://www.infoq.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    }
    request_text = requests.get(url, headers=headers)
    # Requests中有个内置的json解码器，可以直接处理json数据，也就不需要json库了
    # print(request_text.json())

    # 注意：是loads不是load
    _json = json.loads(request_text.text)

    return _json


def parseData(data):
    '''
        step3.筛选有用信息
        :接口返回几百个字段，但只需要每个商品的复购率和它的详情页链接
        :return:将有用的两个字段打包成json返回
        返回格式：[{'repurchaseRate': '**.*%', 'detailUrl': '***'},{'repurchaseRate': '**.*%', 'detailUrl': '***'}...{}]
    '''
    offer_list = data["data"]["data"]["offerList"]
    rate_list = []
    detail_list = []
    for each_offer in offer_list:
        re_purchase_rate = each_offer["company"]["shopRepurchaseRate"]
        # shopRepurchaseRate返回的是如12.9%这样的字符串，为了后面的排序需要转成浮点型
        rate_list.append(float(re_purchase_rate.replace('%', '')))

        detail_list.append(each_offer["information"]["detailUrl"])

    new_offer_list = []
    for item in zip(rate_list, detail_list):
        _rate, _detail = item

        new_offer = {
            "repurchaseRate": _rate,
            "detailUrl": _detail
        }
        new_offer_list.append(new_offer)
    return new_offer_list

def sortRate(offerlist):
    '''
        step4.针对json中某个关键字段（回购率）进行排序
        :return:返回排序后的list
    '''
    _list = offerlist
    # sort的reverse参数默认是False升序，这里我们需要降序排序，设成True
    _list.sort(key=lambda x: x["repurchaseRate"], reverse=True)
    print(_list)


def main():
    # step1.获取前5页商品的所有地址
    urls = getUrls()

    parse_data_list =[]
    for inx, _url in enumerate(urls):
        # step2.获取商品接口地址数据
        json_data = downloadData(_url)

        # step3.筛选有用信息
        parse_data_list += parseData(json_data)

    # step4.针对json回购率进行排序
    sortRate(parse_data_list)


if __name__ == '__main__':
    main()
