import re
import requests
from multiprocessing.dummy import Pool as ThreadPool

#爬虫示例
#1 获取网页内容
def get_html(url):
	s=requests.session()
	s.headers.update({
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
		
		"Cookie": "Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1528353702; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1528353815"
	})
	
	r=s.get(url,timeout=5)

	return r.text

#print(get_html('http://www.xicidaili.com/'))

#-------------------------------------------------------------------------------------------------------
#2 print(get_html('http://www.xicidaili.com/'))

REGEX=re.compile("<td.*>([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)</td>[\n|\s]*<td.*>(\d{2,4})")

def get_ips(html):

	ips=re.findall(REGEX,html)

	return ips

#print (get_ips(get_html('http://www.xicidaili.com/')))

#-------------------------------------------------------------------------------------------------------
# check ips
proxy_list=[]

def checkip(ip):
	s=requests.session()
	s.headers.update({
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
	})
	proxies={}.fromkeys(['http','https'],f"{ip[0]}:{ip[1]}")

	try:
		r=s.get('http://www.baidu.com',timeout=5,proxies=proxies)
	except:
		print(f"{ip[0]}:{ip[1]} is lose...")
		return False

	print(f"{ip[0]}:{ip[1]} is ok!!!!!")

	proxy_list.append(ip)



if __name__=="__main__":
	ips=get_ips(get_html('http://www.xicidaili.com/'))


#for ip in ips:
#	checkip(ip)

#-------------------------------------------------------------------------------------------------------
# 多线程操作
	pool=ThreadPool(30)
	pool.map(checkip,ips)
	pool.close()
	pool.join()

	print(proxy_list)