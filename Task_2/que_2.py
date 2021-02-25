
#2.	Write a program in Python to perform the following operator based task:
#    a.	Ask user to choose the following option first:
#       i.	If User Enter 1 - Addition 
#       ii.	If User Enter 2 - Subtraction 
#       iii.If User Enter 3 - Division 
#       iv.	If User Enter 4 - Multiplication 
#       v.	If User Enter 5 - Average 
#   b.	Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above. 
#   c.	Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5. 
#   d.	At the end if the answer of any operation is Negative print a statement saying “NEGATIVE” 
#   e.	NOTE: At a time a user can only perform one action

print(
    """choose the following option first:
    Enter 1 - Addition 
    Enter 2 - Subtraction 
    Enter 3 - Division
    Enter 4 - Multiplication
    Enter 5 - Average 
    """)
que_2 = int(input("Choose number between 1 - 5 option for Arithmetic Operation:")) 
num1 = eval(input("Enter first numbers for Arithmetic Operation: "))
num2 = eval(input("Enter Second numbers for Arithmetic Operation: "))

ans = 0
if que_2==1:
    ans= num1+num2
    print("Your Addition operation answer is ", ans)
elif que_2==2:
    ans= num1 - num2
    print("Your Subtraction operation answer is ", ans)
elif que_2==3:
    ans= num1/num2
    print("Your Division operation answer is ", ans)    
elif que_2==4:
    ans = num1*num2
    print("Your Multiplication operation answer is ", ans)
elif que_2==5:
    num3=eval(input("Enter first numbers for Average Operatio: "))
    num4=eval(input("Enter Second numbers for Average Operatio: "))
    ans = (num1+num2+num3+num4)/4
    print("Your Average Operatio answer is ", ans)

if ans<0:
    print("And your answer value is NEGATIVE")