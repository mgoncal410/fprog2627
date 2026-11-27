# Calcula las plantas de un vivero tras compras, bajas y esquejes.
INVERNADEROS = 5

plantas = int(input("Plantas iniciales: "))
compradas = int(input("Plantas compradas: "))
secas = int(input("Plantas que se secan: "))

plantas += compradas
print("Tras la compra:", plantas)
# Esperaba plantas = 25 y el depurador mostraba plantas = -5
plantas -= secas
print("Tras las bajas:", plantas)
plantas *= 3
print("Tras los esquejes:", plantas)
plantas //= INVERNADEROS
print("En cada invernadero:", plantas)