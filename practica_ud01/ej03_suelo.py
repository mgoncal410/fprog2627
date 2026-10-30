#Sirve para calcular lo que te cuesta los metros cuadrados pidiendo el ancho por el largo
#Hecho por Manuel González Calandria el 23/10/2026

largo = float(input("Largo de la habitación (m): "))
ancho = float(input("Ancho de la habitación (m): "))
precio = 12.50
m2 = largo * ancho
m2_rectangulo= (largo * largo) //ancho
precio_m2 = precio * m2
print("Superficie: " +str(m2) , "m2")
print("Coste del suelo:", precio_m2 , "€")
print("Superficie de un rectangulo: " + str(m2_rectangulo) + "m2")