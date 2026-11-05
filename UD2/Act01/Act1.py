# Muestra el número de versión de un programa en tres formatos.
mayor = input("Versión mayor: ")
menor = input("Versión menor: ")
parche = input("Parche: ")

version = mayor + "." + menor + "." + parche
etiqueta = "v" + version
largo = "versión " + mayor + ", revisión " + menor + ", parche " + parche 

print("Versión:", version)
print("Etiqueta de Git:", etiqueta)
print("Formato largo:", largo)
#El error esta en la linea 8 que en vez de poner parche en el final a puesto dos veces menor