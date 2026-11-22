class Grille:
    def __init__(self, nb_lignes, nb_colonnes):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.vide = "∿"
        self.matrice = [self.vide] * (nb_lignes * nb_colonnes)

    def tirer(self, ligne, colonne, touche="x"):
        indice = ligne * self.nb_colonnes + colonne
        self.matrice[indice] = touche

    def ajoute(self, bateau):
        positions = bateau.positions()
        for l, c in positions:
            if not (0 <= l < self.nb_lignes and 0 <= c < self.nb_colonnes):
                return
        for l, c in positions:
            self.matrice[l * self.nb_colonnes + c] = bateau.marque

    def __str__(self):
        lignes = []
        for l in range(self.nb_lignes):
            debut = l * self.nb_colonnes
            fin = debut + self.nb_colonnes
            lignes.append("".join(self.matrice[debut:fin]))
        return "\n".join(lignes)