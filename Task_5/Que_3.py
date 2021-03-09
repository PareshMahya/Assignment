#
#3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
#

try:
    usr_ip = input("Enter four digits number :")
    while len(usr_ip)==4:
        print("Perfect")
except:
    print("hello")