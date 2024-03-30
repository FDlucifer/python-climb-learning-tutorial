'''imports'''
import zipfile

count = 1

with open('darkweb2017-top10000.txt','rb') as text: # here you can change your dict
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('test.zip','r') as zf: # here you can change the zip file you want to crack
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            #print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass