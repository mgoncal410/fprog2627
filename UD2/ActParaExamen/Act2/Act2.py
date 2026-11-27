# Programa: Calcula la factura desglosada de una reparación informática a domicilio.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Constantes de tarifas e impuestos
PRECIO_HORA = 25.0
HORAS_MINIMAS = 1.0
PRECIO_DESPLAZAMIENTO = 30.0
IVA = 0.21

horas = float(input("Horas de trabajo: "))
# .lower() pasa la respuesta a minúsculas por si el usuario escribe "S" o "N"
contrato = input("¿Tiene contrato de mantenimiento? (s/n): ").lower()

# max() devuelve el mayor de los dos números: si horas es 0.5, elige 1.0 (HORAS_MINIMAS)
horas_facturadas = max(horas, HORAS_MINIMAS)
mano_obra = horas_facturadas * PRECIO_HORA

# Si tiene contrato ("s"), el desplazamiento es gratis (0.0); si no, son 30.0 €
if contrato == "s":
    desplazamiento = 0.0
else:
    desplazamiento = PRECIO_DESPLAZAMIENTO

# Cálculos finales de la factura
subtotal = mano_obra + desplazamiento
importe_iva = subtotal * IVA
total = subtotal + importe_iva

# :.2f formatea todos los importes en euros con exactamente 2 decimales
print(f"Horas facturadas: {horas_facturadas:.1f}")
print(f"Mano de obra: {mano_obra:.2f} €")
print(f"Desplazamiento: {desplazamiento:.2f} €")
print(f"Subtotal: {subtotal:.2f} €")
print(f"IVA (21 %): {importe_iva:.2f} €")
print(f"TOTAL: {total:.2f} €")