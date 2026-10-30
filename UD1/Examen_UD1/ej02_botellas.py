#Este codigo calcula las cajas de botellas, tambien calcula las que se pierden y las que estan en pack sueltos
#Este codigo esta hecho por Manuel González Calandria el 30/10/2026
botella = int(input("Botellas a empaquetar: "))
pack = 6
caja = 4
botellas_pack = botella // pack
resto = botella // pack
botella_suelta =  resto // pack
botellas_caja = botellas_pack // caja
print("Cajas completas:" , botellas_caja)
print("Botellas sueltas:" ,  botella_suelta )
print("Packs sueltos:" , )