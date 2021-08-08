# Python-TCP-Reverse-Shell
Python TCP reverse shell &amp; persistence &amp; exe &amp; more!

Persistence is gained when creating an exe using pyinstaller like
 
```
pyinstaller -w --onefile revShell_server.py
```

It will add the exe to the registry and will start up on machine startup and user login.