__author__ = 'Dylan'

from socket import *
import threading

ip = open("ip.info", "r")

host = ip.readline()

ip.close()

port = 5005

#Creating socket object
sockServer = socket()
#Binding socket to a address. bind() takes tuple of host and port.
sockServer.bind((host, port))
#Listening at the address
sockServer.listen(5) #5 denotes the number of clients can queue

lastCommand = "P 0|0|0|0|0"
lastProperties = "D 0|0|0|0|0|0|0|0|0|12|0|0|0"

def clientthread(connection):
    global lastProperties
    global lastCommand

    while True:
        data = connection.recv(1024)

        command = data.decode()
        commandSplit = command.split()

        if len(commandSplit) > 0:
            print(commandSplit)

            if commandSplit[0] == "C":
                print("CONTROLLER")

                lastCommand = commandSplit[1] + " " + commandSplit[2] + " " + commandSplit[3]

                print("lastCommand", lastCommand)

                connection.send(lastProperties.encode())
            elif commandSplit[0] == "D":
                print("DRONE")

                if commandSplit[1] != "SEND":
                    lastProperties = commandSplit[1] + " " + commandSplit[2]

                    connection.send(lastCommand.encode())
            else:
                print("NOT FOUND")

while True:
    print("new connection")

    connection, clientAddress = sockServer.accept()

    th1 = threading.Thread(target=clientthread, args=[connection])
    th1.start()

sockServer.close()
