# import json
# import requests
# from requests.exceptions import RequestException
# import re
# import time
#
# def get_one_page(url):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
#         }
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return response.text
#         return None
#     except RequestException:
#         return Non
#
# def parse_one_page(html):
#     # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
#     #                      + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
#     #                      + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
#     pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
#     items = re.findall(pattern, html)
#     for item in items:
#         yield {
#             'index': item[0],
#             'image': item[1],
#             'title': item[2],
#             'actor': item[3].strip()[3:],
#             'time': item[4].strip()[5:],
#
#         }
#
# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')
#
# def main(offset):
#     url = 'http://maoyan.com/board/4?offset=' + str(offset)
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         print(item)
#         write_to_file(item)
#
# if __name__ == '__main__':
#     for i in range(10):
#         main(offset=i * 10)
#         time.sleep(1)
# from lxml import  etree
# text='''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html=etree.HTML(text)
# result=etree.tostring(html)
# print(result.decode('utf-8'))
# from lxml import  etree
# html=etree.parse('test.html',etree.HTMLParser())
# result=html.xpath('//*')
# print(result)
# from  bs4 import  BeautifulSoup
# soup=BeautifulSoup('<p>Hello</p>','lxml')
# print(soup.p.string)
# print(soup.prettify())
# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))
#
# from pyquery import  PyQuery as pq
# doc=pq(filename='test.html')
# print(doc('li'))
# from lxml import  etree
# html = etree.parse('test.html', etree.HTMLParser())
# result=etree.tostring(html)
# print(result.decode('utf-8'))
#
#
#
# def xpa(str):
#     result=html.xpath(str)
#     print(result)
#     return result
#
# if __name__ == '__main__':
#     xpa('//*')
#     xpa('//li')
#     xpa('//li/@class')
#     xpa('//li[@class="item-0"]')
#     xpa('//li[@class="item-0"]/text()')
#     xpa('//li[@class="item-0"]/a/text()')
#     xpa('//ul')
#     xpa('//li/a')
#     xpa('//a[@href="link4.html"]')
#     xpa('//a/@href')
import requests
from pyquery import  PyQuery as pq
# url='http://www.zhihu.com/explore'
# headers={
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# html=requests.get(url,headers=headers).text
# doc=pq(html)
# items=doc('.explore-tab .feed-item').items()
# for item in items:
#     question=item.find('h2').text()
#     author=item.find('.author-link-line').text()
#     answer=item.find('.content').text()
#     file=open('explore.txt','a',encoding='utf-8')
#     file.write('\n'.join([question,author,answer]))
#     file.write('\n'+'='*50+'\n')
#     file.close()
# import csv
# #CSV文件的读写,想和pandas库一起凑一篇文章
# with open('data.csv','a+') as csvfile:
#     fieldnames=['id','name','age']
#     writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id':10001,'name':'xiaoli','age':20})
#     writer.writerows([{'id':10002,'name':'xiaowang','age':21},{'id':10003,'name':'xiaozhang','age':21}])
#
# with open('data.csv','r',encoding='utf-8') as  csva:
#     read=csv.reader(csva)
#     print(read)
#     for row in read:
#         print(row)
import pymongo
client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
student={
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
result=collection.insert_one(student)
print(result)

student1={
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2={
    'id':'20170202',
    'name':'Mike',
    'age':21,
    'gender':'male'
}
result=collection.insert_many([student1,student2])
print(result)
#print(result.inserted_ids)
#查询
result=collection.find_one({'name':'Mike'})
print(type(result))
print(result)
results=collection.find({'age':20})
print(results)
for result in results:
    print(result)
result=collection.find({'age':{'$gt':20}})
print(result)
#计数
count=collection.find().count()
print(count)
count=collection.find({'age':20}).count()
print(count)
#排序
results=collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results ])
#偏移
results=collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in results ])
#更新
condition={'name':'Mike'}
student=collection.find_one(condition)
student['age']=26
result=collection.update(condition,student)
print(result)
#影响的条数
#print(result.matched_count,result.modified_count)
condition={'age':{'$gt':25}}
result=collection.update_one(condition,{'$inc':{'age':10}})
print(result)
#print(result.matched_count,result.modified_count)
#删除
result=collection.delete_one({'name':'Jordan'})
print(result)
#print(result.delete_count)


