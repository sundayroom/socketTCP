import urllib.request
import json

#定义要爬取的微博大V的微博ID
id='1320135280'

#设置代理IP
proxy_addr="122.241.72.191:808"

#定义页面打开函数
def use_proxy(url,proxy_addr):
    req=urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode('utf-8','ignore')
    return data

#获取微博主页的containerid，爬取微博内容时需要此id
def get_containerid(url):
    data=use_proxy(url,proxy_addr)
    content=json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if(data.get('tab_type')=='weibo'):
            containerid=data.get('containerid')
    print(containerid)
    return containerid

#获取微博大V账号的用户基本信息，如：微博昵称、微博地址、微博头像、关注人数、粉丝数、性别、等级等
def get_userInfo(id):
    url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
    data=use_proxy(url,proxy_addr)
    content=json.loads(data).get('data')
    profile_image_url=content.get('userInfo').get('profile_image_url')
    description=content.get('userInfo').get('description')
    profile_url=content.get('userInfo').get('profile_url')
    verified=content.get('userInfo').get('verified')
    guanzhu=content.get('userInfo').get('follow_count')
    name=content.get('userInfo').get('screen_name')
    fensi=content.get('userInfo').get('followers_count')
    gender=content.get('userInfo').get('gender')
    urank=content.get('userInfo').get('urank')
    print("微博昵称："+name+"\n"+"微博主页地址："+profile_url+"\n"+"微博头像地址："+profile_image_url+"\n"+"是否认证："+str(verified)+"\n"+"微博说明："+description+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+gender+"\n"+"微博等级："+str(urank)+"\n")


#获取微博内容信息,并保存到文本中，内容包括：每条微博的内容、微博详情页面地址、点赞数、评论数、转发数等
def get_weibo(id,file):
    i=1
    while True:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            data=use_proxy(weibo_url,proxy_addr)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(len(cards)>0):
                for j in range(len(cards)):
                    #print("-----正在爬取第"+str(i)+"页，第"+str(j)+"条微博------")
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

if __name__=="__main__":
    file=id+".txt"
    get_userInfo(id)
    get_weibo(id,file)

# data={
#     {"ok":1,"data":
#         {"userInfo":{"id":1320135280,
#                      "screen_name":"\u8881\u59d7\u59d7",
#                      "profile_image_url":"https:\/\/tva3.sinaimg.cn\/crop.0.0.1136.1136.180\/4eafaa70jw8em0cj6p2nnj20vk0vk427.jpg",
#                      "profile_url":"https:\/\/m.weibo.cn\/u\/1320135280?uid=1320135280&luicode=10000011&lfid=1005051320135280",
#                      "statuses_count":2943,
#                      "verified":true,
#                      "verified_type":0,
#                      "verified_type_ext":1,
#                      "verified_reason":"\u6f14\u5458\uff0c\u4ee3\u8868\u4f5c\u300a\u714e\u997c\u4fa0\u300b\u300a\u56fd\u6c11\u5927\u751f\u6d3b\u300b\u300a\u5bab\u9501\u73e0\u5e18\u300b\u7b49",
#                      "close_blue_v":false,
#                      "description":"\u5de5\u4f5c\u90ae\u7bb1\uff1aishanshan033@163.com",
#                      "gender":"f",
#                      "mbtype":12,
#                      "urank":43,
#                      "mbrank":6,
#                      "follow_me":false,
#                      "following":false,
#                      "followers_count":28792481,
#                      "follow_count":420,
#                      "cover_image_phone":"https:\/\/tva2.sinaimg.cn\/crop.0.0.640.640.640\/a1d3feabjw1ecasunmkncj20hs0hsq4j.jpg",
#                      "avatar_hd":"https:\/\/ww3.sinaimg.cn\/orj480\/4eafaa70jw8em0cj6p2nnj20vk0vk427.jpg",
#                      "like":false,
#                      "like_me":false,
#                      "toolbar_menus":[{"type":"profile_follow","name":"\u5173\u6ce8","pic":"","params":{"uid":1320135280}},
#          "avatar_guide":[],"fans_scheme":"https:\/\/m.weibo.cn\/p\/index?containerid=231051_-_fans_intimacy_-_1320135280&luicode=10000011&lfid=1005051320135280","follow_scheme":"https:\/\/m.weibo.cn\/p\/index?containerid=231051_-_followersrecomm_-_1320135280&luicode=10000011&lfid=1005051320135280",
#          "tabsInfo":{"selectedTab":1,"tabs":[{"title":"\u4e3b\u9875","tab_type":"profile","containerid":"2302831320135280"},
#                                              {"title":"\u5fae\u535a","tab_type":"weibo","containerid":"1076031320135280","apipath":"\/profile\/statuses","url":"\/index\/my"},
#                                              {"title":"\u8d85\u8bdd","tab_type":"cardlist","containerid":"2314751320135280"},
#                                              {"title":"\u76f8\u518c","tab_type":"album","containerid":"1078031320135280","filter_group_info":{"title":"\u5168\u90e8\u7167\u7247(0)","icon":"http:\/\/u1.sinaimg.cn\/upload\/2014\/06\/10\/userinfo_icon_album.png","icon_name":"\u4e13\u8f91","icon_scheme":""}}]},
#          "showAppTips":1,"scheme":"sinaweibo:\/\/userinfo?uid=1320135280&luicode=10000011&lfid=1005051320135280&from=1110006030"}}

# }