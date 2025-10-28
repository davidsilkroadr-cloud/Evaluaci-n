print("_________LA PLATA DEL ABUELOOOOOO!!!!___________")
ingreso_anual = float(input("Ingreso anual ($): "))
edad = int(input("Edad: "))
dependientes = int(input("Número de dependientes: "))

ingreso_gravable = ingreso_anual - (dependientes * 1000)
if ingreso_gravable < 0:
    ingreso_gravable = 0

if ingreso_gravable <= 10000:
    impuesto = 0
elif ingreso_gravable <= 50000:
    impuesto = (ingreso_gravable - 10000) * 0.10
else:
    impuesto = 4000 + (ingreso_gravable - 50000) * 0.20

if edad > 65:
    impuesto = impuesto * 0.95

print(f"Impuesto a pagar: ${impuesto:.2f}")