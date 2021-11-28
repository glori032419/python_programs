from math import sqrt
import math
print("\t\tWelcome to the Averige Calculator App.")
digits=int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

print(f"The first {digits} numbers of the Fibonacci sequence are: ")

def Fibonaci(numero):
    if(numero==0):
     return 0
    elif (numero==1):
        return 1
    else:
        return(Fibonaci(numero-2)+Fibonaci(numero-1))
digits=int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
print("Fibonaci s: ")
for digits in range(0,digits):
    print(Fibonaci(digits))

print("The corresponding Golden Ratio values are: ")

def fibonacci_golderatio(target):
    if target <2:
        return target
    if target >71:
        return fibonacci_golderatio(target)

    sqrt5=math.sqrt(5)
    golden_ratio=(1 + sqrt5)/2

    return math.floor(math.pow(golden_ratio,target)/sqrt5)

for digits in range(0,digits):
    print(fibonacci_golderatio(digits))
