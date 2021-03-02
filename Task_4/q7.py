
# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.

def find_max_len_string(str1,str2):
    if len(str1)==len(str2):
        print(str1)
        print(str2)
    elif len(str1)>len(str2):
        print(str1)
    else:
        print(str2)

x = input("Enter your string :")
y = input("Enter your string :")

find_max_len_string(x,y)