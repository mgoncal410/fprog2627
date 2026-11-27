# Programa: Analiza tres lecturas de temperatura de CPU y muestra alertas.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Constantes de umbrales de temperatura
TEMP_CRITICA = 90.0
TEMP_ALTA = 75.0
DIF_INESTABLE = 15.0
NUM_LECTURAS = 3

t1 = float(input("Lectura 1 (°C): "))
t2 = float(input("Lectura 2 (°C): "))
t3 = float(input("Lectura 3 (°C): "))

# max() y min() aceptan varios argumentos y devuelven el mayor y el menor directamente
maxima = max(t1, t2, t3)
minima = min(t1, t2, t3)
media = (t1 + t2 + t3) / NUM_LECTURAS

print(f"Máxima: {maxima:.1f} °C | Mínima: {minima:.1f} °C | Media: {media:.1f} °C")

# Primer bloque condicional: evalúa el estado según la temperatura máxima
if maxima >= TEMP_CRITICA:
    print("Estado: CRÍTICO - apagando el equipo")
elif maxima >= TEMP_ALTA:
    print("Estado: ALTO - revisa la ventilación")
else:
    print("Estado: normal")

# Segundo bloque condicional INDEPENDIENTE (es otro 'if', no un 'elif'):
# Se evalúa siempre, sin importar qué pasó en el bloque anterior
if (maxima - minima) > DIF_INESTABLE:
    print("Aviso: lecturas inestables, revisa el sensor")