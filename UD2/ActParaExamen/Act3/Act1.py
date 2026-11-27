# Programa: Valida el inicio de sesión de un usuario mediante constantes.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "Fprog2627"

# .strip() quita espacios delante y detrás; .lower() ignora mayúsculas/minúsculas
usuario = input("Usuario: ").strip().lower()
# En la contraseña NO usamos .lower() ni .strip() porque debe ser exacta
contrasena = input("Contraseña: ")

# 'and' exige que AMBAS condiciones sean True a la vez
if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")