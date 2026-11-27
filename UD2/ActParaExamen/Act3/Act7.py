# Programa: Asigna departamento y prioridad a un ticket de soporte técnico.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

# Guardamos el texto original (limpiando espacios extremos) para poder usar .isupper() luego
descripcion_original = input("Describe el problema: ").strip()
# Creamos una copia en minúsculas para buscar palabras clave sin importar cómo se escribieron
descripcion = descripcion_original.lower()

# Primer bloque: decide el departamento en el orden exacto de prioridad de la tabla
if "contraseña" in descripcion or "usuario" in descripcion:
    departamento = "Cuentas de usuario"
elif "impresora" in descripcion or "tóner" in descripcion:
    departamento = "Periféricos"
elif "internet" in descripcion or "wifi" in descripcion or "conexión" in descripcion:
    departamento = "Redes"
else:
    departamento = "Soporte general"

# Segundo bloque independiente: decide la prioridad
# .isupper() devuelve True si TODAS las letras del texto original estaban en mayúsculas ("GRITANDO")
if "urgente" in descripcion or descripcion_original.isupper():
    prioridad = "ALTA"
else:
    prioridad = "normal"

print(f"Departamento: {departamento}")
print(f"Prioridad: {prioridad}")