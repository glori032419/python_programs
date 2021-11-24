print("Welcome to the Miles Per Hour Conversion App.")
kmh=float(input("What is your speed in miles per hour?: "))
mph=0.4474*kmh #este es el valor de mph
print("miles per hour:",kmh)
print(f"Your speed in meters per second is: {round(mph,2)}")
#usamos la funcion round para redondear la respuesta a 2 decimales.
