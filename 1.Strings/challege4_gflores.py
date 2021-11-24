import math
print("\tWelcome to the Right Triangle Solver App")

cateto_A=float(input("What is the first leg og the triangle: "))
cateto_b=float(input("What is the second leg of the triangle: "))

hipotenusa=math.sqrt((cateto_A**2)+(cateto_b**2))#elevamos al 2 cada cateto para hallar la hipotenusa
print(f"For a triangle with legs of {cateto_A} and {cateto_b} the hypotenuse is {round(hipotenusa,3)}")

area=float(cateto_A)*float(cateto_b)/2.0#multiplicamos los lados y dividimos /2
print(f"For a triangle with legs of {cateto_A} and {cateto_b} the area is {area}")