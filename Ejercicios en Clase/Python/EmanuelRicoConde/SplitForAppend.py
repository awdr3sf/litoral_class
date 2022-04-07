 
# Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: 
# si el promedio global obtenido por un alumno en el último periodo es mayor o igual que 4, 
# se le hará un descuento del 30% sobre la matrícula y no se le cobrará IVA; si el promedio obtenido 
# es menor que 4 deberá pagar la matrícula completa, la cual debe incluir el 12% de IVA.

# Hacer un algoritmo que calcule el valor a pagar si se conocen las notas finales de las 4 materias # que cursaron. Asuma que el valor de la matricula es de $5.000.000  

notas = input("Digite las 4 notas: ").split(",")

# La funcion split(), toma una cadena de caracteres (string) y la pasa a una lista. 
# Por defecto el separador es cada espacio en blanco, pero se puede seleccionar cualquier separador. 
# por ejemplo: .split(",") aqui le estamos diciendo que agregue a la lista cada dato que este separado por coma.

nuevaListaDeNotas = [] #lista vacia

# Una lista en Python es una estructura de datos formada por una secuencia ordenada de objetos. 
# Los elementos de una lista pueden accederse mediante su índice, siendo 0 el índice del primer elemento. 

descuento = 0
iva = 0.12
matricula = 5000000
valorIva = 0
totalPagar = 0

for i in range(len(notas)): #ciclo para o for
    nuevaListaDeNotas.append(float(notas[i])) #funcion append()

# El ciclo Para o For en Python nos ayuda a ejecutar dentro de un rango (range) determinado de iteraciones.
# La función len() devuelve la longitud de la lista (su cantidad de elementos dentro).

# La funcion append(x) Agrega cualquier valor completo al final de una lista, 
# por ejemplo: si enviamos un objeto, agrega el objeto, si enviamos una lista, 
# agrega la lista completa en lugar de sus elementos

# es decir con append agregamos las notas convertidas en el ciclo for a la nueva lista.

promedio = (nuevaListaDeNotas[0] + nuevaListaDeNotas[1] + nuevaListaDeNotas[2] + nuevaListaDeNotas[3]) / len(nuevaListaDeNotas)

if promedio >= 4:
    descuento = 0.3 * matricula
    totalPagar = matricula - descuento
elif promedio < 4:
    valorIva = matricula * iva
    totalPagar = valorIva + matricula

print(f"""
------------------------------------------
Su promedio es de {promedio}
------------------------------------------
Debe pagar iva de {valorIva}
------------------------------------------
Tiene un descuento de {descuento}
------------------------------------------
El valor de la matricula es {totalPagar}
------------------------------------------
""") 

# La f que esta antes de las comillas o la leyenda del print es un metodo para dar formato a dicha salida,
# con esto podemos poner varias varibles y en el orden que queramos, existen otros metodos pero este es el mas sencillo.
