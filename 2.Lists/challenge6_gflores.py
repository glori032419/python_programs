print("\tWelcome to the Grade Sorter App\n")
grades=[ ]

grades.append(int(input("What is your first grade (0-100): ")))
grades.append(int(input("What is your second grade (0-100): ")))
grades.append(int(input("What is your third grade (0-100): ")))
grades.append(int(input("What is your fourth grade (0-100): ")))

print("\nYour grades are: ",grades)

grades= sorted(grades)
grades = grades[ : :-1]
print(f"\nYour grades from highest to lowest are: {grades}")

print(f"\nThe lowest two grades will now be dropped.")
print(f"Removed grade: {grades.pop(3)}")
print(f"Removed grade: {grades.pop(2)}")
#use el metodo pop para eliminar 

print(f"\nYour remaining grades are: {grades}")
print(f"Nice work! Your highest grade is a {max(grades)}")