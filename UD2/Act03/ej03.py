ANOS_GARANTIA = 3
años = input("Años del equipo: ")
causa = input("Causa de la averia: ").strip().lower()

if años >= ANOS_GARANTIA and "agua" and "golpe" not in causa :
    print("Reparación cubierta por la garantia")
else:
    print("Reperación no cubierta: hay que hacer un presupuesto al cliente")