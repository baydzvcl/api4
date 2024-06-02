
import os
import time
import requests
import pystyle
import random
import sys
from pystyle import *

def sendRequest(s): 
    try: 
        return requests.get(s).content
    except Exception:
        pass

def saveFile(f,w):
    try:
        f.write(sendRequest(w))
    except Exception:
        pass 

os.system('clear')
os.system('mode con: cols=120 lines=50')

banner = '''
 Get Proxies List Api                          
'''
print(Colorate.Horizontal(Colors.purple_to_red, Center.XCenter(banner)))

http = open('http.txt','wb')

# HTTP Proxies Sources
http_ = ["https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt","https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all","https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt","https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt","https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt","https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt","https://www.proxy-list.download/api/v1/get?type=http","https://www.proxy-list.download/api/v1/get?type=https","https://www.proxyscan.io/download?type=http","https://www.proxyscan.io/download?type=https","https://api.openproxylist.xyz/http.txt","https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt","https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt","https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all","https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt","https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt"]

for h in http_:
    saveFile(http, h)

Write.Print("[!] Successfully Scraped And Saved HTTP Proxies!\n", Colors.white_to_red, interval=0)
time.sleep(1)


# Closing Files
http.close()

# Done!
time.sleep(1)
Write.Print("Press any key to continue . . .", Colors.white_to_red, interval=0)
input()