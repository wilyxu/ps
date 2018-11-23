#coding=utf-8

a=1
b=1

if a<b:
    print('aa')
elif a>b:
    print('bb')
else:
    print('cc')

inum=1
while inum<50:
    print(inum)
    inum=inum+1


for letter in 'python':
    print('CurrentL:',letter)
else:
    print('Hello')


#--------------dictionary------------------------------------
dict1={"aa":123,"bb":456}
print(dict1)
print(dict1["aa"],dict1["bb"])

for key in  dict1:
    print(key,dict1[key])

dict1["aa"]="11223123"   #可以改写
print(dict1)


#-------------------------------------------------------------
#字符串处理
str1='hello "wily"'
print(str1)
print(type(str1))

str2='''
    hello
    wily
    haha
    '''
print(str2)
print(str1[1])
print(str1[0:3])
print(str1[4:])

print('*'*100)

p='w' in str2
print(p)
#-------------------
print('hello\n\n')#转义字符自动会换行
print(r'hello\n\n')#加上r 按照本意输出


print("my name is %s and weight is %d kg" % ("wily",22))  #    %表示占位符

#--------------------
mystr='hello world haha and itcastcpp 2234'

print(mystr.find('ha'))  # find函数
print(mystr.find('ha',14))
print(mystr[15:])


print(help(mystr.find))

print(mystr.count('ha'))  #统计ha 在字符串里出现过几次

s2=mystr.encode(encoding='utf-8',errors='strict')
print(s2)

print(mystr.replace('ha','xx',1))  #把ha替换成xx,只替换一次

print(mystr.split(' ')) #分割字符串

print(mystr.isalnum())  #至少有一个字符是数字，返回true
#---------------------------------------------------------------------------------------
print('*第四课'*100)
#_______________________________________________________________________________________
s1="hello"
print(s1.isalpha())  #只包含字母的函数
print(s1.isdecimal()) #只包含十进制数字的
print(s1.islower())   #判断小写
print(s1.isupper())   #判断大写
s2='123'
print(s2.isnumeric()) #只包含数字
print(s1.isspace())   #只包含空格

print(s1.join(s2))    #分别插入字符

print(s1.ljust(10))   #左对齐 10个字符

s3="    kek111e   "
print(s3.lstrip().rstrip())    #去除左边空格  右边空格

print(s1.partition("l"))   #以l来进行分割，形成3部分
print(s1.rpartition("l"))   #加个r，从右边开始   以l来进行分割，形成3部分


def myfunction(strname):
    "hello"
    print(strname)
    return

if __name__=='__main__':
    myfunction("wily")

print("my name is %s and weight is %d kg" % ("wily",22))  #    %表示占位符


#不定长参数    *b就变成元组
def arglist(a,*b):
    print(a)
    print(b)

arglist(1,2,3,4,5,6)

# 2个* ，处理成字典
def argdic(a,**b):
    print(a)
    for i in b:
        print(i+" = "+ str(b[i]))

argdic("aaa",x=1,y=2)


# 匿名函数
sum=lambda a,b :a+b

print(sum(10,20))
print(type(sum))

#变量返回值
def isbool(p):
    if p=="false":
        return "false"

print(str(isbool("false")))

