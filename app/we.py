#-*- coding: UTF-8 -*- 
import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import http.cookiejar


def main(email,password): 
    url='https://api-dist.uniqueway.com/v1/authenticate'
    data={}
    #data={"email":"1309464595@qq.com","password":"Hnhw1234"}
    data["email"]=email
    data["password"]=password
    data=urlencode(data)#将字典类型的请求数据转变为url编码
    data=data.encode('ascii')#将url编码类型的请求数据转变为bytes类型
   #将url和请求数据处理为一个Request对象，供urlopen调用
   
    #自动记住cookie
    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(url, data)
   
    with opener.open(request) as res:
        print(res)
        res=res.read().decode('utf-8')#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
    cookie.save(ignore_discard=True, ignore_expires=True)
    return str(res)

def countries(): 
    url='https://api-dist.uniqueway.com/v1/countries?t=ewwrw3sd'  
    headers = {
        #伪装一个火狐浏览器
        "authority": 'api-dist.uniqueway.com',
        "method": 'GET',
        "path": '/v1/countries',
        "scheme": 'https',
        "cache-control":"no-chache",
        "accept": 'application/json, text/plain, */*',
        "accept-language":'zh-CN,zh;q=0.9',
        "authorization": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNzIxLCJleHAiOjE1MzY1OTE5MTl9.gocgbMigwk6O2bGSWAYmEdykogv-Gs1LBG5wIFjusAo',
        "if-none-match": 'W/"cf0d2a7150940e1fa6921a51856beuu"',
        "origin": 'https://dist.uniqueway.com',
        "referer": 'https://dist.uniqueway.com/',
        "user-agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    cookie = http.cookiejar.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True) 
    print(cookie)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    get_request = urllib.request.Request(url,headers=headers,method="GET")
    get_response = opener.open(get_request)#将url和请求数据处理为一个Request对象，供urlopen调用
    res=get_response.read().decode('utf-8')#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
    resut= str(res)
    return resut
