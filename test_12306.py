#!/usr/bin/etc python
#encoding=utf-8

import urllib, urllib2, cookielib, sys
import ssl
from bs4 import BeautifulSoup as bs
from verbose_http import VerboseHTTPHandler

reload(sys)
sys.setdefaultencoding('utf-8')

ssl._create_default_https_context = ssl._create_unverified_context
cj = cookielib.CookieJar()
cookie_opener = urllib2.build_opener(VerboseHTTPHandler, urllib2.HTTPCookieProcessor(cj))


q = {
"purpose_codes": "ADULT",
"queryDate": "2016-10-02",
"from_station": "SHH",
"to_station": "NCG"
}
url = "https://kyfw.12306.cn/otn/lcxxcx/query?"+urllib.urlencode(q)

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, sdch, br',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cache-Control': 'no-cache',
'Connection': 'keep-alive',
#'Cookie': 'JSESSIONID=4B68ECF590A8654B0B73426503377A6C; BIGipServerotn=267387402.50210.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5357%u660C%2CNCG; _jc_save_fromDate=2016-10-02; _jc_save_wfdc_flag=dc',
'Host': 'kyfw.12306.cn',
'If-Modified-Since': '0',
'Referer': 'https://kyfw.12306.cn/otn/lcxxcx/init',
'Upgrade-Insecure-Requests': 1,
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

url1=""
request1 = urllib2.Request(url, headers=headers)
response = cookie_opener.open(request1).read()

request2= urllib2.Request(url, headers=headers)
response = cookie_opener.open(request2).read()

print response
