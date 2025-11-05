#Generate a random number
import random
number_to_guess = random.randint(1, 100)
#Loop
while True:
    try:
#Ask: guess the number?
        guess = int(input("Guess the number between 1 and 100: "))
    #if not a valid number, print an error
    #if number < guess, print too low
        if guess < number_to_guess:
            print("Too low")
    #if number > guess, print too high
        elif guess > number_to_guess:
            print("Too high")
    #else, print well done
        else:
            print("Well done")
            break
    except ValueError:
        print("Please enter a valid number")