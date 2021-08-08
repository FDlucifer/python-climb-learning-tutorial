# Python-Ransomware

To test the Ransomware out on your machine,

* edit lines 49 and 140 in the ransomware.py file with your own absolute paths etc for testing purposes and so you can use the localRoot folder

* [ATTACKER] Run the RSA script to generate two keys, a private and public key

* [TARGET] Run the ransomware script - localRoot .txt files will be encrypted now

* [ATTACKER] Run the fernet key decryption file to decrypt the EMAIL_ME.txt(be on your desktop) file, this will give you a PUT_ME_ON_DESKtOP.txt file, once you put this on the desktop the ransomware will decrypt the localRoot files in that directory

 - Note: the localRoot directory is a local test example samples file

### Created with
* Python 3.7 - https://www.python.org/

#### Disclaimer

> This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for
> illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no
> liability and are not responsible for any misuse or damage caused by this tool and software in general.

#Python#Ransomware#Malware