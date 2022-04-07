""" 
NOTA: este es un enunciado diferente al del reto, pero es muy similar, por lo que les servira para realizarlo

El equipo de futbol de la ciudad aspira clasificar al campeonato internacional, 
pero de no quedar podría entrar a uno de los campeonatos en el país dependiendo los puntos que tengan
en 2021 y en 2022. 

En la siguiente tabla están los puntos de clasificación para cada campeonato:
_______________________________________________________________________________________________
|Puntos 2021 | Puntos 2022 | Campeonato    | Fecha|
_______________________________________________________________________________________________
| < 52       | < 45        | municipal     | 1    |
_______________________________________________________________________________________________
| [52 - 75)  | [45 - 53]   | departamental | 2    |
_______________________________________________________________________________________________
| [75 - 110) | [53 - 71]   | Nacional      | 3    |
_______________________________________________________________________________________________
| >= 110     | >= 71       | Internacional | 4    |
_______________________________________________________________________________________________

Además, para cualquier combinación no válida de los puntos de ambas fechas se
debe mostrar el mensaje “No se puede determinar el campeonato”, así como una fecha de
valor 0.

Entrada Esperada
51 40
71 50
120 80
180 103

Salida Esperada

Municipal Fecha 1
Departamental Fecha 2
Internacional Fecha 4
No se puede determinar el campeonato Fecha 0 """

puntos21 = int(input("Digite los puntos obtenidos en 2021: "))# aqui pedimos los puntos de 2021
puntos22 = int(input("Digite los puntos obtenidos en 2022: "))# aqui los de 2022

#Condicionales que evaluan los puntos ---------------------------------------------⮯
if puntos21 < 52 and puntos22 < 45:
    print("Municipal Fecha 1")
elif puntos21 >= 52 and puntos21 < 75 and puntos22 >= 45 and puntos22 <=53:
#utilizamos el operador logico and para que entre al ciclo si y solo si todas las condiciones se cumplen.
    print("Departamental Fecha 2")
elif puntos21 >= 75 and puntos21 < 110 and puntos22 >= 53 and puntos22 <=71:
    print("Nacional Fecha 3")
elif puntos21 >= 110 and  puntos22 >= 71:
    print("Internacional Fecha 4")
else:
    print("No se puede determinar el campeonato Fecha 0")
#------------------------------------------------------------------------------------⮭