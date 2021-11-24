print("Welcome to the Letter Counter App")
user=input("What is your name?: ")
print("Hello ",user.upper())# usamos el metodo upper para comvertir una palabra en mayuscula.

print("I will count the number of times that specific letter occurs in a message. ")
message=input("Please enter a message: ")
cont=0
letter_count=input("Which letter would you like to count the ocurrences of: ")

for i in message:
    if i==letter_count:
        cont+=1
print(f"{user} your message has {message.count(letter_count)} {letter_count} in it.")
#usamos el count para contar el numero de veces de una letra en un mensaje.