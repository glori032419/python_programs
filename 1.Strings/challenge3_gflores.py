print("Welcome to the Temperature Conversion App.")

fahrenheit=float(input("What is the temperature in degrees Fahrenheit: "))
celsius=(fahrenheit -32) * 5.0/9.0#aplicamos la formula de conversion F a C
kelvin=273.15 # el valor de K
print(f"Degrees Fahrenheit: {fahrenheit}")
print('{} Degrees Fahrenheit son {} Degrees Celsius '.format(fahrenheit,(round(celsius,4))))
print(f"Degrees Kelvin: ",str(round(celsius,4)+kelvin))
#cada resultado tendra la reducion de 4 decimales con round
