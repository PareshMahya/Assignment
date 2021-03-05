#
# 12. Write a function to compute 5/0 and use try/except to catch the exceptions.
a = 5
b = 0
try:
    ans = a/b
    print(ans)
except Exception as pm:
    print("There is ",pm, "error")