from grille import Grille
from bateau import Torpilleur

g = Grille(5, 8)
torpilleur = Torpilleur(2, 3, vertical=False)  # Positions : (2, 3) et (2, 4)

g.tirer(2, 3, touche="💣")
print(g)

g.tirer(2, 4, touche="💣")

if torpilleur.coulé(g, touche="💣"):
    g.ajoute(torpilleur)

print(g)