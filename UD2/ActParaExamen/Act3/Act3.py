# Programa: Comprueba si la reparación de un portátil entra en garantía.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

ANIOS_GARANTIA = 3

anios = int(input("Años del equipo: "))
causa = input("Causa de la avería: ").strip().lower()

# Leemos la condición paso a paso:
# 1. anios < 3  --> tiene menos de 3 años
# 2. ("golpe" in causa or "agua" in causa) --> aparece alguna palabra prohibida
# 3. not (...)  --> negamos lo anterior: NO aparece ni golpe ni agua
# 4. and        --> deben cumplirse las dos cosas a la vez
if anios < ANIOS_GARANTIA and not ("golpe" in causa or "agua" in causa):
    print("Reparación cubierta por la garantía")
else:
    print("Reparación no cubierta: hay que hacer un presupuesto al cliente")