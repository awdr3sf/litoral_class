# VALOR A RECIBIR
v_papasxkilos = float(input("Cuantos kilos de papa desea "))
# VARIABLES DE CALCULO
    # VARIABLE PARA ALMACENAR EL VALOR DEL KILO
v_vdpxk = 2500
    # VARIABLE PARA MULTIPLICAR LOS KILOS POR EL VALOR DEL KILO
v_vdpxk2 = v_papasxkilos * v_vdpxk
# VARIABLES PARA DESCUENTO
    #v_vdpx5kd = variable de valor de descuento por 5 kilos y descuento de 3 %
    #v_vdpx10kd = variable de valor de descuento por 10 kilos y descuento de 5 %
    #v_vdpx15kd = variable de valor de descuento por 15 kilos y descuento de 7 %
    #v_vdpx20kd = variable de valor de descuento por 20 kilos y descuento de 10 %
v_vdpx5kd = v_vdpxk2  * 0.03
v_vdpx10kd = v_vdpxk2  * 0.05
v_vdpx15kd = v_vdpxk2  * 0.07
v_vdpx20kd = v_vdpxk2  * 0.10
#VARIABLE PARA RESTAR DESCUENTO
    #v_vdpx5kd = variable para restar el valor de descuento entre la variable "v_vdpxk2 y v_vdpx5kd" por 5 kilos y descuento de 3 %
    #v_vdpx5kd = variable para restar el valor de descuento entre la variable "v_vdpxk2 y v_vdpx10kd" por 10 kilos y descuento de 5 %
    #v_vdpx5kd = variable para restar el valor de descuento entre la variable "v_vdpxk2 y v_vdpx15kd" por 15 kilos y descuento de 7 %
    #v_vdpx5kd = variable para restar el valor de descuento entre la variable "v_vdpxk2 y v_vdpx20kd" por 20 kilos y descuento de 10 %
v_vdpx5kd2 =  v_vdpxk2  - v_vdpx5kd
v_vdpx10kd2 = v_vdpxk2  - v_vdpx10kd
v_vdpx15kd2 = v_vdpxk2  - v_vdpx15kd
v_vdpx20kd2 = v_vdpxk2  - v_vdpx20kd
# COMPARACIONES E IMPRIMIR EN PANTALLA
    # CONDICIONAL PARA QUE SEA MAYOR A 5 KILOS Y OBTENGA UN DESCUENTO DEL 3% PERO MENOR A 10 KILOS
if v_papasxkilos >= 5 and v_papasxkilos < 10:
    print("Usted compro ",v_papasxkilos, " Kilos De Papa con un valor de ",v_vdpxk2,"y obtuvo un descuento de ",(int(v_vdpx5kd))," Pesos y un total de ",v_vdpx5kd2," con descuento")
    # CONDICIONAL PARA QUE SEA MAYOR A 10 KILOS Y OBTENGA UN DESCUENTO DEL 5% PERO MENOR A 15 KILOS
elif v_papasxkilos >= 10 and v_papasxkilos < 15:
    print("Usted compro ",v_papasxkilos, " Kilos De Papa con un valor de ",v_vdpxk2,"y obtuvo un descuento de ",(int(v_vdpx10kd))," Pesos y un total de ",v_vdpx10kd2," con descuento")
    # CONDICIONAL PARA QUE SEA MAYOR A 15 KILOS Y OBTENGA UN DESCUENTO DEL 7% PERO MENOR A 20 KILOS
elif v_papasxkilos >= 15 and v_papasxkilos < 20:
    print("Usted compro ",v_papasxkilos, " Kilos De Papa con un valor de ",v_vdpxk2,"y obtuvo un descuento de ",(int(v_vdpx15kd))," Pesos y un total de ",v_vdpx15kd2," con descuento")
    # CONDICIONAL PARA QUE SEA MAYOR A 20 KILOS Y OBTENGA UN DESCUENTO DEL 10% 
elif v_papasxkilos >= 20:
    print("Usted compro ",v_papasxkilos, " Kilos De Papa con un valor de ",v_vdpxk2,"y obtuvo un descuento de ",(int(v_vdpx20kd))," Pesos y un total de ",v_vdpx20kd2," con descuento")
# ESTO ES PARA QUE SALGA UN MENSAJE SI DIGITA UN VALOR DE KILO IGUAL O QUE NO ESTE EN LOS KILOS ESTABLECIDOS    
else:
    print("Usted ingreso un valor fuera de nuestros descuentos")
