# Programa: Valida una contraseña según las normas del dominio e indica su nivel.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

LONGITUD_MINIMA = 8
LONGITUD_FUERTE = 12

usuario = input("Usuario: ").strip().lower()
contrasena = input("Nueva contraseña: ")

# Cascada en orden estricto: se detiene en el PRIMER error que encuentre
# 1. len() cuenta cuántos caracteres tiene la cadena
if len(contrasena) < LONGITUD_MINIMA:
    print(f"Error: debe tener al menos {LONGITUD_MINIMA} caracteres")
# 2. Comprobamos si hay algún espacio en blanco dentro
elif " " in contrasena:
    print("Error: no puede contener espacios")
# 3. .isdigit() devuelve True si TODOS los caracteres son dígitos (0-9)
elif contrasena.isdigit():
    print("Error: no puede estar formada solo por números")
# 4. .isalpha() devuelve True si TODOS los caracteres son letras (a-z, A-Z)
elif contrasena.isalpha():
    print("Error: no puede estar formada solo por letras")
# 5. Truco mayúscula: si al pasarla a minúsculas queda igual, es que no tenía ninguna mayúscula
elif contrasena == contrasena.lower():
    print("Error: debe tener al menos una letra mayúscula")
# 6. Pasamos la contraseña a minúsculas para detectar el usuario aunque cambie mayúsculas (ej. Ana2026)
elif usuario in contrasena.lower():
    print("Error: no puede contener el nombre de usuario")
else:
    # Si supera todos los filtros anteriores, la contraseña es válida
    print("Contraseña válida")
    # if anidado para clasificar su nivel de seguridad según su longitud
    if len(contrasena) >= LONGITUD_FUERTE:
        print("Nivel: fuerte")
    else:
        print("Nivel: aceptable")