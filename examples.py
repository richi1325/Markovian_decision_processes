def base1():
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
    return tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k

def base2():
    tipo = "MIN"
    estados = [0,1]
    decisiones = [0,1]
    estados_decisiones = [[1,2],[1,2]]
    decisiones_estados = {
        1: [0, 1],
        2: [0, 1],       
    }
    cij = [
        [14,0],
        [14,75],
    ] 
    k = {
        1: [
            [0.875, 0.125,],
            [0.875, 0.125,],
        ],
        2: [
            [0.125, 0.875,],
            [0.125, 0.875,],
        ],
    }
    return tipo, estados, decisiones, estados_decisiones, decisiones_estados, cij, k
