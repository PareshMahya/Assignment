#
# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
#

usr_ip = input("Enter your string :")
ans = [i for i in usr_ip if i.isupper()]
print(ans)