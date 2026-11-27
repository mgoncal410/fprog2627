# Muestra el porcentaje de votos de cada candidatura con una barra.
ana = int(input("Votos de Ana: "))
luis = int(input("Votos de Luis: "))
marta = int(input("Votos de Marta: "))

# Esperaba total = 100 y el depurador mostraba total = 80
total = ana + luis + marta
p_ana = ana * 100 // total
# Esperaba p_luis = 30 y el depurador mostraba p_luis = 0
p_luis = luis * 100 // total
p_marta = marta * 100 // total

print("Ana:\t[" + "#" * (p_ana // 10) + "." * (10 - p_ana // 10) + "] " + str(p_ana) + " %")
print("Luis:\t[" + "#" * (p_luis // 10) + "." * (10 - p_luis // 10) + "] " + str(p_luis) + " %")
print("Marta:\t[" + "#" * (p_marta // 10) + "." * (10 - p_marta // 10) + "] " + str(p_marta) + " %")
print("Total de votos:", total)