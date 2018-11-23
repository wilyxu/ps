#批量处理图片  缩放图片
from PIL import Image
import os,re

myPath='./image/'

outPath='./desting/'

def processImage(filesource,destsource,name,imgtype,strPath):
    imgtype='jpeg' if imgtype=='.jpg' else 'png'

    #打开图片
    #print(dir(Image))

    imagepath1=strPath+"\\"+name

    im=Image.open(imagepath1)

    #缩放比例
    rate=max(im.size[0]/640.0 if im.size[0]>640 else 0,im.size[1]/1136 if im.size[1]>1136 else 0)
    if rate:
        im.thumbnail((im.size[0]/rate,im.size[1]/rate))

    string=os.path.dirname(os.getcwd())   #取当前目录上级目录
    im.save(string+"\\desting\\"+name,imgtype)

def run():
    #切换到源目录，遍历源目录下所有图片
    os.chdir(myPath)

    #print( os.listdir(os.getcwd()))

#    aList=[('aa'),('bb')]
#    for i in aList:
#        print(i)


    for i in  os.listdir(os.getcwd()):
       postfix=os.path.splitext(i)[1]
       if postfix=='.jpg' or postfix=='.png':
           processImage(myPath,outPath,i,postfix,os.getcwd())



#---------------------------------------------------------------
##    统计代码行数    （有用）

def analyze_code(codefilesource):
    '''
    打开一个py文件，统计其中的代码行数，包括空行和注释
    返回含该文件总行数，注释行数，空行数的列表
    '''
    total_Lines=0
    comment_LInes=0
    blank_Lines=0

    with open(codefilesource,encoding='utf-8') as f:
        Lines=f.readlines()
        total_Lines=len(Lines)
        Lines_index=0
        #遍历每一行
        while Lines_index<total_Lines:
            Line=Lines[Lines_index]
            #检查是否为注释
            if Line.startswith("#"):
                comment_LInes+=1
            elif re.match("\s*'''",Line) is not None:
                comment_LInes+=1
                while re.match(".*'''$",Line) is None:
                    Lines=Lines[Lines_index]
                    comment_LInes+=1
                    Lines_index+=1
            #检查是否为空行
            elif Line=="\n":
                blank_Lines+=1

            Lines_index+=1
    print("在%s中："%codefilesource)
    print("代码行数:",total_Lines)
    print("注释行数:",comment_LInes,"占%0.2f%%"%(comment_LInes*100/total_Lines))
    print("空行数:",blank_Lines,"占%0.2f%%"%(blank_Lines*100/total_Lines))

    return [total_Lines,comment_LInes,blank_Lines]


def runCalCodeLines(FILE_PATH):
    #切换到code所在目录
    os.chdir(FILE_PATH)
    #遍历该目录下的py文件
    total_Lines=0
    total_comment_Lines=0
    total_blank_Lines=0

    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1]=='.py' and os.path.splitext(i)[0]=="yingyonganli2":
            Line=analyze_code(i)
            total_Lines,total_comment_Lines,total_blank_Lines=total_Lines+Line[0],total_comment_Lines+Line[1],total_blank_Lines+Line[2]

    print("总代码行数:",total_Lines)
    print("总注释行数：",total_comment_Lines)
    print("总空行数：",total_blank_Lines)


if __name__=='__main__':
    #run()
    print("aa:","ss")
    runCalCodeLines("./")