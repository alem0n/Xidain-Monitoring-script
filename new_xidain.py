import requests
import os
import datetime
import time
import re
from bs4 import BeautifulSoup
i = 0

def get_date1():
    url='https://gr.xidian.edu.cn/yjsy/yjszs.htm'
    r = requests.get(url)
    html=r.content
    html_doc=str(html,'utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    date_old_list = []
    for k in soup.find_all('li'):
        if k.span != None:
            date_old_list.append('https://gr.xidian.edu.cn/' + k.a.get('href').replace('../',''))
    return date_old_list

def get_date2():
    url='https://gr.xidian.edu.cn/yjsy/yjszs.htm'
    r = requests.get(url)
    html=r.content
    html_doc=str(html,'utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    date_new_list = []
    time_new_list = []
    for k in soup.find_all('li'):
        if k.span != None:
            date_new_list.append('https://gr.xidian.edu.cn/' + k.a.get('href').replace('../',''))
            time_new_list.append(k.span.string.strip())
    return date_new_list,time_new_list

def get_now_date():
    #now_date = datetime.datetime.now() - datetime.timedelta(days=4)
    now_date = datetime.datetime.now()
    now_date = now_date.strftime("%Y-%m-%d")
    now_date2 = datetime.datetime.now()
    return now_date,now_date2

def send_message(date):
    payload = {'text': '今天有一条新信息，第' + str(i) +'次提醒', 'desp': '今天有一条新信息，第' + str(i) + '次提醒\n' + date}
    now_code1 = requests.get("https://sc.ftqq.com/.send", params=payload)
    now_code2 = requests.get("https://sc.ftqq.com/.send", params=payload)
    print(now_code1)
    print(now_code2)
    
date_old_list = get_date1()
while True:
    os.system('cls')
    date_new_list,time_new_list = get_date2()
    #date_new_list.append('https://gr.xidian.edu.cn/yjsy/yjszs.htm')
    now_date,now_date2= get_now_date()
    print('最新文章时间')
    print(time_new_list[0])
    print(time_new_list[1])
    print('当前时间' + str(now_date2) )
    for j in date_new_list:
        if j not in date_old_list:
            send_message(j)
            i += 1
            print('今天有一条新信息，第' + str(i) +'次提醒\n')
        else:
            pass
         
    print( '十分钟后继续')
    time.sleep(600)
    #time.sleep(6)
