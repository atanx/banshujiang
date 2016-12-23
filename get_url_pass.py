#!/usr/bin/etc python
#encoding=utf-8

import urllib, urllib2, cookielib, sys
from bs4 import BeautifulSoup as bs
#from verbose_http import VerboseHTTPHandler
import requests
import traceback
import time
import agents
import random
import os

os.chdir(sys.path[0])
reload(sys)
sys.setdefaultencoding('utf-8')
def get_one(url):
	global ua
	try:
		Referer = url
		#url = 'http://www.banshujiang.cn/e_books/1856/webstorage_links/5376/to_link'
		#ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
		ua=random.choice(agents.AGENTS_ALL)
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
		r = '%s#%s'%(source,code)
		return True, r
	except:
		traceback.print_exc()
		sys.stderr.write(response)
		return False,""
		# print "搬书匠网址：%s\n百度网盘地址：%s\n提取密码: %s"%(url, source, code)


# 读取已经获取的密码
exists = []
for line in open('pass.txt','r'):
	parts = line.split('#')
	if parts:
		exists.append(parts[0])

err_cnt = 0 #连续出现10次未成功解析，退出程序
f = open('pass.txt', 'a+')
for line in open('links.txt', 'r'):
	parts = line.strip().split('#')
	sys.stderr.write("%s#" % parts[0])
	if parts[0] not in exists and 'http' in parts[2]:
		flag, r = get_one(parts[2])
		if flag:
			exists.append(parts[0])
			f.write('%s#%s\n' % (parts[0], r))
			sys.stderr.write('[success]\n')
			err_cnt = 0
		else:
			sys.stderr.write('[failed]\n')
			err_cnt += 1
			if err_cnt>= 10:
				break
	#		ua=agents.AGENTS_ALL.pop()
	else:
		sys.stderr.write('[existes]\n')
