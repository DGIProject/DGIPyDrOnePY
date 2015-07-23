import os
import subprocess
from time import sleep

__author__ = 'Dylan'

lastCommand = ''

#os.system("file.py")

currentMode = 0 #0 : manual, 1 : autopilot, 2 : sleep

#proc1 = subprocess.Popen(['python', 'file.py'])
#proc2 = subprocess.Popen(['python', 'TCPserver.py'])

while True:
    sleep(1)

    with open("data/gyro.file", "r") as ins:
        arrayGyro = []

        for line in ins:
            arrayGyro.append(line)

        print("x:" + arrayGyro[0] + ',y:' + arrayGyro[1] + ' ,z:' + arrayGyro[2])

    with open("data/command.file", "r") as ins:
        array = []

        for line in ins:
            array.append(line)

    if array[0] != lastCommand:
        lastCommand = array[0]

        print(array[0])

        lineCommand = ''
        lineCommand = list(str(array[0]))

        command = 'ok'

        for list in lineCommand:
            #if [i for i, val in enumerate(['p', 'o', 'w', 'e', 'r', ' ', '-', 'a', '0', 'l', '1', '2', '3', '4', '5', '6', '7', '8', '9']) if list in val]:
                #command += list
            print('test')

        print(command)

        if len(array) > 0:
            commands = command.split()

            print('command[0]: ' + commands[0])

            if currentMode == 2:
                print('sleeping ...')

                if commands[0] == 'nospeed':
                    print('sleep now')
                    #cut motors
            else:
                if commands[0] == 'ping':
                    print('-CONSOLE- pong')
                elif commands[0] == 'power':
                    if len(commands) >= 3:
                        if commands[1] == '-all':
                            print('-CONSOLE- all motors at ' + commands[2])
                        elif commands[1] == '-front':
                            print('-CONSOLE- front motor at ' + commands[2])
                        elif commands[1] == '-back':
                            print('-CONSOLE- back motor at ' + commands[2])
                        elif commands[1] == '-left':
                            print('-CONSOLE- left motor at ' + commands[2])
                        elif commands[1] == '-right':
                            print('-CONSOLE- right motor at ' + commands[2])
                        else:
                            print('-CONSOLE- error command : power -[all,front,bottom,left,right] [power in %]')
                    else:
                        print('-CONSOLE- error command : power -[all,front,bottom,left,right] [power in %]')
                elif commands[0] == 'turn':
                    if len(commands) >= 3:
                        if commands[1] == '-left':
                            print('-CONSOLE- turn left at ' + commands[2])
                        elif commands[1] == '-right':
                            print('-CONSOLE- turn right at ' + commands[2])
                        elif commands[1] == '-front':
                            print('-CONSOLE- turn front at ' + commands[2])
                        elif commands[1] == '-back':
                            print('-CONSOLE- turn back at ' + commands[2])
                        else:
                            print('-CONSOLE- error command : turn -[left, right] [degrees]')
                    else:
                        print('-CONSOLE- error command : turn -[left, right] [degrees]')
                elif commands[0] == 'rotate':
                    if len(commands) >= 3:
                        if commands[1] == '-left':
                            print('-CONSOLE- left rotate at ' + commands[2])
                        elif commands[1] == '-right':
                            print('-CONSOLE- right rotate at ' + commands[2])
                        else:
                            print('-CONSOLE- error command : rotate -[left,right] [degrees]')
                    else:
                        print('-CONSOLE- error command : rotate -[left,right] [degrees]')
                elif commands[0] == 'sleep':
                    print('-CONSOLE- sleeping')
                else:
                    print('-CONSOLE- command not found')