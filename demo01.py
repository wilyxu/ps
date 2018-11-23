print("hello")#的的的
print("world")




import requests

#获取浏览器内容
#def get_html(url):
#    s=requests.session()
#    s.headers.update({
#        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
#    })
#    r=s.get(url,timeout=5)
#    return r.text
#
#print(get_html('http://www.xicidaili.com'))

import threading
def printHello():
    print('hello2222')
    t = threading.Timer(2, printHello)
    t.start()
if __name__ == "__main__":
    printHello()