print("\t\t\tWelcome to the Even Odd Number Sorter App.")
valores=[]
def main():
     valores=int(input("\nhow many numbers do you want to enter: "))
     print("\n---------Result Summary---------")

     if valores<0:
          print("It is impossible")
     else:
          pares=0
          for i in range(1,valores + 1):
               numero=int(input(f"\tEnter the numbers {i}: "))
               if numero % 2 ==0:
                    pares+= 1
          print(f"\nThe following {pares} numbers are even and {valores - pares} numbers odd.")
          print("\nThank you for using the program. Goodbye.")
          print(valores)

if __name__=="__main__":
     main()
             
 