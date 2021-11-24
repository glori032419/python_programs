print("Welcome to the Binary/Hexadecimal Converter App")

valores=int(input("Compute binary and hexadecimal values up to the following decimal number: "))

print("Generating lists...Complete!.")

if valores>1:
    print(list(range(0,valores+1)))
else:
    print(list(range(0,valores -1,-1)))

print("Using slices, we will now show a portion of each list.")
decimal_1=int(input("What decimal number would you like to start at: "))
decimal_2=int(input("What decimal number would you like to stop at: "))

print(f"Decimal values from {decimal_1} to {decimal_2}: ")

if decimal_2>decimal_1:
    print(list(range(decimal_1,decimal_2+1)))
else:
    print(list(range(decimal_1, decimal_2 -1,-1)))

print(f" Binary values from {decimal_1} to {decimal_2}: ")

binario=bin(decimal_1)
print(binario)

binario=bin(decimal_2)
print(binario)

binario=bin(valores)
print(binario)

print(f"Hexadecimal values from {decimal_1} to {decimal_2}: ")

hexadecimal =hex(decimal_1)
print(hexadecimal)

hexadecimal= hex(decimal_2)
print(hexadecimal)

hexadecimal= hex(valores)
print(hexadecimal)

print(f"Press Enter to see all values from 1 to {valores}")
print("Decimal-----Binario-----Hexadecimal")

print(f"{decimal_1}----{binario}----{hexadecimal}")
print(f"{decimal_2}----{binario}----{hexadecimal}")
print(f"{valores}----{binario}----{hexadecimal}")