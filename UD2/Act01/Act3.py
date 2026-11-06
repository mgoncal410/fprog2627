# Calcula cuántas cajas, packs y botellas sueltas salen al empaquetar.
BOTELLAS_PACK = 6
PACKS_CAJA = 4

botellas = int(input("Botellas a empaquetar: "))
botellas_caja = BOTELLAS_PACK * PACKS_CAJA

cajas = botellas // botellas_caja
resto = botellas % botellas_caja
packs = sobran // BOTELLAS_PACK
resto = sobran % BOTELLAS_PACK

print("Cajas completas:", cajas)
print("Packs sueltos:", resto)
print("Botellas sueltas:", sueltas)