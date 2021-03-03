
# 14.	Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7. Make sure to use only higher order functions. 

user_range_start_value = int(input("Enter your value of staring range :" ))
user_range_end_value = int(input("Enter your value of end range:" ))
user_range_end_value +=1
#print(list(range(user_range_start_value,user_range_end_value)))
x= filter(lambda i: i%3!=0 and i%7==0, range(user_range_start_value,user_range_end_value))
print(list(x))
