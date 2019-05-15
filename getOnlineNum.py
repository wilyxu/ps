#coding=utf-8
import re
import requests
import datetime


# 1 获取网页内容
def get_html(url):
    s = requests.session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

        "Cookie": "Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1528353702; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1528353815"
    })
    r = s.get(url, timeout=10)
    return r.text

#print(get_html(url))

REGEXTime=re.compile("\d{4}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2}")
REGEXnUM=re.compile("[0-9]+\&lt;/+[a-zA-Z\d]+\&")
RegxInt=re.compile("[0-9]+")

def get_Content(html):
    strTime=re.findall(REGEXTime,html)
    print(f"{strTime}")

    strNum=re.findall(REGEXnUM,html)

    #print(strNum)

    iCommonCar = 0
    iSpcCar = 0
    icount=0    #计数器

    #写入txt文件中
    #strDate=time.strftime('%Y-%m-%d')
    filename = open("wily.txt", "a")
    filename.write(f"{strTime}"+"\n")

    #遍历打印出来
    for strCount in  strNum:
        print(strCount.replace('&lt;/',' | ').replace('&',''))
        filename.write(strCount.replace('&lt;/',' | ').replace('&','')+"\n")

        icount = icount + 1
        #print(type(strCount))
        #if(strCount.find(r"OnlineNum")>=0):      这个是判断字符是否存在
        if(icount==1):
            iCommonCar=re.findall(RegxInt,strCount)
        if(icount==4):
            iSpcCar=re.findall(RegxInt,strCount)

    #print(iCommonCar[0])
    #print(iSpcCar[0])
    print("即时上线率: "+str(round((int(iCommonCar[0])+int(iSpcCar[0]))/4803,4)*100)+"%","\n")

    filename.write("即时上线率: "+str(round((int(iCommonCar[0])+int(iSpcCar[0]))/4803,4)*100)+"%"+"\n\n")
    filename.close()


import threading
def printTaxiNum():
    try:
        strXml = "<Document TaskGuid = \"38726e0a-be8d-4937-ae8d-1444424c4e0a\" DataType = \"OnlineNum\"><CompGuid Type=\"GUID\"></CompGuid></Document>"
        strUrl = 'http://10.8.64.123/Communicate.asmx/TransformData?userid=38726e0a-be8d-4937-ae8d-1444424c4e0a&TaskGuid=38726e0a-be8d-4937-ae8d-1444424c4e0a&XmlTransform=' + strXml
        get_Content(get_html(strUrl))
        t = threading.Timer(30, printTaxiNum)
        t.start()
    except:
        print('网络错误')
        t = threading.Timer(30, printTaxiNum)
        t.start()

if __name__ == "__main__":
    printTaxiNum()

