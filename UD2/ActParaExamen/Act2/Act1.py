# Programa: Calcula el porcentaje de disco ocupado y avisa si supera el límite.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Constante con el límite a partir del cual salta el aviso (en MAYÚSCULAS)
LIMITE_AVISO = 90

# Pedimos datos con decimales -> usamos float()
capacidad = float(input("Capacidad total (GB): "))
usado = float(input("Espacio usado (GB): "))

# Regla de tres para sacar el porcentaje ocupado
porcentaje = (usado / capacidad) * 100

# :.1f muestra el número redondeado a 1 decimal dentro del f-string
print(f"Disco ocupado: {porcentaje:.1f} %")

# Comprobamos si iguala o supera el límite (90 %)
if porcentaje >= LIMITE_AVISO:
    print("¡Aviso! El disco está casi lleno")
else:
    # Si no lo supera (es menor que 90), entra aquí
    print("Espacio suficiente")