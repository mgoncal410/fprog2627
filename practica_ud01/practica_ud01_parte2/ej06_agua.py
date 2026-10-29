#Este codigo es para el recibo del agua, te pide lo que has cosumido en el mes y cuantas personas, y luego hace un calculo y te saca el total a pagar
#Hecho por Manuel González Calandria el 23/10/2026
metros = int(input("Metros cúbicos consumidos: "))
personas = int(input("Personas en la casa: "))
cuota = 8
litros= metros * 1000
coste = metros *2
total = coste + cuota
cada_persona = total / personas

print("="*30)
print("RECIBO DEL AGUA")
print("="*30)
print("Consumo:\t" , metros , "m3")
print("En litros:\t" , litros , "litros")
print("Cuota fija:\t" , cuota , "€" )
print("Coste consumo:\t" , coste , "€")
print("-"*30)
print("TOTAL:\t\t"  , total , "€")
print("Cada persona:\t" , cada_persona , "€")



