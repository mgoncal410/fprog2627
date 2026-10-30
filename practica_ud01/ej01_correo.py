#Este programa pide un usuario, el nombre de una empresa y una extensión y cuando tu la pones te da la web bien puesta con su www y la extension que has puesto, igual con el usuario q te lo pondria como un email
#Hecho por Manuel González Calandria el 23/10/2026
nombre = input("Usuario: ")
empresa = input("Empresa: ")
extension= input("Extensión del dominio: ")

print("Correo:" , nombre + "@" + empresa + extension)
print("Web: www" , empresa , extension, sep=".")
print("Carpeta personal: " , "home", nombre , sep="/")