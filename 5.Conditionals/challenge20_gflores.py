import random
print("\t\t\tWelcome to a game of Rock, Paper, Scissors.")
cuestion=input("How many rounds would you like to play: ")
player=0
computer=" "

choose=input("Time to pick...rock,paper,scissors:")

while True:
    ale=random.randrange(0,3)
    print("1.Rock")
    print("2.paper")
    print("3.Scissors")
    choose=input("Time to pick...rock,paper,scissors:")
    
    if choose=='Rock':
        chooseUser="rock"
    elif choose=='Paper':
        chooseUser="Paper"
    elif choose=="Scissors":
        chooseUser="scissors"
    print("your choose: ",chooseUser)

    if ale==0:
        computer="Rock"
    elif ale==1:
        computer="Paper"
    elif ale==2:
        computer="Scissors"
    print("the computer choose: ",computer)

    if computer=="Rock" and chooseUser=="Paper":
        print("Win, paper envelops  rock")
    elif computer=="Paper" and chooseUser=="Scissors":
        print("win, scissors envelops paper")
    elif computer=="Scissors" and chooseUser=="Rock":
        print("win, rock to crush at Scissors")
    if  computer=="Paper" and chooseUser=="Rock":
        print("Game over, paper envelops rock")
    elif computer=="Scissors" and chooseUser=="Paper":
        print("game over, Scissors cut paper")
    elif computer=="Rock" and chooseUser=="Scissors":
        print("Game over, Rock crush at Scissors")
    elif computer==chooseUser:
        print("It's a tie, how boring!")
    
    play_again=input("PLAY AGAIN (s/n): ")
    if play_again.lower()!="s":
        break