
#6.	What is the output of the following code examples?
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else: 
        print("error")
"""
Here i = 0, and in the next line, it will enter in while loop until "i" is less than 5, 
the first line of the while loop will print the "i" value. It will pass through the increment statement, and it will give you another "i". 
finally, it will pass through if-else statement; whenever if conditions(i==3) satisfy, it will stop the program due to "break" unless it will print "error ". 
So, in this program, after printing i=2 increment "i" value and new "i" value is 3 and it will satisfy "if" condition 
so the program will stop rest of operation.
"""
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

"""
Here count=0, then in the next line, it enters while loop with condition true.
Inside while loop first it will print the count value, then it will pass through increment. 
And lastly, the count value passes through if statement. if condition ("count" is greater than 5) is satisfied, then it will execute break statement and stop the rest of the program.
Note here Given keyword is "Break", it supposes to be a "break"; otherwise, it will give an error that "NameError: name 'Break' is not defined"
"""
x = 123
for i in x:
    print(i)
"""
This code assign x value is 123, then pass through for loop. So, the x value is not changeable; 
that's why it will give an error "TypeError: 'int' object is not iterable"
for loop condition should be some range, not a signal value.
"""