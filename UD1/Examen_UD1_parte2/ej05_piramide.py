
#Este codigo esta hecho por Manuel González Calandria el 30/10/2026
caracte = input("Caracter: ")
tamaño = int(input("Tamaño del bloque: "))
print(" " * tamaño*3,caracte * tamaño + "\n",
      " " * tamaño*2,caracte * tamaño *3 + "\n",
      " " * tamaño, caracte * tamaño * 5 + "\n",
      caracte * tamaño *7 )