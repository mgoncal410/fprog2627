#Este codigo pide los m de un lado de un deposito y el codigo calculas los litros que caben, el volumen y la superficie a pintar
#Este codigo esta hecho por Manuel González Calandria el 30/10/2026
metros = float(input("Lado del depósoto (m): "))
volumen = metros * metros * metros
capacidad = volumen * (metros *1000)
superficie = 6 * (metros * metros)

print("Volumen:", volumen, "m3")
print("Capacidad:", capacidad , "litros")
print("Superficie a pintar:", superficie , "m2")
