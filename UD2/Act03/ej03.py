ANOS_GARANTIA = 3
años = input("Años del equipo: ")
causa = input("Causa de la averia: ").strip().lower()

if not años >= str(ANOS_GARANTIA) and  not causa==("agua" or "golpe") :
    print("Reparación cubierta por la garantia")
else:
    print("Reperación no cubierta: hay que hacer un presupuesto al cliente")