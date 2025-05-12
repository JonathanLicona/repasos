# Pide un número al usuario. Di si es positivo, negativo o si es cero.

numero = int(input("ingresa un numero: "))

if numero < 0:
    print("el numero es negativo")
elif numero > 0:
    print("el numero es positivo")
else:
    print("el numero es cero")
