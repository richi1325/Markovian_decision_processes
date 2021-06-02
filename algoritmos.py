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
    print(">>>   Solución óptima   <<<")
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
    print(">>>   Solución óptima   <<<")
    print(f"\nTipo = {tipo}")
    print(f'Z = {z}')
    for x,y in map(lambda x,y: [x,y],variables,res.x):
        print(f'{x} = {round(y,4)}')
        if(round(y,4)>0.0):
            R.append(int(x[2]))  
    print(f'R={R}')