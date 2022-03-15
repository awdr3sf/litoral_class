#Pedir un voto de 3 candidatos
print("[A] Candidato partido azul")
print("[B] Candidato partido verde")
print("[C] Candidato partido rojo")
#Variables de candidatos
candidato_1 = "a"
candidato_1 = "b"
candidato_1 = "c"
voto = input("Elegir uno de los 3 candidatos escribir una de las 3 letras : ")
voto = voto.lower()
if voto.isascii:
    if voto == "a":
        print("Usted eligio el candidato [A] Partido AZUL")
    elif voto == "b":
        print("Usted eligio el candidato [B] Partido Amarillo")     
    elif voto == "c":
        print("Usted eligio el candidato [C] Partido Rojo") 
if voto.isnumeric:
    print("Usted Eligio un valor numerico porfavor eliga una letra correspondiente a los candidatos")
    #Codigo hecho por Andres Camacho :V









