# Calcula la superficie a barnizar y el ribete de una mesa redonda.
PI = 3.1416

radio = float(input("Radio de la mesa (m): "))
# Esperaba superficie = 7.0686 y el depurador mostraba superficie = 22.20660996
superficie = PI * (radio ** 2)
borde = 2 * PI * radio

print(f"Superficie a barnizar: {superficie:.2f} m²")
print(f"Ribete del borde: {borde:.2f} m")