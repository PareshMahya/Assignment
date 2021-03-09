#
#  2.	Write a program in Python to allow the user to open a file by using the argv module.
#       If the entered name is incorrect throw an exception and ask them to enter the name again. 
#       Make sure to use read only mode.
#

# while True:
#     # try:
#         usr_ip = input("Enter the file name of Que_1.py :")
#         if usr_ip !="Que_1.py":
#             raise input("Enter the file name of Que_1.py :")
#             # with open("Que_1.py") as f:
#             #     f.read()
#             #     f.close()
#             #     break
#     # except(FileNotFoundError):
#     #     print("Sorry, Incorrect file name")
#     #     usr_ip = input("Please, enter the file name of Que_1.py :")

try:
    usr_ip = input("Enter the file name of Que_1.py :")
    f = open(, "r")
except FileNotFoundError:
    print("The file doesn't exist")