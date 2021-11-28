print("\t\t\tThe Python Calculator App.")

print("\nEnter two numbers and an operation and the desired operation will be performed.")
numero1=int(input("Enter the number: "))
numero2=int(input("Enter the number: "))


eleccion=0

while eleccion !=6:
    print(""" 
    Indique la operacion a realizar
    1)addition
    2)subtraction
    3)multiplication
    4)division
    5)change num
    6)get out
    """)

    eleccion=int(input())
    if eleccion==1:
        print(" ")
        print("RESULT: ",numero1," + ",numero2," = ",numero1+numero2)
    elif eleccion==2:
        print(" ")
        print("RESULT: ",numero1," - ",numero2," = ",numero1-numero2)
    elif eleccion==3:
        print(" ")
        print("RESULT: ",numero1," x ",numero2," = ",numero1*numero2)
    elif eleccion==4:
        print(" ")
        print("RESULT: ",numero1," / ",numero2," = ",float(numero1/numero2))
    elif eleccion==5:
        numero1=int(input("Enter the number: "))
        numero2=int(input("Enter the number: "))
    elif eleccion==6:
        print("Goodbye.")
