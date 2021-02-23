#2. Create a variable of type complex and swap it with another variable of type integer.
a = 1
d = 1+2j
print ("The values of 'a' and 'd' are ", a, " and", d), type(a), type(d)
a, d = d, a
print ("After swapping the values of 'a' and 'd' new values are ", a, " and", d), type(a), type(d)