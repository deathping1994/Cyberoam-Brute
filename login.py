import os
from sys import argv
from urllib import parse, request


BASE_URL = "http://172.16.68.6:8090/login.xml"


def send_request(request_type, *arg):
    if request_type == 'login':
        params = parse.urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
    elif request_type == 'logout':
        print("Initiating logout request..")
        params = parse.urlencode({'mode': 193, 'username': arg[0]})

    response = request.urlopen(BASE_URL, params.encode("ascii"))
    return str(response.read())


def login(filename):
    pid = os.fork()
    if pid != 0:
        fo = open("pid.txt", "w")
        fo.write(str(pid))
        fo.close()
        exit(0)
    flag = 0
    with open(filename, "r") as creds:
        while True:
            if flag == 0:
                cred = creds.readline()
                # user, passwd = cred.split(" ")
                user = cred
            res = send_request("login", user, "77uu88")
            if "successfully logged" in res:
                flag = 1
                # print("logged in using %s", user)
            else:
                flag = 0


if __name__ == "__main__":
    if "login" in argv:
        print(argv[2])
        login(argv[2])
    elif "logout" in argv:
        fo = open("pid.txt","r")
        pid = fo.readline()
        os.kill(int(pid), 9)
        res = send_request("logout", argv)
        if "logged off" in res:
            print("Logout Request completed")

__author__ = 'gaurav'
