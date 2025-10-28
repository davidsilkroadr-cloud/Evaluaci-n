print("_________hola mundoooo, aquí el tren sabroson ;)___________")
senal = input("¿cuál es el color de la señal?(verde/amarillo/rojo): ")
distancia = float(input("¿a qué distancia está la estación? (km): "))
obstaculo = input("¿Hay algún obstáculo? (si/no): ")

# Verificar obstáculo primero
if obstaculo == "si":
    velocidad = 0
elif senal == "verde":
    if distancia > 5:
        velocidad = 100
    else:
        velocidad = 80
elif senal == "amarillo":
    if distancia > 3:
        velocidad = 50
    else:
        velocidad = 30
elif senal == "rojo":
    velocidad = 0
else:
    velocidad = 0
    print("Señal no válida")

print(f"Velocidad del tren: {velocidad} km/h")