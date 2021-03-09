#1.	Write a program in Python to allow the error of syntax to be handled using  exception handling.
#   HINT: Use SyntaxError 


try:
    ans = eval("Enter something :")
except SyntaxError:
    print("SyntaxError")

