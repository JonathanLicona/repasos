Peso = int(input("ingresa tu peso (kg): "))
altura = float(input("ingresa tu altura (m): "))

imc = Peso / (altura**2)
print(f"Tu imc es: {imc}")
if imc < 18.5:
    print(f"estas en bajo peso{imc}")
elif imc >= 18.5 and imc <= 24.9:
    print("estas normal")
elif imc >= 25 and imc <= 29.9:
    print(f"estas en sobrepeso{imc} ")
else:
    print(f"estas en obesidad {imc}")
  
