#
# 4. Write a program in Python using generators to reverse the string. 
#       Input String = “Consultadd Training”
# 

def rev_str(my_str):
    my_str ="".join(reversed(my_str))
    yield my_str

x = rev_str("Consultadd Training")
print(x.__next__())
