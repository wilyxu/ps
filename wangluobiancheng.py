
# post 用于爬虫  的用户登录，提交请求，包括用户名等
import requests

url=r'http://221.224.8.53:9001/IndustryLogin.aspx'
user={'username':'kgcz','txt_Password':'kgcz'}

s=requests.session()



headers = {"Content-Type": "application/x-www-form-urlencoded"}

r=s.post(url,data=user)

html=r.text
#print(html)


cookies={"_pk_id.100001.8cb4":"4233034746953d56.1534474870.1.1534474870.1534474870.",
         "_pk_ses.100001.8cb4":"*",
         "bid":"5Eg5yQ420CI",
         "ll":"118163"}
testurl='https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001'

req=requests.session()
s=req.get(testurl,cookies=cookies)

print(s)

