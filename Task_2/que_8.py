
#8.	Write a program that accepts a string as an input from the user and calculate the number of digits and letters. 
#Sample input: consul72 
#Expected output: Letters 6 Digits 

que_8= input("Enter your string input with characters of digits and letters:")
l=0
d=0
for i in que_8:
    if i.isdigit(): d+=1
    elif i.isalpha(): l+=1
    else: pass
print("Letters", l," Digits", d) 