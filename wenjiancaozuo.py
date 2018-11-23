str=input("please input your name:")   #需要在下面命令提示里输入
print(str)


##操作文件     写     读
filename=open("hello.txt","a+")    # w  是write 写的意思，如果没有文件，也会创建
filename.write("wily xu bbb")
filename.close()


filename2=open("hello.txt","r")    # r  是read 读的意思
buf=filename2.read()   #读所有字节   filename2.read(20)   读 20个字节
print(buf)
filename2.close()

print(filename2.closed)    # 看这个文件是否关闭
print(filename2.mode)      # 返回文件的访问模式  r  只读 | w  只写，如果文件不存在，则创建，如果文件存在，则清空再写 |  a  追加写，不存在则创建文件  | r+ 可读可写 | w+ 可读可写，如果文件不存在，则创建，如果文件存在，则清空再写| a+ 追加打开文件，可读可写，不存在则创建
print(filename2.name)      # 返回文件的名称

#r+  的操作比较奇怪，第一次r+  和  a 类似在末尾加上，第二次用则在头上覆盖
#有读写指针在
file1=open("hello.txt","r+")
file1.write(" ddd")
file1.flush()

#file1.close()


file1.read()
file1.seek(4) #指针从头开始
file1.write("xxxyyy")
file1.flush()    #存在内存,刷新，需要理解一下
file1.seek(0)    #把指针移到最开头
strres=file1.read()
print(strres)

file1.close()
#----------------------------------
file2=open("hello.txt","a")