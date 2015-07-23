from time import sleep
import serial
import sys
import time

ser = serial.Serial('COM5', 9600)
returnSerial = open('data/returnSerial.file', 'w')

print(ser)

sleep(1)

lastLine = ""

while 1:
    with open("data/command.file", "r") as ins:
        array = []

        for line in ins:
            array.append(line)

        mot = array[0] + "\r"
        ser.write(mot.encode())

    line = ser.readline().decode()

    print(line)

    if line != lastLine:
        print("different")
        returnSerial.seek(0)
        returnSerial.write(line)
        #returnSerial.write("test")
        returnSerial.truncate()
        lastLine = line

    sleep(0.2)

returnSerial.close()