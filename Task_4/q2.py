# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
#    Sample input: “abcSdefPghijQkl”
#    Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

q1 = "abcSdefPghijQkl"
def uplow(x):
    up = 0
    low = 0
    for i in q1:
        if i >="a" and i <="z": low = low + 1
        elif i >="A" and i <="Z": up = up + 1
    print("No. of Uppercase characters :", up, "No. of Lower case Characters : ", low)
uplow(q1)