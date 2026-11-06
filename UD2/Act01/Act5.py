# Sigue las monedas de un equipo de un videojuego.
PERSONAJES = 5

monedas = input("Monedas iniciales: ")
ganadas = int(input("Monedas ganadas en la partida: "))
gastadas = int(input("Monedas gastadas en la tienda: "))

monedas += ganadas
print("Tras la partida:", monedas)
monedas -= gastadas
print("Tras la tienda:", monedas)
monedas //= PERSONAJES
print("Cada personaje:", monedas)