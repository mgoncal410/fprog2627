# Programa: Identifica el tipo de fichero según su extensión.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Limpiamos espacios y pasamos a minúsculas para que .PNG y .png funcionen igual
fichero = input("Nombre del fichero: ").strip().lower()

# 'not in' comprueba si el carácter "." NO aparece en ningún sitio del texto
if "." not in fichero:
    print("El fichero no tiene extensión")
# .endswith() mira si la cadena termina exactamente con esa subcadena
elif fichero.endswith(".py"):
    print("Script de Python")
# 'or' devuelve True si se cumple al menos una de las dos terminaciones
elif fichero.endswith(".jpg") or fichero.endswith(".png"):
    print("Imagen")
elif fichero.endswith(".pdf") or fichero.endswith(".docx"):
    print("Documento")
else:
    print("Tipo desconocido")