
# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)

l = []
for i in range(1,21):
    l.append(i)
q10 = filter(lambda x:x%2==0, l)
print(list(q10))