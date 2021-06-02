from os import system
from sre_constants import RANGE
from time import sleep

def lecturaPMD():
    print("--------------RECOLECCIÓN DE DATOS--------------")
    
    #Tipo
    tipo = input("\n¿El problema es de MAX o MIN?:")

    #Estados
    estados = int(input("\nInserte el número de estados: "))
    decisiones = int(input("Inserte el número de decisiones: "))
    decisiones_estados = {}
    
    #Decisiones con estados a los que aplica
    print()
    estados_decisiones = list(map(lambda _: [],range(estados)))
    for i in range(decisiones):
        data = list(map(lambda x: int(x.strip()), input(f"Inserte los estados que aplican a la decisión #{i+1}: ").split(",")))
        decisiones_estados[i+1] = data
        for j in data:
            estados_decisiones[j].append(i+1)
    #Recolección de los costos
    system("cls")    
    print("-------------------- MATRIZ DE COSTOS --------------------")
    cij = list(map(lambda _: [],range(estados)))
    for i in range(estados):
        for j in range(decisiones):
            if i not in decisiones_estados.get(j+1,[]):
                cij[i].append(0.0)
            else:
                cij[i].append(float(input(f"Inserte el costo de del estado {i} con la desición {j+1}: ")))
    
    #Matriz de transición para los estados
    system("cls")
    print("-------------------- MATRICES DE TRANSICIÓN --------------------")
    k = {}
    for index,values in decisiones_estados.items():
        k[index] = []
        for i in range(estados):
            for j in range(estados):
                if i not in values:
                    if(j==0):
                        k[index].append([])
                    break
                else:
                    if(j==0):
                        k[index].append([])
                        print(f"-------------------- DECISIÓN K={index} CON ESTADOS={values} --------------------")
                    k[index][i].append(float(input(f"Inserte la probabilidad de pasar del estado {i} al estado {j}: ")))
    return tipo, range(estados), range(decisiones), estados_decisiones, decisiones_estados, cij, k