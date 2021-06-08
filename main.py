from time import sleep

from menu import portada, eleccion
from lectura import lecturaPMD, validadorEnteros
from algoritmos import *
from os import system
from examples import base1

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
                print(" No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
            enumeracionExhaustivaPoliticas(estados,estados_decisiones, cij, k, tipo)
            input()
        elif seleccion == "3":
            if tipo == None:
                print(" No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()            
            solucionPorProgramacionLineal(estados,estados_decisiones, cij, k, tipo)
            input()
        elif seleccion == "4":
            if tipo == None:
                print(" No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()            
            mejoramientoPoliticas(estados,estados_decisiones, cij, k, tipo)
            input()
        elif seleccion == "5":
            if tipo == None:
                print(" No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
            alpha = validadorFlotantes(' Inserte el factor de descuento:')
            mejoramientoPoliticasDescuento(estados,estados_decisiones, cij, k, tipo, alpha)
            input()
        elif seleccion == "6":
            if tipo == None:
                print(" No se han ingresado los datos por primera vez, serás redireccionado a la opción 1....")
                sleep(6)
                tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
            alpha = validadorFlotantes(' Inserte el factor de descuento:')
            iteraciones = validadorEnteros(' Inserte el número de iteraciones:')
            tolerancia = validadorFlotantesPositivos(' Inserte la tolerancia del método:')
            aproximacionesSucesivas(estados,estados_decisiones, cij, k, tipo,alpha,iteraciones,tolerancia)
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

def validadorFlotantes(mensaje):
    while True:
        try:
            numero = input(mensaje) 
            numero = float(numero)
            break
        except ValueError:
            print('¡Debes insertar un número!')
    return numero

def validadorFlotantesPositivos(mensaje):
    while True:
        try:
            numero = input(mensaje) 
            numero = float(numero)
            if numero<=0.0:
                print('El valor debe ser mayor a 0!')
            else:
                break
        except ValueError:
            print('¡Debes insertar un número!')
    return numero


if __name__ == "__main__":
    main()