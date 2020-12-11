"""
@author: Luna Ganzales Rocio y Martinez Garcia Isabel
"""
import json
import random
from operator import itemgetter

with open('colina.json') as file:
	Conocimiento = json.load(file)


camino=[]
pista=[]
nodo = []

def subircolina(principio,punto,anterior):
	camino.append(principio)
	print("El camino es  "+ principio)
	print("El camino anterior es  "+ anterior)
	if nodo:
		del nodo[:]
		del pista[:]
	if punto == principio:
		print("objetivo encontrado")
		return principio
	if anterior == "":
		anterior = principio
	for i in Conocimiento:
		if i[0] == principio:
			if anterior != "":
				if i[1] != anterior:
					pista.append(i)
	print(min(pista, key=itemgetter(2))[:])
	print (pista)
	inicio = (min(pista, key=itemgetter(2))[2])
	
	for j in pista:
		if j[2] == inicio:
			print("entra")
			nodo.append(j)
	print("valores finales")
	print(nodo)
	cont = 0
	for x in nodo:
		cont = cont +1
		if cont > 1:
			y = random.random()
			print("x")
			print(x)
			if y < 0.5:
				nodo.pop()
			else: 
				nodo.pop(0)
		else:
			print(nodo)
	if nodo:
		for x in nodo:
			print("nodo")
			print(x[1])
			return subircolina(x[1],punto,principio)
conexion=subircolina("A","H","")
if conexion:
	print("nodo")
	print(conexion)
	print("ruta")
	print(camino)
