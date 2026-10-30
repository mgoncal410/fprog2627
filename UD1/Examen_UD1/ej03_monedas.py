#Este codigo es para ver las monedas que tienes al principio y contando con unos gastos y lo que repartes, y tambien lo que ganas pon un evento
#Este codigo esta hecho por Manuel González Calandria el 30/10/2026
monedas = int(input("Monedas iniciales: "))
monedas_partida= int(input("Monedas ganadas en la aprtida: "))
monedas_tienda = int(input("Monedas gastadas en la tienda: "))
monedas += monedas_partida
print("Tras la partida:", monedas)
monedas -= monedas_tienda
print("Tras la tienda:", monedas)
monedas *= 3
print("Tras el evento triple:", monedas)
monedas //= 5
print("Cada personaje:", monedas)




