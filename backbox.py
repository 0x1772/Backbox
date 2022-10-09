from ast import If
from platform import system
from sqlite3 import connect
import sys
import socket
import subprocess
import os
import time
import signal
import random
import string
import threading
import re
from unittest import result 

##banner function for Backbox
def print_banner(ver, exp_cnt):
    """
    print banner along with some info
    """
    banner = colors.CYAN + colors.BOLD + r'''
 ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄▄    ▒█████  ▒██   ██▒
▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█████▄ ▒██▒  ██▒▒▒ █ █ ▒░
▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒ ▄██▒██░  ██▒░░  █   ░
▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░█▀  ▒██   ██░ ░ █ █ ▒ 
░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█  ▀█▓░ ████▓▒░▒██▒ ▒██▒
░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓███▀▒░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░▒░▒   ░   ░ ▒ ▒░ ░░   ░▒ ░
 ░    ░   ░   ▒   ░        ░ ░░ ░  ░    ░ ░ ░ ░ ▒   ░    ░  
 ░            ░  ░░ ░      ░  ░    ░          ░ ░   ░    ░  
      ░           ░                     ░                   

by 0x1772
'''+f'''

    version: {ver}

    {exp_cnt} exploits
''' + colors.END + colors.GREEN + '''

    by jm33_m0
    https://github.com/jm33-m0/mec
    type h or help for help\n''' + colors.END

    print(banner)


##function(input('Choose Option:'))
def function(Optiox):
    if Optiox == '1':
        print("Do yo want to change your ip before Vulnerability Scan?(Recommended=> YES)")
        print("please type yes or no")
        if IpOpt == "yes"
            os.system('sudo python2 ipchanger.py')
        elif IpOpt == "no"
            print("ip not changed...")
    elif Optiox == '2':
        os.system('python2 ipchanger.py') 
    elif Optiox == "3":
        ngrok_check_default()
    else:
        print("Please type an available function")
    

##if_statement(input('Choose Option:'))
def statement_if(local_state):
    if local_state == '1':
        local_a():
    elif local_state == '2':
        local_b():
    else:
        print("Please type an available local_statement")
        print("ERROR404")

def local_b():
    print("Do yo want to change your ip before Vulnerability Scan?(Recommended=> YES)"),
    print("Please type yes or no")
    if db_1 == "1":
        os.system('python2 ipchanger.py")
     elif db_1 == "2":
        os.system("sudo python2 vulnerabilityscanner.py"
    else:
        print("please type an function")

def ngrok_check():
    req = requests.get('http://127.0.0.1:4040/api/tunnels')
    soup = BeautifulSoup(req.text, 'lxml')
    tunnelsjson = json.loads(soup.find('p').text)
    url = tunnelsjson['tunnels'][0]['public_url']
    print(url)

def ngrok_check_default():
    sock = socket.socket(socket.AF.INET, socket.socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1',4000))
    print(result)
    if result == 0:
        print("Plase install ngrok or open port for app")
    else:
        print("Port is open. Everything looks fine...")
        os.system("sudo chmod +x core/ip_tracer")
        os.system("sudo ./ip_tracer")
        