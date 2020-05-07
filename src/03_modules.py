"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print(arg)

# Print out the OS platform you're using:
print(os.name)

# Print out the version of Python you're using:
print(f'{str(sys.version_info.major)}.{str(sys.version_info.minor)}.{str(sys.version_info.micro)}')


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'{os.getpgid(0)}')

# Print the current working directory (cwd):
print(f'{os.getcwd()}')

# Print out your machine's login name
print(os.getlogin())
