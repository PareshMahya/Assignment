#
# 5.	Write an example on decorators
# 

# Modification of original function
def use_zero(func):
    def inner(a,b):
        if a==0 or b==0:
            print("Multiplication of zero is always zero!")
            return
        return func(a,b)
    return inner
@use_zero

# original function
def mul(a,b):
    print(a*b)

# call original function
x = mul(1,0)
