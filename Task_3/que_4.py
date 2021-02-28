
#4.	Find the largest and smallest number from a given list.
# For smallest number by using "min" keyword
list = [1,2,0.5,0,-0.5,4,5,]
print("This is the smallest number ", min(list), "of the list = ", list)
# For largest number by using "max" keyword
print("This is the largest number ", max(list), "of the list = ", list)

# By using for loop keyword
list1 = []
n = int(input("Enter number of elements in list: "))
for i in range(1, n+1):
    ele= int(input("Enter your elements: "))
    list1.append(ele)
m = list1[0]
for i in range(n):
    if list1[i] < m: 
        m = list1[i]
    else:
        pass
print("This is the smallest number ", m, "of the list = ", list1)
