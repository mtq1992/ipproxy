#encoding=utf8
import urllib
import socket
socket.setdefaulttimeout(3)
f = open("./src/proxy.txt")
lines = f.readlines()


proxys = []
for i in range(0,len(lines)):
	ip = lines[i].strip("\n").split("\t")
	proxy_host = "http://"+ip[0]+":"+ip[1]
	proxy_temp = {"http":proxy_host}
	proxys.append(proxy_temp)
url = "https://www.baidu.com/"
"""
headers = {'Accept': 'text/html, application/xhtml+xml, */*',
		   'Accept-Language': 'zh-CN',
		   'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) QQBrowser/8.2.4257.400'
		   }
"""
for proxy in proxys:
	try:

		res = urllib.urlopen(url,proxies=proxy).read()
		#print res
		print proxy
		print 'ok!!!!!!'
	except Exception,e:
		print proxy
		print 'error!!!!!'
		#print e
		continue
