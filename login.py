import signal,pdb
import os
import time
from sys import argv
from urllib import parse, request

BASE_URL = "http://172.16.68.6:8090/"


def loggedin(user):
    url = "http://172.16.68.6:8090/live?" + "mode=192&username=" + str(user)
    res = request.urlopen(url).read()
    if "<ack><![CDATA[ack]]></ack>" in str(res):
        return True
    else:
        return False


def send_request(request_type, *arg):
    if request_type == 'login':
        params = parse.urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
        url = BASE_URL+"login.xml"
    elif request_type == 'logout':
        print("Initiating logout request..")
        params = parse.urlencode({'mode': 193, 'username': arg[0]})
        url = BASE_URL + "logout.xml"
        pdb.set_trace()
        print (response)
    response = request.urlopen(url,params.encode('utf-8'))
    return str(response.read())


def login(filename):
    i = 0
    users=open("passwords/"+filename, "r")
    user = users.readline()
    flag = False
    while user is not '':
        user=user[:-1]
        res =send_request("login", user, filename[:-4])
        if "<message><![CDATA[You have successfully logged into JIIT Internet Server.]]></message>" in res:
            string = "Logged in using " + user
            os.system('notify-send ' + '"' + string + '"')
            flag= True
        while flag:
            time.sleep(20)
            if not loggedin(user):
                res=send_request("login", user, filename[:-4])
                if "<message><![CDATA[You have successfully logged into JIIT Internet Server.]]></message>" not in res:
                    flag= False
        user=users.readline()
        if user == '':
            print ("End of file, restarting")
            users.seek(0,0)
            user= users.readline()

if __name__ == "__main__":
    if "login" in argv:
        try:
            login(argv[2])
        except KeyboardInterrupt:
            res = send_request("logout", argv)
            if "logged off" in res:
                string= "Logged out of Cyberroam"
                os.system('notify-send ' + '"' + string + '"')
                print("Logout Request completed")    
    elif "logout" in argv:
        res = send_request("logout", argv)
        if "logged off" in res:
            string= "Logged out of Cyberroam"
            os.system('notify-send ' + '"' + string + '"')
            print("Logout Request completed")
    else:
        print("prob")
        print(argv)
__author__ = 'gaurav'
