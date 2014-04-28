# -*- coding: UTF-8 -*-
import re
import sys
import os
from renrenapi import RenRen
from accounts import accounts
from BeautifulSoup import BeautifulSoup
import time
import sys
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')

allrp_pattern = re.compile(r"<b id='bTotalRpNum'>.*?</b>")
todayrp_pattern = re.compile(r"<b id='bTodayRpNum'>.*?</b>")
cookiePath = './login_cookie'

def getConnection():
    try:
        connect = MySQLdb.connect(host='localhost', user='root', passwd='', db='seuknower_paocao_development', port=3306)
        return connect
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def getMessage():
    for account in accounts:
        bot = RenRen()
        #result = bot.login(account[0], account[1])
        result = False
        if result:
            pass
        else:
            print 'login by cookie'
            if os.path.isfile(cookiePath):
                print 'cleantha'
                bot.loginByCookie(cookiePath)
                bot.email = '' 
            else:
                pass
        try:
            print "hehe"
            tyxpage = bot.getTyxPage()
            soup = BeautifulSoup(tyxpage)
            messages = soup.findAll('div', {'class': 'feed p-feed-item status'})
            message = messages[0].findAll('span', {'class': 'status-detail'})
            print message[0].text
            time = messages[0].findAll('span', {'class': 'pulish-time'})
            print time[0].text

            file = open("../paocaomessage", "w")
            file.write(message[0].text)
            file.close()
        except:
            pass

        #connect = getConnection()
        #cursor = connect.cursor()
        #cursor.execute("insert into tyx_messages (message) values ('%s')" % str(message[0].text))
        #connect.commit()
        #cursor.close()
        #connect.close()

def getMessageNew():
    bot = RenRen()
    tyxpage = bot.getTyxPage()
    soup = BeautifulSoup(tyxpage)
    messages = soup.findAll('div', {'class': 'page-status'})
    message = messages[0].findAll('span', {'class': 'status-content'})
    finalMessage = message[0].text

    link = re.compile("\(.*?\)")
    info = re.sub(link, '', finalMessage)
    info = info.replace("&amp", "")
    print info
    file = open("../paocaomessage", "w")
    file.write(info)
    file.close()

if __name__ == '__main__':
    while True:
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        hour = time.strftime('%H',time.localtime(time.time()))
        minute = time.strftime('%M',time.localtime(time.time()))
        print int(hour)
        print int(minute)
        if int(hour) == 6 and int(minute) == 30:
            #getMessage()
            getMessageNew()
        else:
            pass
        if int(hour) == 6 and int(minute) == 25:
            #getMessage()
            getMessageNew()
        else:
            pass
        time.sleep(30)
