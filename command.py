__author__ = 'Dylan'

sleep = False

def analyseCommand(command):
    splitCommands = command.split()

    if len(splitCommands) <= 0:
        return '-CONSOLE- no command'
    else:
        if splitCommands[0] == 'ping':
            return '-CONSOLE- pong'
        elif splitCommands[0] == 'power':
            if len(splitCommands) >= 3:
                if splitCommands[1] == '-all':
                    return '-CONSOLE- all motors at ' + splitCommands[2]
                elif splitCommands[1] == '-front':
                    return '-CONSOLE- front motor at ' + splitCommands[2]
                elif splitCommands[1] == '-back':
                    return '-CONSOLE- back motor at ' + splitCommands[2]
                elif splitCommands[1] == '-left':
                    return '-CONSOLE- left motor at ' + splitCommands[2]
                elif splitCommands[1] == '-right':
                    return '-CONSOLE- right motor at ' + splitCommands[2]
                else:
                    return '-CONSOLE- error command : power -[all,front,bottom,left,right] [power in %]'
            else:
                return '-CONSOLE- error command : power -[all,front,bottom,left,right] [power in %]'
        elif splitCommands[0] == 'turn':
            if len(splitCommands) >= 3:
                if splitCommands[1] == '-left':
                    return '-CONSOLE- turn left at ' + splitCommands[2]
                elif splitCommands[1] == '-right':
                    return '-CONSOLE- turn right at ' + splitCommands[2]
                elif splitCommands[1] == '-front':
                    return '-CONSOLE- turn front at ' + splitCommands[2]
                elif splitCommands[1] == '-back':
                    return '-CONSOLE- turn back at ' + splitCommands[2]
                else:
                    return '-CONSOLE- error command : turn -[left, right] [degrees]'
            else:
                return '-CONSOLE- error command : turn -[left, right] [degrees]'
        elif splitCommands[0] == 'rotate':
            if len(splitCommands) >= 3:
                if splitCommands[1] == '-left':
                    return '-CONSOLE- left rotate at ' + splitCommands[2]
                elif splitCommands[1] == '-right':
                    return '-CONSOLE- right rotate at ' + splitCommands[2]
                else:
                    return '-CONSOLE- error command : rotate -[left,right] [degrees]'
            else:
                return '-CONSOLE- error command : rotate -[left,right] [degrees]'
        elif splitCommands[0] == 'sleep':
            return '-CONSOLE- sleeping'
        else:
            return '-CONSOLE- command not found'
    
while True:
    command = input('Enter command :')
    
    print(analyseCommand(command))

    if sleep:
        print()