print("\t\t\tWelcome to the favorite Teachers Program.")

fav_teachers=[]
fav_teachers.append(str.title(input("Who is your first the favorite teacher: ")))
fav_teachers.append(str.title(input("Who is your second the favorite teacher: ")))
fav_teachers.append(str.title(input("Who is your third the favorite teacher: ")))
fav_teachers.append(str.title(input("Who is your fourth the favorite teacher: ")))

print("\nYour favorite teachers ranked are: ",fav_teachers)

fav_teachers=sorted(fav_teachers)
print("\tYour favorite teachers alphabetically are: ",fav_teachers)

fav_teachers=sorted(fav_teachers,reverse=True)
print("\n\tYour favorite teachers in reverse alphabetical order are: ",fav_teachers)

print("\n\tYour top two teachers are:",fav_teachers[:0],fav_teachers[:2])
print("\n\tYour next two favorite teachers are: ",fav_teachers[2:])
print("\n\tYou last favorite teacher is: ",fav_teachers[-1:])

print(f"\nYou have a total of {len(fav_teachers)} favorite teachers.")

fav_teachers.insert(0,(str.title(input(f"Ooops,{fav_teachers[0:1]} is no longer your first favorite teacher. Who is your nwe FAVORITE teacher: "))))
print("\nYour favorite teachers ranked are: ",fav_teachers)

fav_teachers=sorted(fav_teachers)
print("\tYour favorite teachers alphabetically are: ",fav_teachers)

fav_teachers=sorted(fav_teachers,reverse=True)
print("\n\tYour favorite teachers in reverse alphabetical order are: ",fav_teachers)

print("\n\tYour top two teachers are:",fav_teachers[:0],fav_teachers[:2])
print("\n\tYour next two favorite teachers are: ",fav_teachers[2:])
print("\n\tYou last favorite teacher is: ",fav_teachers[-1:])

print(f"\n\tYou have a total of {len(fav_teachers)} favorite teachers.")