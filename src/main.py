from enumerationInstance import enumerationInstance
from propagation import propagation
from time import time

listTempoIncomplete = []
for i in range(1, 17) :
    chronoStart = time()
    propagation(f"instances/{i}.txt")
    chronoStop = time()
    listTempoIncomplete.append(chronoStop - chronoStart)
    print()
    
listTempoComplete = []
for i in range(1, 17) :
    chronoStart = time()
    enumerationInstance(f"instances/{i}.txt")
    chronoStop = time()
    listTempoComplete.append(chronoStop - chronoStart)
    print()
    
print("Algorithme : Méthode INCOMPLETE de résolution !")
for i in range(16) :
    print(f"   -> Instance {i+1} : {listTempoIncomplete[i]} secondes.")
    
print('\n')
    
print("Algorithme : Méthode COMPLETE de résolution !")
for i in range(16) :
    print(f"   -> Instance {i+1} : {listTempoComplete[i]} secondes.")