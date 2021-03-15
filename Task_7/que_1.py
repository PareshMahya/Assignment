# 1. Write a program that calculates and prints the value according to the given formula:
    # Q= Square root of [(2*C*D)/H]
    # Following are the fixed values of C and H:
    # C is 50. 
    # H is 30.
    # D is a variable whose values should be input to your program in a comma-separated sequence. 

import math
usr_ip = input("Enter the comma-separated sequence number for variavle D: ")
#print(type(usr_ip))
usr_ip_list = usr_ip.split(',')
#print(type(usr_ip_list))
print("value of comma-separated sequence D :", usr_ip_list)
ans_list = []
for D in usr_ip_list:
    Q = round(math.sqrt(2 * 50 * eval(D) / 30),2)
    ans_list.append(Q)
print(ans_list)