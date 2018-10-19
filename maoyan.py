import requests
from requests.exceptions import RequestException
import re
import time
import json

def load_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
def load_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index':item[0],
            'title':item[1],
            'actor':item[2],
            'release-time':item[3]
        }
def load_json(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps({'name':'ls'}))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


def main(offset):
    url='http://maoyan.com/board/4?offset='+str(offset)
    html=load_page(url)
    items=load_one_page(html)
    for item in items:
        print(item)
        load_json(item)

if __name__ == '__main__':
    for i in range(10):
       main(offset=i*10)
       time.sleep(1)
