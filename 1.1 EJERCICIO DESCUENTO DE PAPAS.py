# VALOR A RECIBIR
variable_kilos = float(input("Cuantos kilos de papa desea "))
# VARIABLES DE CALCULO
    # VARIABLE PARA ALMACENAR EL VALOR DEL KILO
variable_valorkilos = 2500
    # VARIABLE PARA MULTIPLICAR LOS KILOS POR EL VALOR DEL KILO
variable_valorporkilos = variable_kilos * variable_valorkilos
# VARIABLES PARA DESCUENTO
    #variable_5kilos = variable de valor de descuento por 5 kilos y descuento de 3 %
    #variable_1kilos = variable de valor de descuento por 10 kilos y descuento de 5 %
    #variable_15kilos = variable de valor de descuento por 15 kilos y descuento de 7 %
    #variable_20kilos = variable de valor de descuento por 20 kilos y descuento de 10 %
variable_5kilos = variable_valorporkilos  * 0.03
variable_10kilos = variable_valorporkilos  * 0.05
variable_15kilos = variable_valorporkilos  * 0.07
variable_20kilos = variable_valorporkilos  * 0.10
#VARIABLE PARA RESTAR DESCUENTO
    #variable_total5kilos = variable para restar el valor de descuento entre la variable "v_vdpxk2 y variable_5kilos" por 5 kilos y descuento de 3 %
    #variable_total10kilos = variable para restar el valor de descuento entre la variable "variable_valorporkilos y variable_10kilos" por 10 kilos y descuento de 5 %
    #variable_total15kilos = variable para restar el valor de descuento entre la variable "variable_valorporkilos y variable_15kilos" por 15 kilos y descuento de 7 %
    #variable_total20kilos = variable para restar el valor de descuento entre la variable "variable_valorporkilos y variable_20kilos" por 20 kilos y descuento de 10 %
variable_total5kilos =  variable_valorporkilos  - variable_5kilos
variable_total10kilos = variable_valorporkilos  - variable_10kilos
variable_total15kilos = variable_valorporkilos  - variable_15kilos
variable_total20kilos = variable_valorporkilos  - variable_20kilos
# COMPARACIONES E IMPRIMIR EN PANTALLA
    # CONDICIONAL PARA QUE SEA MAYOR A 5 KILOS Y OBTENGA UN DESCUENTO DEL 3% PERO MENOR A 10 KILOS
if variable_kilos >= 5 and variable_kilos < 10:
    print("Usted compro ",variable_kilos, " Kilos De Papa con un valor de ",(int(variable_valorporkilos)),"y obtuvo un descuento de ",(int(variable_5kilos))," Pesos y un total de ",(int(variable_total5kilos))," con descuento")
    # CONDICIONAL PARA QUE SEA MAYOR A 10 KILOS Y OBTENGA UN DESCUENTO DEL 5% PERO MENOR A 15 KILOS
elif variable_kilos >= 10 and variable_kilos < 15:
    print("Usted compro ",variable_kilos, " Kilos De Papa con un valor de ",(int(variable_valorporkilos)),"y obtuvo un descuento de ",(int(variable_10kilos))," Pesos y un total de ",(int(variable_total5kilos))," con descuento")
    # CONDICIONAL PARA QUE SEA MAYOR A 15 KILOS Y OBTENGA UN DESCUENTO DEL 7% PERO MENOR A 20 KILOS
elif variable_kilos >= 15 and variable_kilos < 20:
    print("Usted compro ",variable_kilos, " Kilos De Papa con un valor de ",(int(variable_valorporkilos)),"y obtuvo un descuento de ",(int(variable_15kilos))," Pesos y un total de ",(int(variable_total5kilos))," con descuento")
    # CONDICIONAL PARA QUE SEA MAYOR A 20 KILOS Y OBTENGA UN DESCUENTO DEL 10% 
elif variable_kilos >= 20:
    print("Usted compro ",variable_kilos, " Kilos De Papa con un valor de ",(int(variable_valorporkilos)),"y obtuvo un descuento de ",(int(variable_20kilos))," Pesos y un total de ",(int(variable_total5kilos))," con descuento")
# ESTO ES PARA QUE SALGA UN MENSAJE SI DIGITA UN VALOR DE KILO IGUAL O QUE NO ESTE EN LOS KILOS ESTABLECIDOS    
else:
    print("Usted ingreso un valor fuera de nuestros descuentos")

