#
#
#  7.	Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8. 
# x=[1,2,3,4,5,6,7,8,9,-1]
#
def getPairSumNum(x, sum_num):
    n = len(x)
    temp = []
    for i in x:
        for j in x[(i-1):]:
            if x[i] + x[j] == sum_num:
                y = (x[i],x[j])
                temp.append(y)
            if i==(n-2) and j==(n-1):
                break
    print(temp)
    
x = [1,2,3,4,5,6,7,8,9,-1]
sum_num = 8
getPairSumNum(x, sum_num)