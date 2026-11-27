MIN_CARACTER = 17
SEPARADORES =5
mac = input("Dirrección MAC: ").strip().isupper()

if not mac.count(":") == SEPARADORES or " " in mac:
    print(f"{mac} es una MAC valida")
elif mac == "ff:ff:ff:ff:ff:ff":
    print("Es una MAC de difusión")
elif mac.startswith("00:50:56"):
    print(f"{mac} es una tarjeta de red virtual de VMware")
else:
    print(f"Error: la MAC tiene que tener {SEPARADORES} separadores ':'")



