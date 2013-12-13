#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template
import bottle
import urllib2,sys,re,os,json

from time import sleep

singleToken=""
headers = {'User-Agent':'Android4.1.1/yyting/Xiaomi/MI 2A/ch_google/78'}

# http://www.yytingting.com/yyting/usercenter/AutoRegister.action?regid=NDYwMDA0MzMwNjY2MTg1&regmei=ODYwNjcwMDI0NjA2MTM4
def getToken():
    global singleToken
    print singleToken
    if singleToken == "" or (random() < 2):
        url = 'http://www.yytingting.com/yyting/usercenter/AutoRegister.action?regid=NDYwMDA0MzMwNjY2MTg1&regmei=ODYwNjcwMDI0NjA2MTM4'
        ####### dict结构，可以加入x-forward-for甚至refer等 ######
        global headers
        req = urllib2.Request(url ,headers = headers)
        html = urllib2.urlopen(req).read()
        decodejson = json.loads(html)
        singleToken = decodejson['token']
        return singleToken
    else:
        return singleToken

def getPageJson(typeid = 0):
    url = 'http://www.yytingting.com/yyting/bookclient/ClientTypeResource.action?type='+str(typeid)+'&pageNum=0&pageSize=100&token='+getToken()
    global headers
    req = urllib2.Request(url ,headers = headers)
    html = urllib2.urlopen(req).read()
    decodejson = json.loads(html)
    return decodejson

def getBookPageJson(id):
    url = 'http://www.yytingting.com/yyting/bookclient/ClientGetBookDetail.action?id='+str(id)+'&token='+getToken()
    global headers
    req = urllib2.Request(url ,headers = headers)
    html = urllib2.urlopen(req).read()
    decodejson = json.loads(html)
    return decodejson

def showIndexList(decodejson):
    # for i in json['list']
    # return decodejson['list']
    node = []
    for i in decodejson['list']:
        if i['desc'] == None:
            i['desc'] = ""
        node.append((str(i['id']),i['name'],i['desc']))
        # node = node + str(i['id']) + "<br>"+ i['name']+"<br>"+i['desc']+"<br>"
    return node

def random():
    from random import randint
    return randint(0,10) #Inclusive

def showBookDesc(bookid):
    url = 'http://www.yytingting.com/yyting/bookclient/ClientGetBookDetail.action?id='+bookid+'&token='+getToken()
    global headers
    req = urllib2.Request(url ,headers = headers)
    html = urllib2.urlopen(req).read()
    desc = json.loads(html)

    book = {}
    book['desc'] = desc
    book['token'] = getToken()
    return book

@route('/book/<id>/page/<pageno>')
def getBookSounds(id,pageno):
    #print id , pageno
    url = 'http://www.yytingting.com/yyting/bookclient/ClientGetBookResource.action?bookId='+id +'&pageNum='+pageno+'&pageSize=50&token='+getToken()
    global headers
    req = urllib2.Request(url ,headers = headers)
    html = urllib2.urlopen(req).read()
    #decodejson = json.loads(html)
    return html

@route('/resource/<id>')
def getResource(id):
    # print type(id)
    if int(id) < 104:
        lits = showIndexList(getPageJson(id))
        return template('lanren_index', lits=lits)
    else:
        descs = showBookDesc(id)
        return template('lanren_book', map=descs)

@route('')
@route('/ll')
def index():
    # return template('<b>token = {{token}}</b>!', token=getToken())
    lits = showIndexList(getPageJson())
    # print len(lits)
    # for i in showIndexList(getPageJson()):
    # 	lits = temp +'<div>'+i[0]+'<br>'+i[1]+'<br>'+i[2]+'</div>'
    # print temp
    return template('lanren_index', lits=lits)

def yz():
    return (1,2,'往往')

# run(host='192.168.5.100', port=8080)

run(host='0.0.0.0', port=8000)
# 0.0.0.0
# bottle.run(server='gunicorn')

# if __name__ == '__main__':
# 	print yz()[1]
    # print getToken()
    # print getPageJson()
    # print showIndex(getPageJson())

# 	while 1:
# 		# print random()
# 		print getToken()
# 		sleep(1)
# 	# print singleToken
