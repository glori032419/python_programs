import statistics
import copy

print("\t\t\tWelcome to the Average Calculator App.")

user=input("What is your name: ")
calificaciones=[]
print(input("How many grades would you like enter: "))

calificaciones.append(int(input("\t\tEnter grade: ")))
calificaciones.append(int(input("\t\tEnter grade: ")))
calificaciones.append(int(input("\t\tEnter grade: ")))
calificaciones.append(int(input("\t\tEnter grade: ")))
calificaciones.append(int(input("\t\tEnter grade: ")))

calificaciones.sort(reverse=True)
print("\nGrades Highest to Lowest: ",calificaciones)

print(f"\n{user}'s Grade Summary: ")
print("\t\tTotal Number of Grades: ",len(calificaciones))
print("\t\tHighest Grades: ",max(calificaciones))
print("\t\tLowest Grades: ",min(calificaciones))

mean =statistics.mean(calificaciones)
print("\t\tAverige:",mean)

print(f"\nGood luck {user}!.")

print("\nLets see what your average could have been if you did better/worse on an asignment.")

new_list=copy.copy(calificaciones)

print(input("\nWhat grade would you like to change: "))
del new_list[4]
new_list.insert(4,int(input(f"Whats grade would you like to change: {new_list[4:]}")))

print("\nNew Grades Highest to Lowest:",new_list)
print(f"\n{user}'s New Grade Summary: ")
print("\t\tTotal Number of Grades: ",len(new_list))
print("\t\tHighest Grades: ",max(new_list))
print("\t\tLowest Grades: ",min(new_list))

mean =statistics.mean(new_list)
print("\t\tAverige:",mean)

print("\nToo bad your original grades are still the same!.")
print(calificaciones)
print("\nYou should go ask for extra credit!.")




