#ESte codigo simula un almacén, y tu le tiens q poner la seccion en el que esta junto al pasillo y estante.
#Este codigo esta hecho por Manuel González Calandria el 30/10/2026
seccion = input("Sección: ")
pasillo = input("Pasillo: ")
estante = input("Estante: ")

print("Etiqueta: " +seccion,pasillo,estante, sep="-")
print("Ruta: " +seccion,pasillo,estante, sep="/")
print("Formato largo:" , "sección", str(seccion) + "," , "pasillo", str(pasillo) + "," , "estante" ,estante )