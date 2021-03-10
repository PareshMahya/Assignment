#
#  2.	Write a program in Python to allow the user to open a file by using the argv module.
#       If the entered name is incorrect throw an exception and ask them to enter the name again. 
#       Make sure to use read only mode.
#

import sys
try:
    if sys.argv[1]=="test.txt":
        with open("test.txt")as f:
            f.read()
except FileNotFoundError:
        print("Entered file name is invalid, Please, enter the name again :")