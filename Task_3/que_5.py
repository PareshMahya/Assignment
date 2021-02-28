
# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

que5 = [0,1,2,3,46,32,466,33,33]
qa5 =[]
for i in range(len(que5)):
    if que5[i]%2!=0:
        qa5.append(que5[i])
print(qa5)

