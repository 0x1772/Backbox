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
from turtle import home
from unittest import result
from wsgiref import simple_server 

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
        return home
    else:
        print("Port is open. Everything looks fine...")
        os.system("sudo chmod +x core/ip_tracer")
        os.system("sudo ./ip_tracer")
        return home,
          
from string import ascii_letters

def get_name():
    name = input("What is your name?\n: ").strip().title()

    while not all(letter in ascii_letters + " -" for letter in name):
        name = input("Please enter a valid name.\n: ").strip().title()

    return name


def get_name():
    name = input("What is your name?\n: ").strip().title()

    while not (name.replace("-", "") and
               name.replace("-", "").replace(" ", "").isalpha()):
        name = input("Please enter a valid name.\n: ").strip().title()

    return name


name = get_name().title()

print("You said your name was " + name + ".)



###hashcode
def hash_cracker_installation():
    hashcode1 = input("Please enter your hash for bruteforce")
    os.system("go mod init hashcracker")
    os.system("go build -o hashcracker")
    os.system("make install")
    os.system("./hashcracker -hash", hashcode1)

### spotify installer code
def spotift_installer():
    os.system("sudo apt install git")
    os.system("git clone https://github.com/0x1772/SpotifyAccCreator/")
    os.system("cd SpotifyAccCreator")
    os.system("sudo python2 creator.py")
    
catch_ip() {
touch sites/$server/saved.usernames.txt
ip=$(grep -a 'IP:' sites/$server/ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
ua=$(grep 'User-Agent:' sites/$server/ip.txt | cut -d '"' -f2)
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Victim IP:\e[0m\e[1;77m %s\e[0m\n" $ip
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] User-Agent:\e[0m\e[1;77m %s\e[0m\n" $ua
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Saved:\e[0m\e[1;77m %s/saved.ip.txt\e[0m\n" $se>cat sites/$server/ip.txt >> sites/$server/saved.ip.txt


if [[ -e iptracker.log ]]; then
rm -rf iptracker.log
fi