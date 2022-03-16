#Pedir un voto de 3 candidatos

#MANDAMOS 3 MENSAJES CON LAS 3 LETRAS A ELEGIR DE LOS CANDIDATOS
print("[A] Candidato partido azul")
print("[B] Candidato partido verde")
print("[C] Candidato partido rojo")

#Variables de candidatos
#AQUI COLOCAREMOS LA VARIABLE Y LE ASIGNAREMOS UN INPUT PARA GUARDAR LA LETRA
voto = input("Elegir uno de los 3 candidatos escribir una de las 3 letras : ")
#CONVERTIREMOS LOS VALORES PARA SIEMPRE RECIBIR EN MINUSCULA
voto = voto.lower()

#CONDICIONAL PARA QUE SOLO SE EJECUTE EL PROGRAMA SIEMPRE Y CUANDO SEA UNA LETRA RECIBIDA EN EL INPUT DENTRO DE LA VARIABLE "VOTO"
if voto.isascii:
    #AQUI EMPIEZA LAS CONDICIONALES Y COMPARAREMOS CON LETRAS QUE DESEAMOS COLOCAR EN LOS CANDIDATOS
    if voto == "a":
        print("Usted eligio el candidato [A] Partido AZUL")
    elif voto == "b":
        print("Usted eligio el candidato [B] Partido Amarillo")     
    elif voto == "c":
        print("Usted eligio el candidato [C] Partido Rojo") 
if voto.isnumeric:
    print("Usted Eligio un valor numerico porfavor eliga una letra correspondiente a los candidatos")
    #Codigo hecho por Andres Camacho :V









