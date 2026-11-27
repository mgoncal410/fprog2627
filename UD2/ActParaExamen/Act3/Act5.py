# Programa: Valida el formato de una IPv4 y la clasifica en loopback, privada o pública.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

PUNTOS_IPV4 = 3

# .strip() limpia espacios al inicio y final, pero respeta espacios intermedios (que son error)
ip = input("Dirección IP: ").strip()

# .count(".") cuenta cuántas veces aparece el punto. Una IPv4 tiene exactamente 3 puntos y 0 espacios
if ip.count(".") != PUNTOS_IPV4 or " " in ip:
    print("Formato no válido")
# .startswith() comprueba el prefijo inicial de la cadena
elif ip.startswith("127."):
    print(f"{ip} es una IP de loopback (el propio equipo)")
elif ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16."):
    print(f"{ip} es una IP privada")
else:
    print(f"{ip} es una IP pública")