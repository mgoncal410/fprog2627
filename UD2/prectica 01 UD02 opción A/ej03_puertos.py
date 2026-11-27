
modo = input("Modo del puerto (acceso, troncal o apagado): ")


if modo == "Acceso":
    vlan=int(input("VLAN del puerto: "))
elif vlan < 4095:
    print(f"Puerto en modo acceso en la VLAN {vlan}")
elif vlan >= 5000:
    print(f"Error: la VLAN tiene que estar entre 1 y 4094")
