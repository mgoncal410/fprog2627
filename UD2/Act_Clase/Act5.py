fichero = input("Indica el nombre del fichero: ").strip().lower()

if fichero.endswith(".png") or fichero.endswith(".jpg"):
    print("Es una imagen")
else:
    print("No es una imagen")