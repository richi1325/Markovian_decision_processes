from os import system
import re

def lecturaPMD():
    system("cls")
    print("--------------RECOLECCIÓN DE DATOS--------------")
    
    #Tipo
    while True:
        tipo = input("\n¿El problema es de MAX o MIN?:").upper().strip()
        if tipo in ['MAX','MIN']:
            break
        else:
            print('¡Por favor selecciona una opción válida!')

    #Estados
    estados = validadorEnteros("\nInserte el número de estados: ")   
    decisiones = validadorEnteros("Inserte el número de decisiones: ")
    decisiones_estados = {}
    
    #Decisiones con estados a los que aplica
    print()
    estados_decisiones = list(map(lambda _: [],range(estados)))
    for i in range(decisiones):
        data_correcta = True
        while True:
            estados_decisionesInput = input(f"Inserte los estados que aplican a la decisión #{i+1}: ")
            if re.findall(r'[^0-9,]+',estados_decisionesInput):
                print('¡Sólo se aceptan números y comas!')
            else:
                data = list(map(lambda x: int(x.strip()), estados_decisionesInput.split(",")))
                data.sort()
                data = set(data)
                for elemento in data:
                    if elemento not in range(estados):
                        print('¡Uno o más estados ingresados no existen!')
                        data_correcta = False
                        break
                    else:
                        data_correcta = True
                if data_correcta:
                    break
        decisiones_estados[i+1] = list(data)
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
                while True:
                    costo_input = input(f"Inserte el costo de del estado {i} con la desición {j+1}: ")
                    try:
                        costo_input = float(costo_input)
                        break
                    except ValueError:
                        print('¡Debes insertar un número!')
                cij[i].append(costo_input)
    
    #Matriz de transición para los estados
    system("cls")
    print("-------------------- MATRICES DE TRANSICIÓN --------------------")
    k = {}
    for index,values in decisiones_estados.items():
        k[index] = []
        for i in range(estados):
            while True:
                for j in range(estados):
                    if i not in values:
                        if(j==0):
                            k[index].append([])
                        break
                    else:
                        if(j==0):
                            print(f'\n**********        K = {index},  ESTADO = {i}       **********\n')
                            k[index].append([])
                        while True:
                            try:
                                probabilidad_input = input(f"Inserte la probabilidad de pasar del estado {i} al estado {j}: ")
                                probabilidad_input = float(probabilidad_input)
                                if probabilidad_input<0.0 or probabilidad_input>1.0:
                                    print("Las probabilidades no pueden ser menores a cero o mayores a 1")
                                else:
                                    break
                            except ValueError:
                                print('¡Debes insertar un número!')
                        k[index][i].append(float(probabilidad_input))
                if (round(sum(k[index][i]),4)<1.0 or round(sum(k[index][i]),4)>1.0) and k[index][i]:
                    print(f"\nLa suma de las probabilidades para P{i}j(k={index}) = {round(sum(k[index][i]),4)}  != 1, por favor ingresa un vector válido\n")
                    k[index].pop()
                else: 
                    break
    return tipo, range(estados), range(decisiones), estados_decisiones, decisiones_estados, cij, k


def validadorEnteros(mensaje):
    while True:
        try:
            numero = input(mensaje) 
            numero = int(numero)
            if numero<=0: 
                print('¡Ingresa un número mayor a cero!')
            else:
                break
        except ValueError:
            print('¡Debes insertar un número!')
    return numero