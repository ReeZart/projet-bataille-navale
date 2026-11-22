class Bateau:
    marque = "⛵"

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        if self.vertical:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]
        return [(self.ligne, self.colonne + i) for i in range(self.longueur)]

    def coulé(self, grille, touche="x"):
        for l, c in self.positions():
            if grille.matrice[l * grille.nb_colonnes + c] != touche:
                return False
        return True


class PorteAvion(Bateau):
    marque = "🚢"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)


class Croiseur(Bateau):
    marque = "⛴"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)


class Torpilleur(Bateau):
    marque = "🚣"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)


class SousMarin(Bateau):
    marque = "🐟"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)