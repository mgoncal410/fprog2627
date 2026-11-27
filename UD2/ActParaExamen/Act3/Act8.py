# Programa: Valida el nombre de un equipo según las normas de red e indica su tipo.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

LONG_MIN = 5
LONG_MAX = 15

nombre = input("Nombre del equipo: ").strip()

# Validación en cascada en el orden estricto del enunciado:
# 1. Longitud fuera del intervalo [5, 15] (< 5 o > 15)
if len(nombre) < LONG_MIN or len(nombre) > LONG_MAX:
    print(f"Error: debe tener entre {LONG_MIN} y {LONG_MAX} caracteres")
# 2. Espacios intermedios
elif " " in nombre:
    print("Error: no puede contener espacios")
# 3. .isupper() verifica que todas las letras estén en mayúsculas (ignora guiones y números)
elif not nombre.isupper():
    print("Error: las letras deben ir en mayúsculas")
# 4. Comprobamos los prefijos válidos para clasificar el equipo
elif nombre.startswith("PC-"):
    print("Nombre válido: puesto de trabajo")
elif nombre.startswith("SRV-") or nombre.startswith("NAS-"):
    print("Nombre válido: servidor")
else:
    print("Error: debe empezar por PC-, SRV- o NAS-")