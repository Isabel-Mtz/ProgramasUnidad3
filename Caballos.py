
"""
@author: Luna Ganzales Rocio y Martinez Garcia Isabel
"""

import copy

caballos = [ [ 1, 0, 1], 
	  [ 0, 0, 0], 
	  [ 2, 0, 2] 
		] 
for ver in range(3):
	for hor in range (3):
		print(caballos[ver][hor], end= ' ')
	print()	
print()

matriz = copy.deepcopy(caballos)

for a in range(4):
		
	if caballos[0][0] != 0:
		matriz[1][2]=copy.deepcopy(caballos[0][0])
		matriz[0][0]=copy.deepcopy(caballos[1][2])
		
	if caballos[0][1] != 0:
		matriz[2][2]=copy.deepcopy(caballos[0][1])
		matriz[0][1]=copy.deepcopy(caballos[2][2])

	if caballos[0][2] != 0:
		matriz[2][1]=copy.deepcopy(caballos[0][2])
		matriz[0][2]=copy.deepcopy(caballos[2][1])
				
	if caballos[1][0] != 0:
		matriz[0][2]=copy.deepcopy(caballos[1][0])
		matriz[1][0]=copy.deepcopy(caballos[0][2])
		
	if caballos[1][2] != 0:
		matriz[2][0]=copy.deepcopy(caballos[1][2])
		matriz[1][2]=copy.deepcopy(caballos[2][0])

	if caballos[2][0] != 0:
		matriz[0][1]=copy.deepcopy(caballos[2][0])
		matriz[2][0]=copy.deepcopy(caballos[1][2])

	if caballos[2][1] != 0:
		matriz[0][0]=copy.deepcopy(caballos[2][1])
		matriz[2][1]=copy.deepcopy(caballos[0][0])
								
	if caballos[2][2] != 0:
		matriz[1][0]=copy.deepcopy(caballos[2][2])
		matriz[2][2]=copy.deepcopy(caballos[1][0])
		
	caballos = copy.deepcopy(matriz)
		
	for ver in range(3):
		for hor in range (3):
			print(matriz[ver][hor], end= ' ')
		print()
	print()
"""
resultado de correr el programa:
    1 0 1 
0 0 0 
2 0 2 

0 2 0 
2 0 1 
0 1 0 

1 0 2 
0 0 0 
1 0 2 

0 1 0 
2 0 1 
0 2 0 

2 0 2 
0 0 0 
1 0 1 
"""