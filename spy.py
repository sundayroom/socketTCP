# url="http://www.baidu.com"
# # #response=urllib.request.urlopen(url)
# # req=urllib.request.Request(url)
# # response=urllib.request.urlopen(req)
# # print(response.read().decode('utf-8'))
# import socket
# # import urllib.request
# # import  urllib.parse
# #
# #
# #
# # url="http://httpbin.org/post"
# # data=urllib.parse.urlencode({'name':'ada'}).encode('utf-8')
# # headers = {
# #       'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
# #  }
# # try:
# #     response=urllib.request.Request(url=url,data=data,headers=headers,method='POST')
# #     req=urllib.request.urlopen(response,timeout=1)
# #     print(req.read().decode('utf-8'))
# # except urllib.error.URLError as e:
# #     if isinstance(e.reason,socket.timeout):
# #         print('Time Out')
# import socket
# import urllib.request
# import  urllib.parse
# url="http://tieba.baidu.com/"
# #data=urllib.parse.urlencode({'name':'ada'}).encode('utf-8')
# headers = {
#       'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36',
#  }
# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'web-proxy.oa.com:8080',
#     'https': 'web-proxy.oa.com:8080'
# })
# opener = urllib.request.build_opener(proxy_handler)
# urllib.request.install_opener(opener)
# try:
#     response=urllib.request.Request(url=url,headers=headers)
#     req=urllib.request.urlopen(response,timeout=1)
#     print(req.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('Time Out')
# from urllib.parse import urlparse
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result)
#
# from urllib.parse import urlunparse
#
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))
# from urllib.parse import urlsplit
#
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)
#
# from urllib.parse import urljoin
#
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))
#
# from urllib.parse import quote
#
# word = '请问'
# url = 'https://www.baidu.com/s?md=' + quote(word)
# print(url)
# import requests
# r=requests.get('http://www.baidu.com')
# print(r.status_code)
# print(type(r))
# print(type(r.text))
# print(r.text)
# #print(r.cookie)
#
# data={
#     'name':'zhangsan',
#     'age':23
# }
# r=requests.get('http://httpbin.org/get',params=data)
# print(r.text)
# print(r.json())
# print(type(r.json()))
#
# import re
#
# headers={
#     'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r=requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern=re.compile(r'explore-feed.*?question_link.?[*>(.?*)</a>]',re.S)
# titles=re.findall(pattern,r.text)
# print(titles)
import requests
r=requests.get('http://github.com/favicon.ico')
with open('image.ico','wb') as f:
    f.write(r.content)

files={'file':open('image.ico','rb')}
r=requests.post('http://httpbin.org/post',files=files)
print(r.text)

r=requests.get('http://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
    print(key+'='+value)

import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)