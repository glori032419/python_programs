import random
print("\t\t\tWelcome to the Python Dice App.")
nd = int(input("\nHow many sides would you like on your dice: "))

nv = int(input("\nHow many dice would you like to roll: "))
print("\n--------Results are as followed--------")

td = [0]*(5*nd+1)

for i in range (nv):

    s = 0
    for ii in range (nd):
        s += random.randint(nd,(6*nd))
    td[s-nd]+=1
print(td)
print("\nThank  you for using the Python Dice App.")