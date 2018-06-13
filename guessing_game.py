from random import randint

print("I'm think of a number between 1 and 10.")
guess = int(input("Input a number: "))
# print(guess)

game = randint(0, 10)

if game == guess :
    print("You got it right!")
    print(str(game) + " was the correct answer")
else :
    print("Sorry. " + str(guess) + " Isn't correct. Try again.")