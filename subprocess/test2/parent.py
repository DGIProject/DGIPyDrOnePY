__author__ = 'Dylan'

from subprocess import Popen, PIPE

prog = Popen("child.py", shell=True, stdin=PIPE, stdout=PIPE)

prog.stdin.write("This will go to script A\n")
print(prog.stdout.read())

prog.wait() # Wait for scriptA to finish