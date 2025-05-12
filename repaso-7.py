numero_1= int(input("ingresa el primer numero: "))
numero_2= int(input("ingresa el segundo numero:  "))

if numero_1 < numero_2:
    print(f"el numero mayor es: {numero_2} ")
elif numero_2 < numero_1:
    print(f"el numero mayor es: {numero_1}")
else:
    print("ambos numeros son iguales")
