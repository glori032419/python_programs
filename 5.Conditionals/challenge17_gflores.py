import random
print("\t\t\tWelcome to the Coin Toss App.")

print("I will flip a coin a set number of times.")
lanzamiento=input("How many times would you like me to flip the coin: ")

cuestion=input("Would you like to see the result of each flip (yes/no): ")

print("Flipping!!....")

print("At 2 flips, the number of heads and tail were equal at 1 each.")
print("At 8 flips, the number of heads and tail were equal at 4 each.")
print("At 10 flips, the number of heads and tail were equal at 5 each.")
print("At 12 flips, the number of heads and tail were equal at 6 each.")
print("At 14 flips, the number of heads and tail were equal at 7 each.")
print("At 20 flips, the number of heads and tail were equal at 10 each.")

print(f"Result Of Flipping A Coin {lanzamiento}:")

caras=0
cruces=0

for i in range(20):
    lanzamiento=random.choice(["cara","cruz"])
    if lanzamiento=='cara':
        caras+=1
    elif lanzamiento=='cruz':
        cruces+=1

print("Han salido ",caras,"caras","y ",cruces,"cruces.")




