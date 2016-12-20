#!/usr/bin/env python 

import StringIO, httplib, urllib2

class VerboseHTTPResponse(httplib.HTTPResponse):
	def _read_status(self):
		s=self.fp.read()
		print '-'*20, 'Response', '-'*20
		print s.split('\r\n\r\n')[0]
		self.fp = StringIO.StringIO(s)
		return httplib.HTTPResponse._read_status(self)
	
class VerboseHTTPConnection(httplib.HTTPConnection):
	response_class= VerboseHTTPResponse
	def send(self, s):
		print '-' * 50
		print s.strip()
		httplib.HTTPConnection.send(self,s)
	
class VerboseHTTPHandler(urllib2.HTTPHandler):
	def http_open(self, req):
		return self.do_open(VerboseHTTPConnection, req)

