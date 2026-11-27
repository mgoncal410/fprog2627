# Programa: Calcula el tiempo estimado de descarga de un fichero en h, min y s.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Constantes de conversión de unidades y tiempo
MB_POR_GB = 1000
MB_POR_TB = 1000000
BITS_POR_BYTE = 8
SEG_POR_HORA = 3600
SEG_POR_MIN = 60

tamano = float(input("Tamaño del fichero: "))
# .upper() convierte "gb" o "Gb" en "GB" para comparar siempre en mayúsculas
unidad = input("Unidad (MB, GB o TB): ").upper()
velocidad = float(input("Velocidad de la conexión (Mb/s): "))

# 1º Comprobamos si la velocidad es válida (no se puede dividir entre 0 o negativo)
if velocidad <= 0:
    print("Error: la velocidad debe ser mayor que 0")
else:
    tamano_mb = 0.0
    # Usamos una variable booleana "bandera" (flag) para saber si la unidad fue válida
    unidad_valida = True

    match unidad:
        case "MB":
            tamano_mb = tamano
        case "GB":
            tamano_mb = tamano * MB_POR_GB
        case "TB":
            tamano_mb = tamano * MB_POR_TB
        case _:
            unidad_valida = False
            print("Error: unidad no válida")

    # Solo hacemos el cálculo si la unidad existía
    if unidad_valida:
        # Pasamos MB a Megabits (* 8), dividimos entre Mb/s y redondeamos con round()
        segundos_totales = round((tamano_mb * BITS_POR_BYTE) / velocidad)

        # Descomposición clásica de segundos en horas, minutos y segundos (// y %)
        horas = segundos_totales // SEG_POR_HORA
        resto = segundos_totales % SEG_POR_HORA
        minutos = resto // SEG_POR_MIN
        segundos = resto % SEG_POR_MIN

        print(f"Tiempo estimado: {horas} h {minutos} min {segundos} s")

        if horas >= 1:
            print("Descarga larga: prográmala para la noche")