import requests
from  urllib.parse import  urlencode
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}
def get_page(offset):
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'cout':'20',
        'cur_tab':'1',
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError:
        return None
def get_images(json):
    jiepai={}
    image_list=[]
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title')!=None and item.get('image_list')!=None:
                jiepai['title']=item.get('title')
                #item.get('image_list')
                for item in item.get('image_list'):
                    image_list.append(item)
                jiepai['image_list']=image_list
                # print(jiepai)
        return jiepai

import os
from hashlib import md5

def save_image(jiepai):
    if not os.path.exists(jiepai.get('title')):
        os.mkdir(jiepai.get('title'))
    try:
        for url in jiepai['image_list']:
            print(url.get('url'))
            response = requests.get('http:'+url.get('url'),headers=headers)
            if response.status_code==200:
                file_path = '{0}/{1}.{2}'.format(jiepai.get('title'), md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path,'wb') as f:
                        f.write(response.content)
                else:
                    print('Already Download',file_path)
    except requests.ConnectionError as e:
        print('Error',e.args)


json=get_page(0)
jiepai=get_images(json)
save_image(jiepai)

