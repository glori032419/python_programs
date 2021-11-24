print('Welcome to the Multiplication/Exponent Table App')
name = input("\n\nWhat is your name: ")
num = float(input("What number would you like to work with: "))
message = name.title() + ", Math is cool!"
#use el metodo title para tener la primera letra en Mayuscula como un titulo
numbers = (1,2,3,4,5,6,7,8,9)
#puse una tupla con los numeros importantes

print(f"\n\n Multiplication Table For {num}\n")
for n in numbers:
  print(f'\t {n} * {num} = {round(n * num,4)}')
  
print(f"\n\n Exponent Table For {num}\n")
for n in numbers:
  print(f'\t {num}**{n} = {round(num**n,4)}')

print('\n',message)
print(f'\t{str.lower(message)}')
print(f'\t\t{str.title(message)}')
print(f'\t\t\t{str.upper(message)}')