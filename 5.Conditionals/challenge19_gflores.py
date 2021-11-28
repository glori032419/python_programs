import random
print("\t\t\tWeolcome to the Guess My number ")

attempts=0
user=str.title(input("Hello! What is your name: ").swapcase())

number=random.randint(1,20)
print(f"Well {user}. I am thinking of a number between 1 and 20.")

while attempts<6:
    print("try to guess")
    approach=input()
    approach=int(approach)

    attempts=attempts + 1

    if approach<number:
        print("Your guess is too low.")
    if approach>number:
        print("Your guess is too high.")
    if approach==number:
        break
if approach==number:
    attempts=str(attempts)
    print("Good job" +user+ "You guessed my number in" +attempts+ "guesses!.")
if approach!=number:
    number=str(number)
    print("Game over. The number I was thinkig of was " +number)
