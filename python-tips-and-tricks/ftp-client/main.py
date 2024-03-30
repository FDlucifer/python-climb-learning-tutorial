from ftplib import FTP

host = "test"
user = "test"
password = "test"

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

'''
# download files
    with open('test.txt', 'wb') as f:
        ftp.retrbinary("retr " + "mytest.txt", f.write, 1024)

# upload files
    with open('myupload.txt', 'rb') as f:
        ftp.storbinary("stor " + "upload.txt", f)
'''

# ftp command
    ftp.cwd("mydir")

    with open('myspecialfile.txt', 'wb') as f:
        ftp.retrbinary("retr " + "otherfile.txt", f.write, 1024)

    ftp.quit()