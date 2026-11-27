# Programa: Clasifica un puerto de red e identifica el servicio si es bien conocido.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Constantes con los rangos oficiales de puertos TCP/UDP
PUERTO_MIN = 0
MAX_BIEN_CONOCIDO = 1023
MAX_REGISTRADO = 49151
PUERTO_MAX = 65535

puerto = int(input("Número de puerto: "))

# Primero filtramos los puertos imposibles (< 0 o > 65535)
if puerto < PUERTO_MIN:
    print("Puerto no válido")
elif puerto > PUERTO_MAX:
    print("Puerto no válido")
# Si llega aquí, está entre 0 y 65535. Comprobamos si es <= 1023
elif puerto <= MAX_BIEN_CONOCIDO:
    print("Puerto bien conocido")
    # match-case evalúa el valor exacto de 'puerto' contra cada 'case'
    match puerto:
        case 21:
            print("Servicio: FTP")
        case 22:
            print("Servicio: SSH")
        case 53:
            print("Servicio: DNS")
        case 80:
            print("Servicio: HTTP")
        case 443:
            print("Servicio: HTTPS")
        case _:
            # 'case _:' es el caso por defecto (como un 'else') si no coincide ninguno
            print("Servicio: otro")
# Si no era <= 1023 pero es <= 49151, es registrado
elif puerto <= MAX_REGISTRADO:
    print("Puerto registrado")
# Si llega aquí, está entre 49152 y 65535
else:
    print("Puerto dinámico")