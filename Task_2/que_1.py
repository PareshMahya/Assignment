
#1.	Write a program in Python to perform the following operation:
#    • If a number is divisible by 3 it should print “Consultadd” as a string,
#    • If a number is divisible by 5 it should print “Python Training” as a string,
#    • If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.

que_1= eval(input("Enter your number:"))
print("Your entered value is ", que_1)
if que_1%3==0 and que_1%5==0: print("Consultadd - Python Training")
elif que_1==0: print("Consultadd")
elif que_1%5==0: print("Python Training")
else: print("Sorry, you need to know prepose of this program before enter any number.")
