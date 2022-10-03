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

def print_banner(self, moduleText=None):
        print("""
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
    """);

        if (moduleText):
            print("MODULE\n" + str(moduleText))

        print('\n\n\n') 


def function(Optiox):
    if Optiox == '1':
        os.system('python2 vulscanner.py')
    elif Optiox == '2':
        os.system('python2 ipchanger.py')
    else:
        print("Please type an available function")

##function(input('Choose Option:'))

print_banner()