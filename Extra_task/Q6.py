#
# 6.	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.
#

def evenLengthWord(x): 
    y = x.split(' ') 
    print(y)
    ans = ""
    for word in y:
        if len(word)%2==0:
            ans += " "+ word
        else:
            ans = ans
    return ans  
x = "hello my name is abcde paresh kumar " 
y = evenLengthWord(x)
print (y.lstrip())