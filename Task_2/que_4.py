
#4.	Write a program in Python to break and continue if the following cases occurs:
#    If user enters a negative number just break the loop and print “It’s Over” 
#    If user enters a positive number just continue in the loop and print “Good Going”

que_4 = int(input("enter any positive or negative number:"))
if que_4<0:
    print("It’s Over")
elif que_4>0:
    print("Good Going")
else:
    print("Sorry, try again and enter positive or negative number.")
