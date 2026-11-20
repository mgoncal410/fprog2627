LONGITUD_CP=5

codigo = input("DIme tu numero postal: ").strip()

if len(codigo) == LONGITUD_CP and codigo.isdigit():
    print("Codigo postal valido")
    if codigo.startswith("41"):
        print("Codigo postal de Sevilla")
else:
    print("Codigo postal no valido")