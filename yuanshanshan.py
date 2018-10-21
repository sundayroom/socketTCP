import  urllib.request
import json
id='1320135280'
proxy_addr="122.241.72.191:808"
def user_proxy(url,proxy_addr):
    req=urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode('utf-8')
    return  data
def get_containerid(url):
    data=user_proxy(url,proxy_addr)
    print(data)
    content=json.loads(data).get('data')
    for tag in content.get('tabsInfo').get('tabs'):
        if tag.get('tab_type')=='weibo':
            containerid=tag.get('containerid')
    return  containerid
def get_user_info(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    data=user_proxy(url,proxy_addr)
    print(data)
    content=json.loads(data).get('data')
    user={}
    user['id']=content.get('userInfo').get('id')
    user['statuses_count']=content.get('userInfo').get('statuses_count')
    user['gender']=content.get('userInfo').get('gender')
    user['followers_count']=content.get('userInfo').get('follower_count')
    user['follow_count']=content.get('userInfo').get('follow_count')
    user['profile_url']=content.get('userInfo').get('profile_url')
    yield user

def get_weibo(id,file):
    i=1
    while True:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            data=user_proxy(weibo_url,proxy_addr)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(len(cards)>0):
                for j in range(len(cards)):
                    print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
                    card_type=cards[j].get('card_type')
                    if(card_type==9):
                        mblog=cards[j].get('mblog')
                        attitudes_count=mblog.get('attitudes_count')
                        comments_count=mblog.get('comments_count')
                        created_at=mblog.get('created_at')
                        reposts_count=mblog.get('reposts_count')
                        scheme=cards[j].get('scheme')
                        text=mblog.get('text')
                        with open(file,'a',encoding='utf-8') as fh:
                            fh.write("----第"+str(i)+"页，第"+str(j)+"条微博----"+"\n")
                            fh.write("微博地址："+str(scheme)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+text+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")
                i+=1
            else:
                break
        except Exception as e:
            print(e)
            pass

url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
get_user_info(id)
get_containerid(url)
get_weibo(id,'mayun.txt')
