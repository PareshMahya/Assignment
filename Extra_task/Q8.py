#
# 8.	Write a program in Python to complete the following task:
# Create two lists such as even_list and odd_list
# Ask user to enter a number in the range of 1,50 and make sure if the entered number is even, append it to the even_list and if the entered number is odd append it to the odd_list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you enter all the  5 elements, calculate the sum of the list and return the maximum of the list.
# 

even_list = []
odd_list = []
count=0
while count<5:
    count+=1
    uip=int(input("Enter a number in the range of 1,50 :"))
    
    if uip%2==0 and uip<=50:
        print("very good, It's valid number.")
        even_list.append(uip)
    elif uip%2!=0 and uip<=50:
        print("very good, It's valid number.")
        odd_list.append(uip)
    else:
        print("Sorry, It is not a valid number.")
        count-=1

print("even list:",even_list,",\tSum of the even list :",sum(even_list), ",\t and Max of the even lsit", max(even_list))
print("odd list",odd_list, ",\tSum of the odd list :", sum(odd_list), ",\t and Max of the odd lsit", max(odd_list))
