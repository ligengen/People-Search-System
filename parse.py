import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import os
import time

cnt = 0
while(os.path.exists('result%i.html'%cnt)):
    soup = BeautifulSoup(open('result%i.html'%cnt),'lxml')
    file = open('result%i.txt'%cnt,'w+')
    for y in soup.descendants:
        if y.name == 'img':
            file.write(soup.img['alt'])
            file.write('\n')
            file.write(soup.img['src'])
            file.write('\n')
        #file.write()
        if y.name == 'tr':
            for ch in y.children:
                if (not ch.string):
                    for x in ch.strings:
                        file.write(x)
                else:
                    file.write(ch.string)
    cnt = cnt + 1
    if(not os.path.exists('result%i.html'%cnt)):
        time.sleep(50)




