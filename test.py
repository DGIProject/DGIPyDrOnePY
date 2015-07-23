import re

__author__ = 'Dylan'

with open("data/command.file", "r") as ins:
        array = []

        for line in ins:
            array.append(line)

lineCommand = list(array[0])
command = ''

for list in lineCommand:
    if [i for i, val in enumerate(['p', 'o', 'w', 'e', 'r', ' ', '-', 'a', '0', 'l', '1', '2', '3', '4', '5', '6', '7', '8', '9']) if list in val]:
        command += list

print(command)