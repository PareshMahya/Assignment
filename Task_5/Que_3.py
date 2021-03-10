#
#3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
#

try:
    usr_ip = int(input("Enter four digits number :"))
    ip = str(usr_ip)
    if len(ip)!=4:
        raise ValueError ("Worng Number of Digit")
except ValueError:
     print("The length is too short/long !!!")