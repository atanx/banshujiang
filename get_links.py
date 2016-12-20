#!/usr/bin/etc python
#encoding=utf-8

import urllib, urllib2, cookielib, sys
from bs4 import BeautifulSoup as bs
from verbose_http import VerboseHTTPHandler
import requests
import traceback
import re

reload(sys)
sys.setdefaultencoding('utf-8')

def get_one(idx):
	host = 'http://www.banshujiang.cn'
	try:
		url = 'http://www.banshujiang.cn/e_books/%d'%idx
		#url = 'http://www.banshujiang.cn/e_books/1856/webstorage_links/5376/to_link'
		ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
		headers = {'User-Agent':ua}
	
		# 获取授权token
		response = requests.get(url).content
		sp = bs(response, 'html.parser')
		title = sp.find('div',{'class':'ebook-title'}).text.strip()
		a = [host+i.get('href') for i in sp.find_all('a',{'href':re.compile(r'webstorage_links')})]
		for i in a:
			print '%d#%s#%s'%(idx, title, i)
	
	except:
		response = ''
		traceback.print_exc()
		pass
	return response
		#print "搬书匠网址：%s\n百度网盘地址：%s\n提取密码: %s"%(url, source, code)


# 


for i in range(540,3000):
	html = get_one(i)
	if "The page you were looking for doesn't exist." in html:
		break
	else:
		sys.stderr.write('process %d\n'%i)




