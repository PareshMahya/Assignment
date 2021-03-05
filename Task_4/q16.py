# 16. What is the output of the following codes:
# ---------- (i) --------- 
# def foo():
#         try:
#             print("hi")
#             return 1    
#         finally:
#             print("hi")
#             return 2 
#         k = foo()
#         print(k)

# In the above program Indentation Error.
def foo():
        try:
            print("hi")
            return 1    
        finally:
            print("hi")
            return 2 
k = foo()
print(k)
# If we fixed Indentation Error then it will run both block, try block will save value "1" but finally block will overwrite the value by "2". 
# And we get only "2" out put. 
#
# --------- (ii) ---------- 
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

# Here program is not going to execute, because of  Indentation error of a(). 
# If we fixed it, still we have 
# NameError: name 'f' is not defined 
# And i don't know what is x, and f so i can not fix this error 
# Here only problem in Try block, finally block will work