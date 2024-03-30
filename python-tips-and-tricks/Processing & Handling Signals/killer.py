import os
import signal

pid = input("Enter PID:")
os.kill(int(pid), signal.SIGUSR1)