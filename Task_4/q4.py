# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

temp_q4 = input("Enter anything in a hyphen-separated sequence: ")
s="-"
# print (temp_q4)
# print(type(temp_q4))
q4= temp_q4.split(s)
# print(type(q4)) 
# print(q4)
ans = sorted(q4)
#print(ans)
print(s.join(ans))

