tipo=input("Nombre del fichero: ").strip().lower()

if tipo.endswith(".png"".jpg"".pdf"".docx"".py"):
    if tipo.endswith(".png"".jpg"):
        print("Imagen")
        if tipo.endswith(".pdf"".docx"):
            print("Documento")
            if tipo.endswith(".py"):
                print("Script de Python")
else:
    print("El fichero no tiene extensión")