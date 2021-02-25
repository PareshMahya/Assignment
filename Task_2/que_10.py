
#10.	Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
#       counter=1
#       While counter <= 5:
#       print(“Type in the”, counter, “number”
#       counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If thecorrect number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.

print("guess the lucky number in five guess")
counter=1
while counter<=5:
    que_10 = int(input("guess the lucky number: "))
    counter +=1
    if que_10 ==50:
        print("Good Guess!")
    elif que_10 !=50:
        print("Try again!")       
else:
    print("Game Over!")
