__author__ = 'Dylan'

from socket import *
import threading

host = '192.168.95.20'
port = 5005

#Creating socket object
sockServer = socket()
#Binding socket to a address. bind() takes tuple of host and port.
sockServer.bind((host, port))
#Listening at the address
sockServer.listen(5) #5 denotes the number of clients can queue

lastCommand = "waiting"
lastProperties = "0|0|0|0"

pMotor1 = 0
pMotor2 = 0
pMotor3 = 0
pMotor4 = 0

dApproach = 0

def clientthread(connection):
    while True:
        data = connection.recv(1024)

        command = data.decode()
        commandSplit = command.split()

        if len(commandSplit) > 0:
            #print(commandSplit)

            global lastCommand
            global lastProperties

            global pMotor1
            global pMotor2
            global pMotor3
            global pMotor4

            global dApproach

            if commandSplit[0] == "C":
                print("CONTROLLER")

                if commandSplit[1] == "LED":
                    print("led")

                    lastCommand = "LED " + commandSplit[2]
                elif commandSplit[1] == "TURN":
                    print("TURN")
                elif commandSplit[1] == "POWER":
                    print("POWER")

                    #Calculate power
                    #if commandSplit[3].isdigit():
                        #pMotor1 = int(commandSplit[3])
                        #pMotor2 = int(commandSplit[3])
                        #pMotor3 = int(commandSplit[3])
                        #pMotor4 = int(commandSplit[3])

                    lastCommand = "MOTOR " + commandSplit[2] + "-" + commandSplit[3] + "-" + commandSplit[4] + "-" + commandSplit[5]
                else:
                    print("UNDEFINED COMMAND")

                print("lastCommand : ", lastCommand)

                connection.send(lastProperties.encode())
            elif commandSplit[0] == "A":
                #print("ARDUINO")

                #properties = commandSplit[1].split('|')

                #dApproach = properties[0]

                if commandSplit[1] == 'TEST':
                    print('New properties')
                    lastProperties = 'PROPERTIES'

                connection.send(lastCommand.encode())
            else:
                print("NO TYPE")

while True:
    connection, clientAddress = sockServer.accept()

    th1 = threading.Thread(target=clientthread, args=[connection])
    th1.start()

sockServer.close()