#Este codigo hace que te va ha pedrir un numero de seguidores iniciales y los nuevos, los q se van, y dependidel valos se simula que has subido un video y que ver los nuevos y los que son bots
#Hecho por Manuel González Calandria el 23/10/2026
inicial = int(input("Seguidores iniciales: "))
nuevos = int(input("Seguidores nuevos: "))
se_van = int(input("Seguidores que se van: "))

tras_nuevos= inicial + nuevos
tras_bajas = tras_nuevos - se_van
tras_video = tras_nuevos *3
bots = (tras_video *50)//100
print("Tras los nuevos:" + str(tras_nuevos))
print("Tras las bajas:" + str(tras_bajas))
print("Tras el video viral:" + str(tras_video))
print("Sin los bots:" + str(bots))