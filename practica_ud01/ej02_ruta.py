#Te pide tras paradas de autobuses y te dice cual es el recorrido de ida y buelta dependiendo de en que paradas este
#Hecho por Manuel González Calandria el 23/10/2026
primer_bus = input("Primera parada: ")
segundo_bus = input("Segunda parada: ")
tercer_bus = input("Tercera parada: ")

print("="*20)
print("Ida:" , primer_bus, "->", segundo_bus, "->", tercer_bus)
print("="*20)
print("Vuelta:" , tercer_bus , "->", segundo_bus, "->", primer_bus)
print("="*20)