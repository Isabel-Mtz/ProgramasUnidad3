
"""
Luna Ganzáles Rocio y Martinez Garcia Isabel
"""

import json
Angrafo = False

with open("anchuraarbol.json", "r") as read_file:
     data = json.load(read_file)
     Angrafo = data['angrafo']   
     
def profundidadnodo(nodo,inicio):
    grafo = []
    valor = True
    for n in Angrafo:
        if n["nodo"] == nodo:
            grafo=n["rama"].split()
    print (nodo,grafo)
    if(grafo[0] ==  inicio):
        print ("Se  a encontrado la Raiz del Arbol ")
        return False
    else:
        while(len(grafo)>=2):
            nodo = grafo[1]
            grafo.remove(nodo)
            valor=profundidadnodo(nodo,inicio)
            if (valor==False):
                return False
profundidadnodo("Raiz","15")