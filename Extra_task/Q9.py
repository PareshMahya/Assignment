# 9.Write a program to find out the occurrence of a specific character  from an alphanumeric string.
#     Sample input: 12abcbacbaba344ab  
#     Expected output: a=5 b=5 c=2
#     NOTE: Make sure to avoid counting the occurrence of  numeric values  in the string.


usr_ip = "12abcbacbaba344ab"
ans={}
for i in usr_ip:
    count = 0
    if i.isalpha():
        if i in ans:
            ans[i]+=1
        else:
            ans[i]=1
    else:
        pass
for k, v in ans.items():
    print(k,"=",v)