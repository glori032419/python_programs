print("\t\t\tWelcome to the Yes or No Issue Polling App.")

votantes={}

print("\n\tWhat is the  yes or no issue you will be voting on today:  ")
cuestion1=("Should soda be banned for young children?")


num_cuestion=input("\tWhat is the number of voters you will allow on the issue: ")
password=input("\n\tEnter a password for polling results: ")
name=input("\tEnter your full name: ")
print("\nHere is our issue: ",cuestion1)
answer=input("\nWhat do you think....yes or no: ")

votantes={"name":name,"password":password,"answer":answer}

if answer=='yes':
    print(f"\nThanks you {name}! Your vote of yes has been recorded.")
else:
    answer=='no'
    print(f"\nThanks {name}! Your vote of no has been recorded.")

print("\t\tThe following people voted: ")
print("\n",votantes)

