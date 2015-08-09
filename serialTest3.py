_author__ = 'Dylan'

from time import sleep
import serial
import sys
import glob
import time
import socket
import threading

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

test = serial_ports()

print(test)

ser = serial.Serial(serial_ports()[0], 115200)
#ser = serial.Serial('COM5', 115200)

print(ser)

sleep(5)

ip = open("ip.info", "r")

TCP_IP = ip.readline()

ip.close()

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
        try:
            line = ser.readline().decode('utf-8')
            #print(line)
            s.send(str(line).encode())
        except serial.SerialException as e:
            return

th1 = threading.Thread(target=mainThread)
th1.start()

th2 = threading.Thread(target=receiveThread)
th2.start()

th1.join()
th2.join()

s.close()
