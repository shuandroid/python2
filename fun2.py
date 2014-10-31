#coding:utf-8
import re
import os
import sys
import urllib2
from bs4 import BeautifulSoup

#---------------------
def getStore(title,url):
    #text = urllib2.urlopen(url)
    #text  = url
    #context = text.read();
    context = url
    title2 = title
    #print 'zaizheli 2222222'
    thefrom = context.find(r'href=')+6
    theto = context.find(r'target=') - 2
    forcontext= 'http://www.jianshu.com'+context[thefrom:theto]
    context2 = urllib2.urlopen(forcontext).read()
    soup_store = BeautifulSoup(context2)
    #print '3333333'
    #path = '/home/chen/python/jianshu2/'+title2
    
    #text.close()                          waiting......
    #store(path)
    filename = soup_store.title.string + '.markdown'
    print filename
    #get the content
    f = open(filename,'wb+')    
    res_store = re.compile(r'<div class="show-content">[\s\S]*?</div>')
    thecontext = re.findall(res_store,context2.decode('utf8'))
    thecontext =  thecontext[0]
    thecontext = thecontext.replace('<p>','')
    thecontext = thecontext.replace('</p>','')
    f.write(thecontext.encode('utf8'))
    f.close()
def store (path):
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)
    
#==============================get the title==========================
'''def getTitle(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    #title = soup.find('title')
    title = soup.title.string
    string = str(title)
    return string[7 : -28]

def Judge(title):
    lens = len(title)
    for i in xrange(0,lens):
        if title[i] == '*':
            return False
    return True
 '''
#-----------------
def getPageURLs(m):
    #text = urllib2.urlopen(url).read()
    #print text
    text = m
    #pattern = r'<h4><a href="/p/.+" target="_blank" >.*</a></h4>'
    regex = re.compile(r'<h4><a href="/p/.*" target="_blank">.*</a></h4>') 
    urlList = re.findall(regex,text)
    #print 'zai zheli'
    return urlList

#------------------
def getAllURLs():
    global count,pagenum       #count  shi jishuqi,,,the shi ti huan de biao da shi.
    pagenum = 0
    count = 0
    forpagenum = 0
    urls = ['http://www.jianshu.com/collection/5519553f7aec',
            'http://www.jianshu.com/collection/566fa0025d60',
            'http://www.jianshu.com/collection/655e6db2abc7']    
    #////////////////////////////////////////////////
    for ur in urls:
        print ur
        while(True):
            
            if count%9==0:
                pagenum = pagenum + 1
            #get the number
            s1 = ur+'/top?page=' + str(pagenum)           
            m1 = urllib2.urlopen(s1).read()
            soup1 = BeautifulSoup(m1)
            #print soup1
            #print pagenum
            contentname = soup1.title.string
            print 'this'+contentname+'article'
            path = '/home/chen/python/article/jianshu/' + contentname                               #创建文件夹
            store(path)
            #break
            urlList2 = getPageURLs(m1)
            #print urlList2             bingo debug!
            for thelist in urlList2:
                count += 1
                forpagenum += 1
                print count
                #print 'yunxing'
                getStore(contentname,thelist)
                if(forpagenum>99):
                    forpagenum = 0
                    break
            if(count > 99):
                count = 0
                break        

    #////////////////////////////////////////////////
        
    #------------------increase threads....
    
    print 'the work is over'    
if __name__ == '__main__':
    print 'the article is searching...'    
    getAllURLs()



