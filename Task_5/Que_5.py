#
# 5. Go through the link provided below to understand finally and raise concept: https://www.programiz.com/python-programming/exception-handling
#
# 

try:
    usr_ip = int(input("Enter four digits number :"))
    ip = str(usr_ip)
    if len(ip)!=4:
        raise ValueError ("Worng Number of Digit")
    else: 
        print("Number of digit are good")
except ValueError:
     print("The length is too short/long !!!")
finally:
    print("Now, you are at the end program!")


