# Programa: Clasifica una edad por grupo tras validar que es un número entero válido.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

EDAD_MAXIMA = 120
LIMITE_INFANCIA = 11
LIMITE_ADOLESCENCIA = 17
LIMITE_ADULTA = 64

# Leemos primero como texto (sin int()) para poder comprobarlo antes de convertir
entrada = input("Edad: ").strip()

# 'not entrada.isdigit()' entra si el usuario escribió letras ("quince"), negativos ("-5") o vacío
if not entrada.isdigit():
    print("Error: escribe un número entero")
else:
    # Como ya sabemos que son todo dígitos, convertir con int() es 100 % seguro (no dará ValueError)
    edad = int(entrada)
    if edad > EDAD_MAXIMA:
        print("Error: edad no válida")
    elif edad <= LIMITE_INFANCIA:
        print("Infancia")
    elif edad <= LIMITE_ADOLESCENCIA:
        print("Adolescencia")
    elif edad <= LIMITE_ADULTA:
        print("Edad adulta")
    else:
        print("Jubilación")