print("____________________Papi flaviooooooooooo, tu reactoooor!!!__________________")
temperatura = float(input("¿cuál es la temperatura del reactor?(°C): "))
presion = float(input("¿cuál es la presión del reactor?(bar): "))
nivel_refrigerante = float(input("¿cuál es el nivel de refrigerante?(%): "))

if temperatura > 800 and presion > 500:
    estado = "CRÍTICO"
elif (600 <= temperatura <= 800) or (300 <= presion <= 500):
    estado = "ALERTA"
else:
    estado = "NORMAL"

if nivel_refrigerante < 50:
    if estado == "CRÍTICO":
        estado = "ALERTA"
    elif estado == "ALERTA":
        estado = "NORMAL"

print(f"Estado del reactor: {estado}")