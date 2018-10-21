import requests
from  pyquery import PyQuery as pq

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

def get_page(url):
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return  response.text
    except requests.ConnectionError as e:
        print(e.args)

def get_page_list(html):
    doc=pq(html)
    items=doc('#zh-recommend-list .feed-item').items()
    for item in  items:
        all={}
        all['bu']=item.children()
        # qustion=item.find('h2').text()
        # author=item.find('.author-link-line').text()
        # text=item.find('.post-content').text()

        print(all)




url='https://www.zhihu.com/explore'
html=get_page(url)
get_page_list(html)
