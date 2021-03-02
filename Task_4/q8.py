
# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).

def t_square_number(start,end):
    l=[]
    for i in range(start,end+1):
        ans = i*i
        l.append(ans)
    t=tuple(l)
    print(t)

(x,y)=(int(input("Enter start number :")),int(input("Enter end number :")))
t_square_number(x,y)