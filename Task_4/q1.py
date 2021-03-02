# 1. Write a program to reverse a string.
#       Sample input: “1234abcd” 
#       Expected output: “dcba4321”

q1 = "1234abcd" 
# print(type(q1))
q1_a = q1[-1:-(len(q1)+1):-1]
print(q1_a)
# print(type(q1_a))

