#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
#The computer makes guesses, and you give it input - is its guess too high or too low? 
#Using bisection search, the computer will guess the user's secret number!


l = 0
h = 100
ans = (l+h)//2

print("Please think of a number between 0 and 100!")

for i in range (l,h):
    print("Is your secret number " + str(ans) + " ?")
    InputFromPrompt = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if InputFromPrompt == 'h':
        h = ans
        ans = (l+h)//2
    elif InputFromPrompt == 'l':
        l = ans
        ans = (l+h)//2
    else: 
        if InputFromPrompt == 'c':
            print("Game over. Your secret number was: " + str(ans))
            break
        else:
            print("Sorry, I did not understand your input.")
