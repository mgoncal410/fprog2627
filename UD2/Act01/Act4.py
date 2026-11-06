# Calcula la superficie a barnizar y el ribete de una mesa redonda.
PI = 3.1416

radio = float(input("Radio de la mesa (m): "))
superficie = PI * (radio ** 2) #El problemas es que el el radio tiene qus estar elevado a 2, y estaba fuera del parentesis, y lo que estaba haciendo es elevar a dos el resultado de pi por radio 
borde = 2 * PI * radio

print(f"Superficie a barnizar: {superficie:.2f} m²")
print(f"Ribete del borde: {borde:.2f} m")