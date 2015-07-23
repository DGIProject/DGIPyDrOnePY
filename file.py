from random import randint
from time import sleep

__author__ = 'Dylan'

print('ok')

sleep(5)

target = open('data/gyro.file', 'w')

while True:
    value1 = str(randint(2,9))
    value2 = str(randint(2,9))
    value3 = str(randint(2,9))

    print(value1, value2, value3)

    target.seek(0)

    target.write(value1)
    target.write("\n")
    target.write(value2)
    target.write("\n")
    target.write(value3)

    target.truncate()

    sleep(1)

target.close()



