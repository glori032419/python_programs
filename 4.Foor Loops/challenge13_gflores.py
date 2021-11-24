import math
print("\t\tWelcome to the Factorial Calculator App.")

numero=int(input("\nWhat number would you like to compute the factorial of: "))

while numero>0:
    print(numero,end='*')
    numero-=1
print("\nHere is the result from the math library:")
numero=int(input("What number would you like to compute the factorial of: "))
print("the factorial of ",numero,"es",math.factorial(numero))

print("\nHere is the result from my own algoritm:")
numero=int(input("What number would you like to compute the factorial of: "))
factorial=1
if numero!=0:
    for i in range(1,numero+1):
        factorial=factorial*i
print(f"The factorial of {numero} is {factorial}!")

print(f"\nIt is shown twice that {numero}! = {factorial}(with excitement)")