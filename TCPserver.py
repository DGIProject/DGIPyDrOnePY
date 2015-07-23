import socket
import string
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.95.33', 5005)
print('starting up server')
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

lastCommand = "waiting"

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from ' + str(client_address))

        #target = open('data/command.file', 'w')

        #target.seek(0)
        #target.write("waiting")
        #target.truncate()

        # Receive the data in small chunks and retransmit it
        while True:
            print("Test")
            data = connection.recv(1024)

            print('received data ', data)

            if data:
                print('sending data back to the client')

                command = data.decode()
                commandSplit = command.split()

                print(commandSplit)

                if commandSplit[0] == 'C':
                    print("update command")
                    lastCommand = command

                    #target.seek(0)
                    #target.write(command)
                    #target.truncate()

                connection.sendall(lastCommand.encode())
            else:
                print('no more data from ' + str(client_address))

                break

    finally:
        # Clean up the connection
        connection.close()