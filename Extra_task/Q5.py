#
# 5.	Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.

def reverse_vowel_alphabet(x):
    print(x)
    y = x[::-1]
    print(y)
    ans= ""
    for i in y:
        print(i)
        if i in "aeiouAEIOU":
            ans += i
    return ans    
print(reverse_vowel_alphabet("Hi, this is Paresh"))

