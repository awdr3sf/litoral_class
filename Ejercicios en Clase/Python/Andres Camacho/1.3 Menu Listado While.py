#FUNCION DEFINIDA
class menu0:
    print("\n Menu Opciones")
    Menu1 = ['1. Menu Principal','2.Menu Personas','3.Menu Clientes','4.Salir']
    print("\n",Menu1[0],"\n",Menu1[1],"\n",Menu1[2],"\n",Menu1[3])
#FUNCION LLAMADA
menu = menu0

#VARIABLE VALOR USUARIO
Menu = int(input("Digitar un valor : "))
#CONDICIONES PARA MOSTRAR MENU
while Menu !=4 and Menu < 4:
    if Menu == 1:
        print("|=======Abriste Menu Principal========|")  
        print("\n",menu0.Menu1[1],"\n",menu.Menu1[2],"\n",menu.Menu1[3])
        print("|=======Puedes Elegir Otra Opcion : ========|")
    elif Menu == 2:
        print("|=======Abriste Menu Personas========|")
        print("\n",menu0.Menu1[0],"\n",menu.Menu1[2],"\n",menu.Menu1[3])
        print("|=======Puedes Elegir Otra Opcion : ========|")
    elif Menu == 3:
        print("|=======Abriste Menu Clientes========|")
        print("\n",menu0.Menu1[0],"\n",menu.Menu1[1],"\n",menu.Menu1[3])
        print("|=======Puedes Elegir Otra Opcion : ========|")
    elif Menu == 4:
        print("Gracias Vuelva Pronto")
    Menu = int(input("Digitar un valor : "))

