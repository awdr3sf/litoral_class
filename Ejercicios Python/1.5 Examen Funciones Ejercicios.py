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
    nota2 = float(input("Digitar primera nota : "))
    nota3 = float(input("Digitar primera nota : "))
    nota4 = float(input("Digitar primera nota : "))
    promedio = (nota1+nota2+nota3+nota4) / 4
    print("tu promedio es de : ",promedio)
    if promedio >0 and promedio <2.9:
        print("Usted reporobo con un promedio de : ",round(promedio,2))
    elif promedio == 3 and promedio < 3.5:
        print("Usted paso con un promedio regular de : ",round(promedio,2))
    elif promedio == 3.6 and promedio < 4.0:
        print("Usted paso con un promedio bueno de : ",round(promedio,2))
    elif promedio == 4.1 and promedio < 4.5:
        print("Usted paso con un promedio Muy Bueno de : ",round(promedio,2))
    elif promedio == 4.6 and promedio < 5.0:
        print("Usted paso con un promedio excelente de : ",round(promedio,2))

def resultadoentero():
    numero1 = int(input("Digitar primer numero : "))
    numero2 = int(input("Digitar primer numero : "))
    resultado = numero1//numero2
    resultado2 = numero1/numero2
    

    print("El numero entero de divisor es : ",resultado, "y el numero total es de : ",resultado2)





