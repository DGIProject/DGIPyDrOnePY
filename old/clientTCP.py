import socket
from time import sleep

ip = open("ip.info", "r")

TCP_IP = ip.readline()

ip.close()

port = 5005

TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for x in range(0, 5):
    s.send("C H Y 0".encode())

    #data = s.recv(BUFFER_SIZE)
    #print("received data:", data)
    sleep(1)

s.close()