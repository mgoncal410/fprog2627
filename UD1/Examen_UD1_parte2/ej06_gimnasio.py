#Este codigo sirbe para calcular lo que pagarias por el gimnasio
#Este codigo esta hecho por Manuel González Calandria el 30/10/2026
mes = int(input("Meses contratados: "))
clase = int(input("Clases dirigidas extra: "))
matricula = 20
cuota = 30
clase_ex = 4
pagar_mes = mes*cuota
pagar_clase = clase*clase_ex
total= pagar_clase + pagar_mes + matricula
media= (total - matricula)/5
print("="*20)
print("RECIBO DEL GIMNASIO")
print("="*20)
print("Meses:\t", mes)
print("Clases extra:\t", clase)
print("Matrícula:\t", matricula , "€")
print("Cuotas:\t", pagar_mes , "€" )
print("Coste clases:\t", pagar_clase, "€")
print("-"*20)
print("TOTAL:\t\t", total, "€")
print("Media al mes:\t", media, "€")