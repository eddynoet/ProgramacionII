from platos.plato import Plato
from platos.pique import Pique
from platos.charque import Charque

pique = Pique("Pique macho", 80, "grande")
charque = Charque("Charquekan", 50, "con extra queso")

pique.mostrar_info()
pique.entregar_plato()
pique.recojer_plato()
print(" ")
charque.mostrar_info()
charque.entregar_plato()
charque.recojer_plato()

