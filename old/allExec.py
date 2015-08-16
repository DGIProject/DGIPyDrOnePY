__author__ = 'Dylan'

import threading
import os

def tcpServer():
    os.system("TCPserver3.py")

def serialArduino():
    os.system("serialTest3.py")

th1 = threading.Thread(target=tcpServer)
th1.start()

th2 = threading.Thread(target=serialArduino)
th2.start()