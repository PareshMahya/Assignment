# 7. Write a program to replace the last element in a list with another list.
#     Sample input: [1,3,5,7,9,10], [2,4,6,8] 
#     Expected output: [1,3,5,7,9,2,4,6,8]

q7_1_list = [1,3,5,7,9,10]
q7_2_list = [2,4,6,8]
ans = q7_1_list[:(len(q7_1_list)-1)] + q7_2_list
print(ans)