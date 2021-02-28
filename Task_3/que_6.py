
# 6. Create a list of elements such that it contains  the squares of  the first and last 5 elements between 1 and30 (both included).
q6 =[]
for i in range(1,31):
    q6.append(i)
print(q6)

ans = q6[:5]+q6[25:30]
print(ans)