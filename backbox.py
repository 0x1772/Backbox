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

def print_banner():
    banner = """\
        
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

by 0x1772.

type <help> for usage information!\n\n"""
    for line in banner:
        term.output(text.blue(line)) 



def function(Optiox):
    if Optiox == '1':
        os.system('python2 vulscanner.py')
    elif Optiox == '2':
        os.system('python2 ipchanger.py')
    else:
        print("Please type an available function")

function(input('Choose Option:'))

print_banner()
