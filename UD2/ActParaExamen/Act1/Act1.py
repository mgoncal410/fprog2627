# Muestra el número de versión de un programa en tres formatos.
mayor = input("Versión mayor: ")
menor = input("Versión menor: ")
parche = input("Parche: ")

version = mayor + "." + menor + "." + parche
etiqueta = "v" + version
# Esperaba largo = 'versión 2, revisión 15, parche 3' y el depurador mostraba largo = 'versión 2, revisión 15, parche 15'
largo = "versión " + mayor + ", revisión " + menor + ", parche " + parche

print("Versión:", version)
print("Etiqueta de Git:", etiqueta)
print("Formato largo:", largo)