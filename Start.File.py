import random


guessing_number = random.randint(0,5)

guessString = (input("Welcome to the guessing game! Choose a number between 0 and 5: "))
guess = float(guessString)
numberOfGuesses = 0

while guess != guessing_number:
    numberOfGuesses += 1
    if guess > guessing_number:
        guessString = (input("That guess is too high! Try again: "))
        guess = float(guessString)
    elif guess < guessing_number:
        guessString = (input("That guess is too low! Try again: "))
        guess = float(guessString)

print(f"Congrats! You got the right number of {guessing_number}! It took you {numberOfGuesses} tries!")

print("Now it is time to guess my favorite color.")

favorite_color = "yellow"
color_guess = input("What do you think is my favorite color? ")

while color_guess.lower() != favorite_color:
    color_guess = input("That's not correct. Please try again: ")



print(f"That's right! {favorite_color} is the best color there is!")


import time


print("Let's flip a coin ten times")

time.sleep(2)

for x in range(11):
    coin_flip = random.randint(1,2)
    if coin_flip == 1:
        print("Heads")
    else:
        print("Tails")
    time.sleep(1)


print("Let's decide where to eat for dinner")
time.sleep(2)
print("Thinking...")
time.sleep(3)

restaurants = ["Taco Bell", "Burger King", "White Castle", "Freddy's"]

restaurant_number = random.randint(0, 3)
restaurant_choice = (restaurants[restaurant_number])

print(f"Let's go to {restaurant_choice}!")