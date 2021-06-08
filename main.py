from time import sleep

from numpy.core.fromnumeric import nonzero
from menu import portada, eleccion
from lectura import lecturaPMD
from algoritmos import *
from os import system

def main():
    portada()
    input()
    tipo = None
    while True:
        system("cls")
        eleccion()
        seleccion = input("\n Seleccione una opción:")
        if seleccion == "1":
            tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
        elif seleccion == "2":
            if tipo == None:
                print("No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
            enumeracionExhaustivaPoliticas(estados,estados_decisiones, cij, k, tipo)
            input()
        elif seleccion == "3":
            if tipo == None:
                print("No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()            
            solucionPorProgramacionLineal(estados,estados_decisiones, cij, k, tipo)
            input()
        elif seleccion == "4":
            if tipo == None:
                print("No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()            
            mejoramientoPoliticas(estados,estados_decisiones, cij, k, tipo)
            input()
        elif seleccion == "5":
            if tipo == None:
                print("No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
            mejoramientoPoliticasDescuento(estados,estados_decisiones, cij, k, tipo,1)
            input()
        elif seleccion == "6":
            if tipo == None:
                print("No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
            aproximacionesSucesivas(estados,estados_decisiones, cij, k, tipo,1,100,0.1)
            input()
        elif seleccion == "7":
            break
        else:
            print("\n¡Por favor ingrese una opción válida!")
            sleep(2)
    print("""
        _
       /.\\
       Y  \\
      /   "L
     //  "/
     |/ /\_==================
     / /
    / /     ¡Hasta la próxima!
    \/

    """)
    sleep(3)

if __name__ == "__main__":
    main()