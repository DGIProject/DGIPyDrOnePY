__author__ = 'Dylan'

from time import sleep
import serial
import sys
import time
import socket
import threading

#ser = serial.Serial('/dev/ttyACM0', 115200)
ser = serial.Serial('COM5', 115200)

print(ser)

sleep(5)

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def mainThread():
    lastCommand = ""
    i = 0

    while True:
        data = s.recv(1024)

        #print("data")

        command = data.decode() + "\r"

        print('command', command)

        #if command != lastCommand:
            #print("sendCommand")

            #lastCommand = command

        ser.write(command.encode())

        #i = i + 1

        #print(i)

        s.send(str("D SEND").encode())
    #s.close()

def receiveThread():
    print("receiveThread")
    while True:
        line = ser.readline().decode()

        #print(line)

        s.send(str(line).encode())

th1 = threading.Thread(target=mainThread)
th1.start()

th2 = threading.Thread(target=receiveThread)
th2.start()

th1.join()
th2.join()

s.close()