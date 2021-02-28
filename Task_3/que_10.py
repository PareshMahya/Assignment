
# 10. Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
#     Sample input: 34,67,55,33,12,98
#     Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
a=34,67,55,33,12,98
#print(type(a))
l=list(a)
for i in range(len(l)):
    l[i]=str(l[i])
print(l, tuple(l))
