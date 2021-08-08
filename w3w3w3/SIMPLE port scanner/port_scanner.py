'''Port scanner FOR ports ending in 000 eg, 1000,2000,3000 etc - 
untill find hidden service port'''


'''imports'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)


#port = 1000
for portx in range(1, 1000):
    try:
        s.connect(('127.0.0.1', portx))
        r = s.recv(1024)
        if 'Congratulations' in r.decode('utf8'):
            print('[!] HIDDEN SERVICE FOUND: %s ~ %s' % (portx, r.decode('utf8')))
            s.close()
            break
        else:
            print('%s ~ %s' % (portx, r.decode('utf8')))
            s.close()
    except socket.error as err:
        print('%s ~ %s' % (portx, err))

    #port += 1000
