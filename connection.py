# from redis import StrictRedis,ConnectionPool
# pool=ConnectionPool(host='localhost',port=6379,db=0,password='1234')
# redis=StrictRedis(host='localhost',port=6379,db=1,password='1234')
# redis1=StrictRedis(connection_pool=pool)
# redis.set('name','LX')
# #print(redis.get('name'))
# redis1.set('name','Ada')
# #print(redis1.get('name'))
# # print(redis.exists('LX'))
# # print(redis.exists('Ada'))
# # print(redis.type('LX'))
# print(redis.keys(b'^A.*'))
# print(redis.randomkey())
# redis.rename('name','nickname')
# print(redis.dbsize())
# redis.expire('name',2)
# redis.move('name',0)
# print(redis.get('name'))
# print(redis.get('nickname'))
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
import json
import urllib
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/1320135280',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
client = MongoClient()
db = client['weibo']
collection = db['weibo']
max_page = 14


#设置代理IP
# proxy_addr="122.241.72.191:808"
#
# #定义页面打开函数
# def use_proxy(url,proxy_addr):
#     req=urllib.request.Request(url)
#     req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
#     proxy=urllib.request.ProxyHandler({'http':proxy_addr})
#     opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
#     return data
#
# #获取微博主页的containerid，爬取微博内容时需要此id
# def get_containerid(url):
#     data=use_proxy(url,proxy_addr)
#     content=json.loads(data).get('data')
#     for data in content.get('tabsInfo').get('tabs'):
#         if(data.get('tab_type')=='weibo'):
#             containerid=data.get('containerid')
#     return containerid

def get_page(page):
    params = {
        'type': 'uid',
        'value':'1320135280',
        'containerid':'1076031320135280',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(jsonstr):
    if jsonstr:
        it = jsonstr.get('data')
        items=it['cards']
        for item in items:
            item_Z = item.get('mblog')
            weibo = {}
            weibo['id'] = item_Z.get('id')
            weibo['text'] = pq(item_Z.get('text')).text()
            weibo['attitudes'] = item_Z.get('attitudes_count')
            weibo['comments'] = item_Z.get('comments_count')
            weibo['reposts'] = item_Z.get('reposts_count')
            #print(weibo)
            yield weibo



def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')
def save_to_text(result):
    result=json.dumps(result)
    with open('mayun.txt','w+')as f:
        f.write(result)




if __name__ == '__main__':
    for page in range(1, max_page + 1):
        jsonstr = get_page(page)
        print(jsonstr)
        results = parse_page(jsonstr)
        try:
            for result in results:
                save_to_mongo(result)
        except Exception as e:
            break




