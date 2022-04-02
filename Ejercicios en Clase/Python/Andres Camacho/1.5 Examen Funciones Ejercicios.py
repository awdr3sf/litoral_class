# realizar el siguiente ejercicio en python de obtener valor de x

def valorx():
    print(5+4*3)
    print(4*5+(5-3))
    print(4+3*3**4*(7-5))
    print(4+7*3**3*(10-5)/2)
    print(15/3*(7+(68-2*33+(25**2/5)/3)/2)+19)

def imc():
    peso = int(input("Digitar tu peso"))
    estatura = float(input("Digitar tu estatura"))
    imc = peso/estatura**2
    print("Tu peso es de : ",peso,"Tu altura es de : ",estatura, "IMC Es de : ",round(imc,2))

def notas():
    nota1 = float(input("Digitar primera nota : "))
    nota2 = float(input("Digitar segunda nota : "))
    nota3 = float(input("Digitar tercera nota : "))
    nota4 = float(input("Digitar cuarta nota : "))
    promedio = (nota1+nota2+nota3+nota4) / 4
    promedio1 = round(promedio, 2)
    if promedio1 >0 and promedio1 <2.9:
        print("Usted reporobo con un promedio de : ",promedio1)
    elif promedio1 <= 3 and promedio1 < 3.5:
        print("Usted paso con un promedio regular de : ",promedio1)
    elif promedio1 <= 3.6 and promedio1 < 4.0:
        print("Usted paso con un promedio bueno de : ",promedio1)
    elif promedio1 <= 4.1 and promedio1 < 4.5:
        print("Usted paso con un promedio Muy Bueno de : ",promedio1)
    elif promedio1 <= 4.6 and promedio1 < 5.0:
        print("Usted paso con un promedio excelente de : ",promedio1)

def resultadoentero():
    numero1 = int(input("Digitar primer numero : "))
    numero2 = int(input("Digitar primer numero : "))
    resultado = numero1//numero2
    resultado2 = numero1/numero2
    print("El numero entero de divisor es : ",resultado, " y el numero total es de : ",resultado2)

#valorx()
#img()
notas()
#resultadoentero()



