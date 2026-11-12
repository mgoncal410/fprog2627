PRECIO_HORAS = 25
HORA_MINIMA=1
DESPLAZAMIENTO=30
IVA=0.21

horas = float(input("Horas de trabajo: "))
contrato = input("¿Tiene contrato de mantenimiento? (S/N)")

horas_facturasdas = max(horas, HORA_MINIMA)

mano_obra = horas_facturasdas * PRECIO_HORAS


if contrato == "S":
    desplazamiento=DESPLAZAMIENTO
else:
    desplazamiento=0

subtotal = (mano_obra+desplazamiento)*IVA
iva=subtotal * IVA
total=subtotal + iva

print(f"Horas facturadas: {horas_facturasdas}")
print(f"Mano de obra: {mano_obra}")
print(f"Desplazamiento: {desplazamiento}")
print(f"Subtotal: {subtotal}")
print(f"IVA ({IVA*100}%): {iva}")
print(f"TOTAL: {total} €")
#if (horas < HORA_MINIMA):
 #   horas_facturasdas=1
#else:
 #   print(horas)