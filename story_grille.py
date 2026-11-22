from grille import Grille

g = Grille(5, 8)

while True:
    print(g)
    ligne = int(input("Ligne (0 à 4) : "))
    colonne = int(input("Colonne (0 à 7) : "))
    g.tirer(ligne, colonne)