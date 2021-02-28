
# 3.	Write  a program to get the sum and multiply of all the items in a given list.
sum=0
ans=1
list = [1,2,3,4,5]
for i in list:
    sum += i
for j in list:
    ans = ans * j
print ("The sum of all list value = ", sum)
print ("The multiplication of all list value =", ans)
