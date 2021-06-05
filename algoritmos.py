from functools import reduce
from itertools import product

from numpy.core.fromnumeric import var
from numpy.lib.function_base import piecewise
from sympy import sympify, solve, simplify
import numpy as np

def enumeracionExhaustivaPoliticas(estados, estados_decisiones, cij, k, tipo):
    politicas = list(product(*estados_decisiones))
    politica_optima = None
    pi_optimo = None
    ER_optimo = None
    print("\n>>>   Políticas   <<<\n")
    for i in politicas:
        PR_i = []
        coef_c = []
        variables = list(map(lambda i: f"π{i}", estados))
        for j,v in map(lambda x,y: [x,y], i,estados):
            coef_c.append(cij[v][j-1]) 
            PR_i.append(k[j][v])
        index=0
        eq_system=[]
        for row in np.array(PR_i).transpose():
            eq_system.append(sympify(reduce(lambda a,b: a+"+"+b,
                [*map(lambda x,y: f"{x}*{y}",row,variables),"-"+variables[index]]
            )))
            eq_system.append(sympify(reduce(lambda a,b: a+"+"+b,[*variables,"-1"])))
            index+=1
        sol = solve(eq_system)
        resultado = np.dot(coef_c,[*sol.values()])

        solPantalla = {}
        for var, value in sol.items():
            solPantalla[var] = round(value,4)
        print(i,"-",solPantalla,"-",resultado)
        if(politica_optima == None):
            politica_optima = i
            pi_optimo = sol
            ER_optimo = resultado
        else:
            if tipo=="MAX" and ER_optimo<resultado:
                politica_optima = i
                pi_optimo = sol
                ER_optimo = resultado
            elif tipo=="MIN"and ER_optimo>resultado:
                politica_optima = i
                pi_optimo = sol
                ER_optimo = resultado
    print("\n>>>   Solución óptima   <<<")
    print(f"\nTipo = {tipo}")
    print(f"R = {politica_optima}")
    for a,b in pi_optimo.items():
        print(f"{a} = {round(b,4)} ")
    print(f"E(R) = {round(ER_optimo,4)}\n")

from scipy.optimize import linprog
def solucionPorProgramacionLineal(estados, estados_decisiones, cij, data, tipo):
    
    #Función Objetivo
    variables = []
    c = []
    restriccion = []
    A_eq = []
    b_eq = []
    #Sujeto a:
    #Suma de todas las variables igual con 1
    for i in estados:
        for k in estados_decisiones[i]:
            variables.append(f'y{i}{k}')
            c.append(cij[i][k-1])
            restriccion.append(1.0)
    A_eq.append(restriccion)
    b_eq.append(1.0)

    #Restriccion por indice j 
    restriccion = []
    for j in estados[:len(estados)-1]:
        for i in estados:
            for k in estados_decisiones[i]:
                if(data[k][i][j]==0.0):
                    restriccion.append(data[k][i][j])
                else:
                    restriccion.append(data[k][i][j]*-1)
        for k in estados_decisiones[j]:
            index = variables.index(f'y{j}{k}')
            restriccion[index] += 1.0  
        A_eq.append(restriccion)
        b_eq.append(0.0)
        restriccion=[]
    if tipo=="MIN":
        res=linprog(c=c,A_eq=A_eq,b_eq=b_eq,method="simplex")
        z=round(res.fun,4)
    else:
        res=linprog(c=np.array(c)*-1,A_eq=A_eq,b_eq=b_eq,method="simplex")
        z=round(res.fun*-1,4)
    R=[]

    print("\n>>>   Modelo   <<<\n")
    eq=""
    for value, var in map(lambda x,y :[x,y], c,variables):
        eq+="+"+str(value)+"*"+var
    print(f"{tipo}  Z =",simplify(sympify(eq)))
    print("\nSujeto a:\n")
    index=0
    for row in A_eq:
        eq=""
        for value, var in map(lambda x,y:[x,y], row,variables):
            eq+="+"+str(value)+"*"+var
        print(f"\t{simplify(sympify(eq))} = {b_eq[index]}")
        index+=1
    print("\n>>>   Solución óptima   <<<\n")
    print(f'Z = {z}')
    for x,y in map(lambda x,y: [x,y],variables,res.x):
        print(f'{x} = {round(y,4)}')
        if(round(y,4)>0.0):
            R.append(int(x[2]))  
    print(f'\nR = {R}\n')

import random
def mejoramientoPoliticas(estados, estados_decisiones, cij, data, tipo):
    #Seleccion de politica aleatoria
    print(f"\nTipo = {tipo}")
    politica_inicial = []
    for j in estados_decisiones:
        politica_inicial.append(random.choice(j))
    PR_i = []
    coef_c = []
    print(f"\nPolítica arbitraría: {politica_inicial}")
    for j,v in map(lambda x,y: [x,y], politica_inicial,estados):
        coef_c.append(cij[v][j-1]) 
        PR_i.append(data[j][v])
    #Construcción y solución del sistema de ecuaciones
    while True:
        eq_system=[]
        for i in estados:
            eq=f"g-{cij[i][politica_inicial[i]-1]}-"
            eq+=reduce(lambda x,y: x+"-"+y ,map(lambda x:
                f"{data[politica_inicial[i]][i][x]}*v{x}",
                estados
            ))
            eq+=f"+v{i}"
            eq_system.append(eq)
        eq_system.append(f"v{estados[len(estados)-1]}")
        sol = solve(eq_system)
        for var, value in sol.items():
            print(f"{var} = {round(value,4)}")
        #Prueba de optimalidad y seleccion de nueva politica
        politica_optima = []
        for i in estados:
            if(len(estados_decisiones[i])==1):
                politica_optima.append(politica_inicial[i]) 
            else:
                pivote = None
                decision = None
                for k in estados_decisiones[i]:                        
                    eq=f"{cij[i][k-1]}+"
                    eq+=reduce(lambda x,y: x+"+"+y ,map(lambda x:
                        f"{data[k][i][x]}*v{x}",
                        estados
                    ))
                    eq+=f"-v{i}"
                    for var, value in sol.items():
                        eq=sympify(eq).subs(var,value)
                    if pivote==None:
                        pivote=eq
                        decision=k
                    else:
                        if tipo=="MAX":
                            if pivote<eq:
                                pivote=eq
                                decision=k
                        else:
                            if pivote>eq:
                                pivote=eq
                                decision=k
                politica_optima.append(decision)                
        if politica_inicial == politica_optima:
            print(f"\n>>> Política óptima: {politica_optima} <<<\n")
            break
        else: 
            print(f"\nNueva política: {politica_optima}")
            politica_inicial = politica_optima

def mejoramientoPoliticasDescuento(estados, estados_decisiones, cij, data, tipo, alpha=1):
    #Seleccion de politica aleatoria
    print(f"\nTipo = {tipo}")
    print(f"α = {alpha}")
    politica_inicial = []
    for j in estados_decisiones:
        politica_inicial.append(random.choice(j))
    PR_i = []
    coef_c = []
    print(f"\nPolítica arbitraría: {politica_inicial}")
    for j,v in map(lambda x,y: [x,y], politica_inicial,estados):
        coef_c.append(cij[v][j-1]) 
        PR_i.append(data[j][v])
    #Construcción y solución del sistema de ecuaciones
    while True:
        eq_system=[]
        for i in estados:
            eq=f"v{i}-{cij[i][politica_inicial[i]-1]}+0.9*(-"
            eq+=reduce(lambda x,y: x+"-"+y ,map(lambda x:
                f"{data[politica_inicial[i]][i][x]}*v{x}",
                estados
            ))
            eq+=")"
            eq_system.append(eq)
        sol = solve(eq_system)
        for var, value in sol.items():
            print(f"{var} = {round(value,4)}")
        #Prueba de optimalidad y seleccion de nueva politica
        politica_optima = []
        for i in estados:
            if(len(estados_decisiones[i])==1):
                politica_optima.append(politica_inicial[i]) 
            else:
                pivote = None
                decision = None
                for k in estados_decisiones[i]:                        
                    eq=f"{cij[i][k-1]}+"
                    eq+=reduce(lambda x,y: x+"+"+y ,map(lambda x:
                        f"{data[k][i][x]}*v{x}",
                        estados
                    ))
                    eq+=f"-v{i}"
                    for var, value in sol.items():
                        eq=sympify(eq).subs(var,value)
                    if pivote==None:
                        pivote=eq
                        decision=k
                    else:
                        if tipo=="MAX":
                            if pivote<eq:
                                pivote=eq
                                decision=k
                        else:
                            if pivote>eq:
                                pivote=eq
                                decision=k
                politica_optima.append(decision)                
        if politica_inicial == politica_optima:
            print(f"\n>>> Política óptima: {politica_optima} <<<\n")
            break
        else: 
            print(f"\nNueva política: {politica_optima}")
            politica_inicial = politica_optima