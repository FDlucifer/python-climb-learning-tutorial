import psutil
import datetime as dt


def log_ram_usage():
    with open("log_ram.txt", "a+") as f:
        f.write(f"ram usage {dt.datetime.now()}: {psutil.virtual_memory().percent}%\n")


def log_cpu_usage():
    with open("log_cpu.txt", "a+") as f:
        f.write(f"cpu usage {dt.datetime.now()}: {psutil.cpu_percent()}%\n")


def print_message(message):
    print("message:", message)
