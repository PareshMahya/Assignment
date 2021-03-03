
# 15. Write a program in Python to  multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.

def mul__By_self_list_element (l):
    ans = l*l
    return ans
user_list=[1,2,3,4,5,6,6,8,9,7,0]
x=map(mul__By_self_list_element, user_list)
print(type(x))
print(list(x))
 
