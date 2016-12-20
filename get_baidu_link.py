#!/usr/bin/etc python
#encoding=utf-8

import urllib, urllib2, cookielib, sys
from bs4 import BeautifulSoup as bs
from verbose_http import VerboseHTTPHandler

reload(sys)
sys.setdefaultencoding('utf-8')

#cj = cookielib.CookieJar()
cookie_opener = urllib2.build_opener(VerboseHTTPHandler)#, urllib2.HTTPCookieProcessor(cj))

Referer = url = sys.argv[1]
#Referer = url = 'http://www.banshujiang.cn/e_books/1856/webstorage_links/5376/to_link'
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
headers = {'User-Agent':ua, 'Referer':Referer}

# 获取授权token
request1 = urllib2.Request(url, headers=headers)
response = cookie_opener.open(request1).read()
soup = bs(response, 'html.parser')
utf8 = soup.find('input',attrs={'name':"utf8"}).get('value')
token = soup.find('input',attrs={'name':"authenticity_token"}).get('value')

# post token获取提取码
data = {'utf8':utf8,'authenticity_token':token}
data = urllib.urlencode(data)
request2 = urllib2.Request(url, data, headers=headers)
response = cookie_opener.open(request2).read()
soup = bs(response, 'html.parser')
code = soup.find('div').contents[0][-4:]
source = soup.find('iframe').get('src')

print "搬书匠网址：%s\n百度网盘地址：%s\n提取密码: %s"%(url, source, code)

