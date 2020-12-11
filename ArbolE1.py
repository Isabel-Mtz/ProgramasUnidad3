# -*- coding: utf-8 -*-
"""
@author:   Luna Ganzáles Rocio y Martinez Garcia Isabel
"""
import json
Angrafo = False

with open("anchuraarbol.json", "r") as read_file:
     data = json.load(read_file)
     Angrafo = data['angrafo']   
     
def recorinodo(tomavla):
    a = 0 
    nodo =[]
    grafo = []
    for n in Angrafo:
        grafo = grafo+[n["rama"].split()]
        nodo = nodo+[n["nodo"].split()]
    for n in grafo:
        print (nodo[a],grafo[a][0])
        if (grafo[a][0] == tomavla):
            return True
        a +=1
        
rearbol = recorinodo("30")
if (rearbol == True):
    print ("Raiz")