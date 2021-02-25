
#9.	Read the two parts of the question below:
#• Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.

'''
que_9_1 = int(input("Guess and enter the lucky number: "))
while que_9_1:
    if que_9_1 == 50:
        print("Right, lucky number is ", que_9_1)
        break
    else: que_9_1 = int(input("guess again the lucky number: "))
'''

#• Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. (The program continues as long as a user has not answered “no” and has not guessed the correct number)
number = int(input("\nGuess and enter the lucky number: "))
while number:
    if number == 50:
        print("\n\t--------  Right, the lucky number is ", number,"  --------\n")
        break
    else:
        number= input("\nSorry, this is not a lucky number, please try again by\nEnter number for guess the lucky number\nor\nEnter the word 'answer' for to quit :")
        if number=="answer":
            answer= input('\nYou want to keep guessing?\nEnter "yes" to keep guessing.\nEnter "no" to stop guessing :')
            if answer=="yes":
                    number = int(input("\nGuess again the lucky number : "))
            elif answer=="no":
                    break
        elif number=="50":
            print("\n\t--------  Right, the lucky number is ", number,"  --------\n")
            break