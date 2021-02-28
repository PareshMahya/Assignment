
# 2.	Create a list of size 5 and execute the slicing structure

list = [1,[1,2,3.0,4.5,5.6,7,8,9,0],"Hello, my friend Kevin","hseraP si sihT,iH",5+1j]
print("\nThis is the list-->", list,", \nlength of list is-->", len(list))
print("Picking an single element")
print("This is the print will show pick the first element from the list and that is -->", list[0], "\nAnd last element is -->", list[len(list)-1], "\nString Data in a list -->",list[2])
print("Slicing element from diffrent Data Structure")
print("\nThis is the print for pick element from a nested list. \nI am picking second element and inside that five element, excluding the first and last element with nornal(single) interval. \nAnd \nThat List is -->", list[1][1:len(list)])
print("\nThis print of picking a list with some abnormal intervals. \nHere I am picking the second element of the original list and inside that list picking every other element. \nThat list is-->",list[1][::2])
print("\nSlicing element inside string")
print(list[2])
print("Picking string with three interval is -->", list[2][::3])
print("This print is for picking String in reverse order -->",list[3][-1:-(len(list[3])+1):-1])
