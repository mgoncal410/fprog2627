# Muestra el recibo de un taxi y lo divide entre las personas que lo comparten.
BANDERA = 3.5
PRECIO_KM = 1.2
PRECIO_MALETA = 0.5

distancia = float(input("Kilómetros recorridos: "))
maletas = int(input("Maletas: "))
personas = int(input("Personas que comparten el taxi: "))

# Esperaba coste_km = 12.0 y el depurador mostraba coste_km = 11.2
coste_km = distancia * PRECIO_KM
coste_maletas = maletas * PRECIO_MALETA
# Esperaba total = 16.5 y el depurador mostraba total = 17.5
total = BANDERA + coste_km + coste_maletas

print("=" * 30)
print("RECIBO DEL TAXI")
print("=" * 30)
print(f"Kilómetros:\t{distancia} km")
print(f"Maletas:\t{maletas}")
print(f"Bajada bandera:\t{BANDERA:.2f} €")
print(f"Coste km:\t{coste_km:.2f} €")
print(f"Coste maletas:\t{coste_maletas:.2f} €")
print("-" * 30)
print(f"TOTAL:\t\t{total:.2f} €")
print(f"Cada persona:\t{total / personas:.2f} €")