print("\t\t\tWelcome to the Factor ")

c=0 #inicializamos el contador  
n=int(input("Introduzca el extremos superior: "))  
print("Múltiplos de 2 y de 3 entre 1 y %i:"%n)  
for i in range(1,n+1):  
 if i%2==0 and i%3==0:  
  c+=1  
  print(i)  
print("Existen %i múltiplos de 2 y 3 en ese rango, incluidos los extremos"%c)
print("In Summary:")
for factors in [1,2,3,4,5,6,7,8,9,10]:
    print(f"{n} * {n} = {n**2}")

run=input("Run again (y/n): ")

if run=='yes':
    c=0 #inicializamos el contador  
    n=int(input("Introduzca el extremos superior: "))  
    print("Múltiplos de 2 y de 3 entre 1 y %i:"%n)  
    for i in range(1,n+1):  
     if i%2==0 and i%3==0:  
      c+=1  
      print(i)  
      print("Existen %i múltiplos de 2 y 3 en ese rango, incluidos los extremos"%c)
      print("In Summary:")
      for factors in [1,2,3,4,5,6,7,8,9,10]:
       print(f"{n} * {n} = {n**2}")
    print("Thanks you for using the programs. Have a  great day.")
else:
     run=='no' 
     print("Thanks you for using the programs. Have a  great day.")
