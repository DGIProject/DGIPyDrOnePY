__author__ = 'Dylan'

from time import sleep
import serial
import sys
import time
import socket
import threading

ser = serial.Serial('COM5', 9600)

TCP_IP = '192.168.95.33'
TCP_PORT = 5005

print(ser)

sleep(5)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#s.send("A 1|1|1|1".encode())

def mainThread():
    lastCommand = ""
    i = 0

    while True:
        #data = s.recv(1024)

        #print("Receive data : ", data.decode())

        command = "LED ON\r"

        if command != lastCommand:
            print("sendCommand")

            lastCommand = command

            #print(command)
            ser.write(command.encode())

        #i = i + 1

        #print(i)

        #line = ser.readline().decode()

        #print(line)

        #s.send(str("A test").encode())

    #s.close()

def receiveThread():
    print("receiveThread")
    while True:
        line = ser.readline().decode()

        print(line)

        #s.send(str("A " + line).encode())

th1 = threading.Thread(target=mainThread)
th1.start()

th2 = threading.Thread(target=receiveThread)
th2.start()

th1.join()
th2.join()