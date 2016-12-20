#!/usr/bin/etc python
#encoding=utf-8

import urllib, urllib2, cookielib, sys
from bs4 import BeautifulSoup as bs
from verbose_http import VerboseHTTPHandler
import requests
import traceback
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def get_one(url):
	try:
		Referer = url
		#url = 'http://www.banshujiang.cn/e_books/1856/webstorage_links/5376/to_link'
		ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
		headers = {'User-Agent':ua, 'Referer':Referer}
	
		# 获取授权token
		response = requests.get(url, headers=headers).content
		soup = bs(response, 'html.parser')
		utf8 = soup.find('input',attrs={'name':"utf8"}).get('value')
		token = soup.find('input',attrs={'name':"authenticity_token"}).get('value')

		# post token获取提取码
		data = {'utf8':utf8,'authenticity_token':token}
		#data = urllib.urlencode(data)
		response = requests.post(url, data, headers=headers).content
		soup = bs(response, 'html.parser')
		code = soup.find('div').contents[0][-4:]
		source = soup.find('iframe').get('src')
		print '%s#%s'%(source,code)
		return True
	except:
		sys.stderr.write(response)
		traceback.print_exc()
		pass
		return False
		#print "搬书匠网址：%s\n百度网盘地址：%s\n提取密码: %s"%(url, source, code)

cnt = 0
for line in sys.stdin:
	parts = line.strip().split('#')
	flag = get_one(parts[2])
	cnt += 1
	sys.stderr.write( 'No.%d'%cnt)
	if flag:
		sys.stderr.write('[success]\n')
	else:
		sys.stderr.write( '[failed]\n')
	time.sleep(5)
