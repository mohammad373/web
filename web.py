# web
import socket
import sys
import time
from colorama import Fore
def __name__():
        try:
            print(Fore.GREEN + "\n\nHello . Welcome Back ;)\n")
            time.sleep(3)
            site = input(Fore.BLUE + "Enter Your Address WebSite ==> ")
            if site == "":
                try:
                    print(Fore.GREEN + "You Are 5 Sec Go To The Mano ;)")
                    time.sleep(5)
                    sys.exit()
                except:
                    pass
            my_socket = socket.gethostbyname(str(site))
            print(Fore.GREEN + "Ip Web Site ==> "+ Fore.RED + my_socket)

        except:
                pass
__name__()

print(Fore.BLUE+ "\n_______________________________________\n")

#_________________________________________________________________________________________________-
import sys
import time
import socket
from colorama import Fore
def __1__():
    try:
        site1 = input(Fore.GREEN + "Enter Your Address WebSite ==> ")
        my_list = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
        for i in my_list:
                host = str(i) + "." + str(site1)
                bypass = socket.gethostbyname(str(host))
                print(Fore.YELLOW +"Your Ip ==> "+Fore.GREEN +str(bypass) +Fore.RED +" | "   + Fore.GREEN + str(host) )

    except:
        pass
__1__()

print("________________________________________________________________")
#___________________________________________________________________________



from colorama import Fore
import sys
import requests
import time
import os

time.sleep(2)

def __2__():
    try:
        print(Fore.BLUE + "\nHello . Welcome Back\nThis Is Doman One ;))\n")
        site2 = input("Enter Your Address WebSite ==>  ")
        if site2 == "":
            try:
                print("Error : This Is Not Found ;(")
                time.sleep(1)
                os.system("clear")
                sys.exit()
            except:
                pass
        info = requests.get(str(site))
        for item in info:
            value = ""
            for var in info[str(i)]:
                item = item.replace("-" , " ")
                item = item.title()
                value += var
                print(item + " : " + value)
    except:
        pass
__2__()




