# 
# 4. Create a login page backend to ask users to enter the username and password. 
#    Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
#

print('Enter correct username and password combo to continue')
count=0
username = input('Enter username : ')
if username =='Paresh':
    while count<3:
        password = input('Enter password: ')
        if password=='Pm13': 
            print('Access granted')
            break
        elif password !='Pm13' and count<3:
            print('\nAccess denied. Re-Type Password.')
            count += 1
            # print(count)
        elif count==3:
            break
        else:
            print("\nOops, Password is incorrect.\nAccess denied.")
            break
elif username !='Paresh':
    print("\nSorry, the Username is incorrect. \nAccess denied.")
