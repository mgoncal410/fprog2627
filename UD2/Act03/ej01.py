usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

admin="admin"
fprog2627="fprog2627"

if usuario.lower() == admin and contraseña.strip() == fprog2627:
    print("Acceso concedido")
else:
    print("Usuario y contraseña incorrecto")