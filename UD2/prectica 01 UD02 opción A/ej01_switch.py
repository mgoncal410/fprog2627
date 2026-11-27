PUERTO_8 = 8
PUERTO_16 = 16
PUERTO_24 = 24
PUERTO_48 = 48
puertos = int(input("Cuantos puertos tiene el switch (8, 16, 24, o 48): "))
puertos_ocupados = int(input("Puertos ocupados: "))
if not puertos >= PUERTO_48 or puertos.count():
    print("Error: no hay switches de ese tamaño")
elif (puertos - puertos_ocupados) <= 2 :
    print(f"Quedan {puertos} puertos libres. Aviso: el switch está casi lleno")
elif (puertos - puertos_ocupados):
    print(f"Quedan {puertos} puertos libres")