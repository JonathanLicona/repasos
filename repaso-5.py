total_factura = float(input("ingresa el valor total de la cuenta: "))
porcentaje = int(input("que porcentage de propina quieres dejar 10% / 15% / 20% : "))
if porcentaje == 10 or porcentaje == 15 or porcentaje == 20:
    op = total_factura * porcentaje / 100
    total = total_factura + op 
    print(op)
    print(f"total a pagar: {total}")
else:
    print("este porcentaje no es valido, 10% / 15% / 20%" )
