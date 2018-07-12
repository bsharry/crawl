
# -*- coding: utf-8 -*- 

import urllib.request
import json
import time
urltmp='http://radar.itjuzi.com/investevent/info?location=in&orderby=def&page='
head1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
head = {
    'Host': 'radar.itjuzi.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent':' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer': 'http://radar.itjuzi.com/investevent',
    'Accept-Encoding':' gzip, deflate',
    'Accept-Language':' zh-CN,zh;q=0.9,zh-TW;q=0.8',
'Cookie':' '}

file = open("itjuzi.txt","wb")

def process(url):
    request = urllib.request.Request(url,headers=head)
    response = urllib.request.urlopen(request)
    #file=open("itjuzi.txt",'w')
    thing=response.read().decode()
    #file.write(thing)
    #file.close()
    tmp=json.loads(thing)
    data=tmp['data']
    rows=data['rows']
    return rows

def write(rows):
    for i in rows:
        s=add("",i['cat_name'])
        s=add(s,i['invse_id'])
        s=add(s,i['com_name'])
        s=add(s,i['round'])
        s=add(s,i['invsest_with'][0]['invst_name'])
        s=add(s,i['invsest_with'][0]['url'])
        s=add(s,i['money'])
        s=add(s,i['date'])
        s=add(s,i['com_id'])
        s=add(s,i['com_logo'])
        s+='\n'
        file.write(s.encode('utf-8'))
        
def add(a,b):
    return a+b+" "


for i in range(1,2337):
    url=urltmp+str(i)
    s="start processing "+url +"\n"
    print(s)
    rows=process(url)
    write(rows)
    s="process " +url+" complete!!!\n"
    time.sleep(1)
    print(s)
file.close()


