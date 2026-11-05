DESCUENTO = 15    # porcentaje
precio = float(input("Precio: "))
#final = precio - precio * DESCUENTO
final = precio - (precio * DESCUENTO/100)
print(f"Precio final: {final:.2f} €")