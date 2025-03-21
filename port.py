import serial
import time

ser = serial.Serial('COM11', 9600, timeout=1)

time.sleep(2)

ser.write(b'11')

ser.close()
