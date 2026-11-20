LONGITUD_MAC=17
SEPARADORES=5

mac = input("Dime la direccion MAC: ").strip()

if len(mac) == LONGITUD_MAC and mac.count(";") == SEPARADORES:
    print("Formato de la dirrecion correcta")
else:
    print("Formato no valido")