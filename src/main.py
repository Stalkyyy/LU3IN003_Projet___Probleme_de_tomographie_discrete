from CONSTANTES import *
from propagation import *
from time import time

print("Algorithme : Méthode INCOMPLETE de résolution !")

listTempo = []
for i in range(1, 17) :
    chronoStart = time()
    propagation(f"instances/{i}.txt")
    chronoStop = time()
    listTempo.append(chronoStop - chronoStart)
    print()
    
for i in range(16) :
    print(f"Instance {i+1} : {listTempo[i]} secondes.")