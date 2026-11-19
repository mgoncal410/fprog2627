bateria = int(input("Cual es tu nivel de bateria: "))

if bateria <= 0:
    print("Bateria agotada: apagando el equipo")
elif bateria <= 19:
    print("Bateria baja: conecta el cargador")
elif bateria <= 79:
    print("Bateria media")
elif bateria <= 100:
    print("Bateria alta")
else:
     print("Valor no válido")