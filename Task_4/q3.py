# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(list_q3):
    list_set = set(list_q3)
    unique_list =list(list_set)
    return unique_list

list_1 = [-1, -11, -7, 1, 0, 2 ,3 , 1, 0.5, 45, -1, 6, 78, 0, 9, -11, -7]
print("The given list :", list_1)
print("New unique list : ", unique(list_1))