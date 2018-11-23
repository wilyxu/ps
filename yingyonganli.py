#----------------------------------------------------------
#画图操作
from PIL import Image,ImageFont,ImageDraw

im=Image.open("./11.jpg")
draw=ImageDraw.Draw(im)

print(im.size)

fontsize=min(im.size)/4

font=ImageFont.truetype("D:\CodePy\FirstTest\Demo\pzh.ttf",20)

draw.text((30,30),'hello boy 小伙子',fill=(255,0,0),font=font) #图像中写文字

draw.line((0, 0) + im.size, fill=125)     #图像中画线

draw.line((550,0,0,342),fill=125)   #图像中画线

im.save('./aaa.jpg','jpeg')

#------------------------------------------------------------------------
#生成随机数，序列号
import string,random

field=string.ascii_letters + string.digits

#取4个随机字符  英文+数字
def getRandom():
    return "".join(random.sample(field,4))

#生成的每个激活码有几组
def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

def generate(n):
    return [concatenate(8) for i in range(n)]

if __name__=='__main__':
    print(generate(200))

#--------------------------------------------------------------
#统计文字出现的次数，这个挺牛逼的
import re
from collections import Counter

def getMostCommonWord(articlefile):
    pattern=r'''[A-Za-z]+|\$:\d+%?$'''   #加上r 按照本意输出
    with open(articlefile) as f:
        r=re.findall(pattern , f.read())
        print(r)
        print('-'*100)
        return Counter(r).most_common()


if __name__=='__main__':
    print(getMostCommonWord('hello.txt'))