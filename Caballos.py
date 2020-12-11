
"""
@author: Luna Ganzales Rocio y Martinez Garcia Isabel
"""

import json
import random

from operator import itemgetter

juego = [0,0,0,0]
jugadores = [1,1,-1,-1]
avance = [0,0,0,0]
tablerodeljuego = [[0,0,0],[0,0,0],[0,0,0]]
piezacaballo = [[0,1],[2,1],[6,-1],[8,-1]]

with open('Pocicioncaballo.json') as file:
	data = json.load(file)

def Movimientode(data,piezacaballo,juego,avance):
    for i in range(len(piezacaballo)):
        for j in data:
            if j[0] == piezacaballo[i][0]:
                if (i == 0)and(juego[0] == 0) and (avance[0] == 0):
                    piezacaballo[i][0] = j[1]
                    avance[0] = 1
                    print("Caballo  p1")
                    print("Movimiento del caballo")
                    print(piezacaballo[i][0])
                    tablerodeljuego = Tablero(piezacaballo[i][0],1)
                    if (piezacaballo[i][0]) == 8:
                        juego[i] = 1
            
                if (i == 1)and(juego[1] == 0)and (avance[1] == 0):
                    piezacaballo[i][0] = j[1]
                    avance[1] = 1
                    print("Caballo  p2")
                    print("Movimiento del caballo")
                    print(piezacaballo[i][0])
                    tablerodeljuego = Tablero(piezacaballo[i][0],2)
                    if (piezacaballo[i][0]) == 6:
                        juego[i] = 1
                    
                if (i == 2)and(juego[2] == 0)and (avance[2] == 0):
                    piezacaballo[i][0] = j[1]
                    avance[2] = 1
                    print("Caballo  p3")
                    print("Movimiento del caballo")
                    print(piezacaballo[i][0])
                    tablerodeljuego = Tablero(piezacaballo[i][0],3)
                    if (piezacaballo[i][0]) == 2:
                        juego[i] = 1
                    
                if (i == 3)and(juego[3] == 0)and (avance[3] == 0):
                    piezacaballo[i][0] = j[1]
                    avance[3] = 1
                    print("Caballo  p4")
                    print("Movimiento del caballo")
                    print(piezacaballo[i][0])
                    tablerodeljuego = Tablero(piezacaballo[i][0],4)
                    if (piezacaballo[i][0]) == 0:
                        juego[i] = 1
    print("posiciones")                
    for i in tablerodeljuego:
        print(i)
    print("Posiciones")    
    if 0 in juego:
        avance = [0,0,0,0]
        tablerodeljuego = reiniciartirada(tablerodeljuego)
        return Movimientode(data,piezacaballo,juego,avance)
    else:
        return finaliza(piezacaballo)

def Tablero(movimiento,piezacaballo):    
    if movimiento==0:
        tablerodeljuego[0][0] = piezacaballo
    if movimiento==1:
        tablerodeljuego[0][1] = piezacaballo
    if movimiento==2:
       tablerodeljuego[0][2] = piezacaballo
    if movimiento==3:
        tablerodeljuego[1][0] = piezacaballo
    if movimiento==5:
       tablerodeljuego[1][2] = piezacaballo
    if movimiento==6:
        tablerodeljuego[2][0] = piezacaballo
    if movimiento==7:
        tablerodeljuego[2][1] = piezacaballo
    if movimiento==8:
        tablerodeljuego[2][2] = piezacaballo
    return tablerodeljuego

def reiniciartirada(tablerodeljuego):
    for i in range(len(tablerodeljuego)):
        for r in range(len(tablerodeljuego[i])):
            tablerodeljuego[i][r] = 0
    return tablerodeljuego

def finaliza(piezacaballo):
    print("Fin")
    
    for p in piezacaballo:
        print(p)
Movimientode(data,piezacaballo,juego,avance)