# Programa: Calculadora básica para dos números usando match-case.
# Autor: Manuel González Calandria
# Fecha: 27/11/2026

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /, **): ")

# Comparamos el símbolo introducido contra las operaciones permitidas
match operacion:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    # La barra vertical '|' permite agrupar varios valores válidos en un mismo case
    case "*" | "x" | "X":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        # Dentro de un case podemos meter un if normal para evitar dividir entre 0
        if num2 == 0:
            print("Error: no se puede dividir entre 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    case "**":
        print(f"{num1} ** {num2} = {num1 ** num2}")
    case _:
        # Si escribió cualquier otro texto o símbolo
        print("Operación no válida")