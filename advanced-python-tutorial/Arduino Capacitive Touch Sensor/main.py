# pip install pyserial
import serial
import time

ser = serial.Serial('COM3', 9800, timeout=1)
time.sleep(2)

for i in range(30):
    line = ser.readline().decode("utf-8")
    if line == "":
        print("no touch")
    else:
        print("touched")

ser.close()