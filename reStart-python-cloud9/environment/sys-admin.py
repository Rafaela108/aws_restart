# Exercise 1: Using os.system
import os

# Run the Bash command ls using os.system()
os.system("ls")

# Exercise 2: Using subprocess.run
import subprocess

# Run the Bash command ls using subprocess.run()
subprocess.run(["ls"])

# Exercise 3: Using subprocess.run with two arguments
# Add the "-l" argument to ls
subprocess.run(["ls", "-l"])

# Exercise 4: Using subprocess.run with three arguments
# Specify a directory name (e.g., README.md)
subprocess.run(["ls", "-l", "README.md"])

# Exercise 5: Retrieving system information
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Exercise 6: Retrieving information about disk space
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])