from ast import If
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
    else:
        print("Please type an available function")

##if_statement(input('Choose Option:'))
def statement_if(local_state):
    if local_state == '1':
        local_a()
    elif local_state == '2':
        local_b()
    else:
        print("Please type an available local_statement")
        print("ERROR404")

def local_b()
    print("Do yo want to change your ip before Vulnerability Scan?(Recommended=> YES)"),
    print("Please type yes or no")
    if db_1 == "1"




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


# util functions 

