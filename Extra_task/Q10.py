#
# 
# 10. Generate and print another tuple whose values are even numbers in the given tuple(1,2,3,4,5,6,7,8,9,10).
#
usr_ip = (1,2,3,4,5,6,7,8,9,10)
usr_ip_list = list(usr_ip)
evn_num = []
for i in usr_ip_list:
    if i%2==0:
        evn_num.append(i)
    else:
        pass
ans= tuple(evn_num)
print(ans)
