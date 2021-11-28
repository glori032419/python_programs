
print("\t\t\tWelcome to the Voter Registration App.")

user=str.title(input("\tPlease enter your name: ").swapcase())
age=int(input("\tPlease enter your age: "))
parties=["Republicano","Democrata","Independiente","Libertario","Verde"]

if age>18 and age<50:
    print(f"\nCongratulations {user}! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")
    print(parties)
    vote=str.title(input("\n\tWhat party would you like to join: ").swapcase())
    print(f"\nCongratulations {user} You have joined the Independent party!")
    print(f"You are an {vote} person!.")

elif age<=18:
    print("You are not old enough to register to vote.")