LIMITW_AVISO = 90
capcidad_total = float(input("Capacidad total(GB): "))
capacidad_usada = float(input("Espacio usado (GB): "))

porcentaje = capacidad_usada // capcidad_total * 100

print(f"Disco ocupado: {round(porcentaje,1)} %")
#print(f"Disco ocupado: {porcentaje:.if} %")

if porcentaje >= LIMITW_AVISO:
    print("¡Aviso! El disco esta casi lleno")
else:
    print("Queda espacio")