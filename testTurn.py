__author__ = 'Dylan'

pMotor1 = 0
pMotor2 = 0
pMotor3 = 0
pMotor4 = 0

while True:
    command = input('command=')

    commandSplit = command.split()

    xPower = round((int(commandSplit[1]) / 45) * 10, 1)
    yPower = round((int(commandSplit[2]) / 45) * 10, 1)

    print(xPower, yPower)

    if xPower > 0:
        pMotor1 = pMotor1 - 2
        pMotor3 = pMotor3 - 2

    if yPower < 0:
        pMotor2 = pMotor2 - 2
        pMotor4 = pMotor4 - 2