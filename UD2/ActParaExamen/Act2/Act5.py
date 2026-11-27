# Programa: Compara la versión instalada de un programa con la disponible.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Leemos mayor y menor por separado como int (porque 2.10 > 2.9, y como float 2.10 == 2.1)
inst_mayor = int(input("Versión instalada - número mayor: "))
inst_menor = int(input("Versión instalada - número menor: "))
disp_mayor = int(input("Versión disponible - número mayor: "))
disp_menor = int(input("Versión disponible - número menor: "))

print(f"Instalada: {inst_mayor}.{inst_menor} | Disponible: {disp_mayor}.{disp_menor}")

# Caso 1: El número mayor disponible es superior al instalado (ej. 3.0 vs 2.5)
if disp_mayor > inst_mayor:
    print("Actualización IMPORTANTE disponible: haz una copia de seguridad antes.")

# Caso 2: El número mayor es idéntico (ej. 2.7 vs 2.5) -> entramos a mirar el menor (if anidado)
elif disp_mayor == inst_mayor:
    if disp_menor > inst_menor:
        print("Actualización menor disponible")
    elif disp_menor == inst_menor:
        print("El programa está actualizado")
    else:
        print("La versión instalada es más reciente que la publicada")

# Caso 3: El número mayor disponible es inferior al instalado (ej. 2.9 vs 3.0)
else:
    print("La versión instalada es más reciente que la publicada")