from math import sqrt
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
