# Developed by 诡锋
# bilibili/网易云音乐：诡锋丶The_Joker
# Youtube : SmokingSexyStyle
# Github : https://github.com/vincent-the-gamer
# Version 1.0

import requests
import bs4
from threading import Thread #用于多线程爬虫，爬取速度快，可以完成多页爬取
import os,time,urllib.request,ssl


ssl._create_default_https_context = ssl._create_unverified_context #禁止SSL证书的认证
session = requests.Session() #创建Session

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
"Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}



#直接下载图片
def downloadImages(num,path):  #页数，路径
    url = "https://konachan.com/post?page={}&tags=".format(num) #循环获取url
    req = session.get(url, headers=headers,stream=True)
    bs = bs4.BeautifulSoup(req.text,'lxml') #拿取url
    obj = bs.find_all("a",{"class":{"directlink"}}) #html标签,{标签的属性:{属性值}}

    objHtml = []                     #存放图片的url
    if not os.path.exists(path):
        os.makedirs(path)
    for f in obj:
        objHtml.append(f.get("href"))
    k = 0
    for i in objHtml:
        urllib.request.urlretrieve(i, filename=path+"/{}.jpg".format(k))
        k = k + 1
        #print(i)



#获取图片的路径
def writePathtoTxt(num,path):
    url = "https://konachan.com/post?page={}&tags=".format(num)
    req = session.get(url, headers=headers,stream=True)
    bs = bs4.BeautifulSoup(req.text,'lxml') #拿取url
    obj = bs.find_all("a",{"class":{"directlink"}})
    objHtml = []
    for f in obj:
        objHtml.append(f.get("href"))
    if not os.path.exists(path):
        os.makedirs(path)
    txt = open(path+"/images_url.txt", 'a')
    for i in objHtml:
      txt.write(i)
      txt.write("\n")


def executeImages(num,path):
    #start = time.time()
    threads = []
    for i in range(num):  # 要爬取多少页就输入几
        t = Thread(target=downloadImages, args=(i + 1,path))  # target 参数是对应的函数名称
        t.setDaemon(True)
        threads.append(t)
        t.start()
        time.sleep(1)

    for t in threads:
        t.join()        # 合并子线程到主线程，然后主线程结束


def executeUrls(num,path):
    #start = time.time()
    threads = []
    for i in range(num):  # 要爬取多少页就输入几
        t = Thread(target=writePathtoTxt, args=(i + 1,path))  # target 参数是对应的函数名称
        t.setDaemon(True)
        threads.append(t)
        t.start()
        time.sleep(1)

    for t in threads:
        t.join()        # 合并子线程到主线程，然后主线程结束
