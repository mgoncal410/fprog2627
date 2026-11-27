# Programa: Muestra el estado de la batería de un portátil según su porcentaje.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Constantes de los límites de batería
BATERIA_MIN = 0
BATERIA_MAX = 100
LIMITE_ALTA = 80
LIMITE_MEDIA = 20
LIMITE_BAJA = 1

bateria = int(input("Batería (%): "))

# En una cascada if-elif-else, Python entra SOLO en la primera condición que sea True.
# 1º Descartamos los valores fuera de rango (< 0 o > 100)
if bateria < BATERIA_MIN:
    print("Valor no válido")
elif bateria > BATERIA_MAX:
    print("Valor no válido")
# 2º Como ya sabemos que es <= 100, basta con comprobar >= 80
elif bateria >= LIMITE_ALTA:
    print("Batería alta")
# 3º Como no entró arriba, ya sabemos que es < 80; basta con comprobar >= 20
elif bateria >= LIMITE_MEDIA:
    print("Batería media")
# 4º Ya sabemos que es < 20; basta con comprobar >= 1
elif bateria >= LIMITE_BAJA:
    print("Batería baja: conecta el cargador")
# 5º El único valor válido que queda por descarte es 0
else:
    print("Batería agotada: apagando el equipo")