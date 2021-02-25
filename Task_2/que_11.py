
#11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

print("guess the lucky number in five guess")
counter=1
while counter<=5:
    que_10 = int(input("guess the lucky number: "))
    counter +=1
    if que_10 ==50:
        print("Good Guess!")
        break
    elif que_10 !=50:
        print("Try again!")       
else:
    print("Sorry but that was not very successful")