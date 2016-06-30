#encoding=utf8
import urllib2
import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http://www.xicidaili.com/nn/1'
headers = {'Accept':'text/html, application/xhtml+xml, */*',
                   'Accept-Language':'zh-CN',
                   'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) QQBrowser/8.2.4257.400'
                   }
req = urllib2.Request(url,headers=headers)
res = urllib2.urlopen(req,timeout=5).read()
#print res
soup = BeautifulSoup.BeautifulSoup(res)
ips = soup.findAll('tr')
f = open("./src/proxy.txt","w")

for x in range(1,len(ips)):
    ip = ips[x]
    tds = ip.findAll("td")
    #print tds
    ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]+"\t"+tds[8].contents[0]+"\n"
    #print tds[2].contents[0]+"\t"+tds[3].contents[0]
    print ip_temp
    f.write(ip_temp)
