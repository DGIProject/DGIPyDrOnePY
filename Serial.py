from time import sleep
import serial
import sys
import time
from threading import Thread

class ReadingThread(Thread):

    def __init__(self, ser):
        Thread.__init__(self)
        self.ser = ser

    def run(self):
        while 1:
            print(self.ser.readline())

def main():
    ser = serial.Serial('COM5', 9600)
    #readT = ReadingThread(ser)
    #readT.start()

    print(ser)
    time.sleep(3)
    while 1:
        mot=input('Cmd ?')
        mot+="\r"
        ser.write(mot.encode())

main()
