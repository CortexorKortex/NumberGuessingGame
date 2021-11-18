# Number guessing game!
import random
print("Hello!")
guesses = 5
start = input("Do you want to play ?: ")
while start != "yes":
    break
else:
    print("Lets go to the game!")
    pc = random.randint(0,10)
    print("You need to guess the number!")
    print("Its between 1 and 10, lets give a shoot!")
    while guesses > 0:
        guess = input("Enter a number: ")
        guess = int(guess)
        if guess > pc:
            print("your guess {} is to high like you brohim :/, try again.".format(guess))
            guesses -=1
            print("you got {} more guesses".format(guesses))
        elif guesses < pc:
            print("your guess {} is to small like your dishes buddyboy, try again.".format(guess))
            guesses -=1
            print("you got {} more guesses".format(guesses))

        elif guess == pc:
            guesses = guesses + 1
            print("Yes ma`am! {} was the right number".format(pc))
            print(("you win one more guess chance "))
            print("you got {} more guesses".format(guesses))
    print("The game is over, get out of here!")
            




