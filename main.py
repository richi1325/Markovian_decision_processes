from menu import portada
from lectura import lecturaPMD
from algoritmos import *
from os import system

def main():
    tipo = "MIN"
    estados = [0,1,2,3]
    decisiones = [0,1,2]
    estados_decisiones = [[1], [1, 3], [1, 2, 3], [3]]
    decisiones_estados = {
        1: [0, 1, 2],
        2: [2],
        3: [1, 2, 3]
    }
    cij = [
        [0.0, 0.0, 0.0],
        [1000.0, 0.0, 6000.0],
        [3000.0, 4000.0, 6000.0],
        [0.0, 0.0, 6000.0]
    ] 
    k = {
        1: [
            [0.0, 0.875, 0.0625, 0.0625],
            [0.0, 0.75, 0.125, 0.125],
            [0.0, 0.0, 0.5, 0.5],
            []
        ],
        2: [
            [],
            [],
            [0.0, 1.0, 0.0, 0.0],
            []
        ],
        3: [
            [],
            [1.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0]
        ]
    }
    #portada()
    #system("cls")
    #tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k = lecturaPMD()
    #system("cls")
    #enumeracionExhaustivaPoliticas(estados,estados_decisiones, cij, k, tipo)
    #solucionPorProgramacionLineal(estados,estados_decisiones, cij, k, tipo)

if __name__ == "__main__":
    main()