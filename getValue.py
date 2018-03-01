import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib
import urllib2
import re
import sys
from bs4 import BeautifulSoup
import os
import json

cnt = 0
file = open('List.txt','w')
ansdic = {}
while(os.path.exists('result%i.html'%cnt)):
    _b = False
    soup = BeautifulSoup(open('result%i.html'%cnt),'lxml')
    #print soup.prettify()
    for y in soup.descendants:
        #print y
        if y.name == 'tr':
            for ch in y.children:
                if(not ch.string):
                    for x in ch.strings:
                        if x == 'Born':
                            _b = True
                else:
                    if ch.string == 'Born':
                        _b = True
        if(_b):
            if y.name == 'td':
            #print y
                for ch in y.children:
                    if(not ch.string):
                        for x in ch.strings:
                            xlist = x.split(' ')
                            for word in xlist:
                                if (ansdic.has_key(word)):
                                    ansdic[word].add(cnt)
                                else:
                                    ansdic[word]=set([cnt])
                    else:
                        xlist = ch.string.split(' ')
                        for word in xlist:
                            if (ansdic.has_key(word)):
                                ansdic[word].add(cnt)
                            else:
                                ansdic[word]=set([cnt])
    cnt += 1

for x in ansdic:
    ansdic[x] = list(ansdic[x])

file.write(json.dumps(ansdic))
