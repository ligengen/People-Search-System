from django.shortcuts import render

from django.template import loader, Context

from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage

import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
gidList = []
gwordList = []
import time
def search(request):
    f = open('/Users/ligen/Desktop/wiki/List.txt','r')
    text = f.read()
    wordIndex = json.loads(text)
    try:
        wordList = []
        keyList = []
        keyList = request.GET['key'].split(' ')
        for key in keyList:
            wordList.append(key)

        idList = []
        for word in wordList:
            if wordIndex.has_key(word):
                if idList == []:
                    for id in wordIndex[word]:
                        idList.append(id)
                else:
                    tempIdList = []
                    for id in idList:
                        if id in wordIndex[word]:
                            tempIdList.append(id)
                    idList.extend(tempIdList)
        print idList
        global gidList
        gidList=  idList
        global gwordList
        gwordList = wordList
    except:
        global gidList
        global gwordList
        idList = gidList
        wordList = gwordList
    after_range_num = 5

    before_range_num = 4
    try:
        page = int(request.GET.get('page',1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    paginator = Paginator(idList, 10)

    try:
        idList = paginator.page(page)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        idList = paginator.page(paginator.num_pages)

    print idList
    if page >= after_range_num:
        page_range = list(paginator.page_range)[page-after_range_num:page+before_range_num]
    else:
        page_range = list(paginator.page_range)[0:page+before_range_num]

    result = []
    for id in idList:
        f = file('/Users/ligen/Desktop/wiki/result' + str(id) + '.txt' )
        text = f.read()
        f.close()

        for key in wordList:
            text = text.replace(key,'<span style = "color:red">' + key + '</span>')

        dic = {'url':id,'title':id,'text':text}
        result.append(dic)
    print idList
    return render(request, 'search.html', {'list': idList, 'result': result, 'page_range': page_range})

def match(request, num):
    print num
    return render(request, 'result%s.html'%num)
