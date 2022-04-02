# PROGRAMA HECHO EN PYTHON
# MANDAREMOS A PEDIR UN VALOR "COLOR" DE 3 Y DEPENDIENDO CUAL ESCOJA LA PERSONA SE MOSTRARA UN MENSAJE DIFERENTE
v_color = input( "Digitar valor ")
v_color = v_color.lower()
if v_color == "verde":
    print("Puede seguir")
elif v_color == "amarillo":
    print("Puede seguir pero con cuidado")
elif v_color == "Rojo":
    print("Detente")
