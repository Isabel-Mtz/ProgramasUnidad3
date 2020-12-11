"""
@author: Luna Ganzales Rocio y Martinez Garcia Isabel
"""


movimiento=[]
juego = 0
tablero =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
jugada = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def datos(reinas, tablero, juego,jugada):
    pt = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    ptablero = 0
    print("Reinas "+str(reinas))
 
    if reinas == 1:
        return solucion(tablero)
    else: 
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                
                if ptablero  == 0:
					
                    if jugada[i][j] != 3:
                        if(tablero[i][j] == 0):

                            if reinas == 4:
                                jugada[i][j] = 3
                            tablero[i][j] = 1
                            ptablero  = ptablero  + 1
                            movimiento.append([i,j])
        tablero = tableromovimiento(tablero,movimiento)
        movimiento.pop(0)
        for i in tablero:

            if 0 in i:
                juego = 0
            else:
                juego = 1
        if juego == 1:
            print(juego)
            for i in pt:
                print(i)
            Numeroreinas = 4
            juego=0
            return datos(reinas,pt,juego,jugada)
        if juego == 0:
            print(juego)
            reinas=reinas-1
            return datos(reinas,tablero,juego,jugada)

def tableromovimiento(tablero,movimiento):
    print("****Movimientos en que la reina se puede mover****")
    ver = movimiento[0][0]
    hor = movimiento[0][1]
    j = range(len(tablero))
    hor2 = hor
    hor1 = ver
    print(movimiento)
    
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            tablero[ver][j] = 2
            tablero[i][hor] = 2
    fin(tablero)
    for i in range(len(tablero)):
        hor2 = hor2-1
        hor1 = hor1 -1
        if (hor2 >= 0)and(hor1 >=0):
            print("========================")
            tablero[hor1][hor2] = 2
    hor2 = hor
    hor1 = ver
    fin(tablero)
    for i in range(len(tablero)):
        hor1 = hor1 +1
        hor2 = hor2 +1
        if (hor1 <= j)and(hor2 <= j):
            print("========================")
            tablero[hor1][hor2] = 2
    hor2 = hor
    hor1 = ver
    fin(tablero)
    for i in range(len(tablero)):
        hor2 = hor2+1
        hor1 = hor1 -1
        if (hor2 < j)and(hor1 >=0):
            print("========================")
            tablero[hor1][hor2] = 2
    hor2 = hor
    hor1 = ver
    fin(tablero)
    for i in range(len(tablero)):
        hor2 = hor2-1
        hor1 = hor1 + 1
        if (hor2 >= 0)and(hor1 <j):
            print("========================")
            tablero[hor1][hor2] = 2
    tablero[ver][hor]=1
    fin(tablero)
    return tablero
    

def solucion(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if (tablero[i][j]) == 0:
                 tablero[i][j] = 1
    print("========================")
    print('Fin')
    for i in tablero:
        print(i)
        print(" ==========")

def fin(tablero):
    for i in tablero:
        print(i)
        print(" ==========")

datos(4,tablero,0,jugada)