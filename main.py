import random
from termcolor import colored, cprint
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

MESSAGES_COULE = {
    PorteAvion: "Porte-avion coulé ! (🚢)",
    Croiseur: "Croiseur coulé ! (⛴)",
    Torpilleur: "Torpilleur coulé ! (🚣)",
    SousMarin: "Sous-marin coulé ! (🐟)",
}


def placer_bateaux(nb_lignes, nb_colonnes):
    types_bateaux = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    bateaux = []
    cases_occupees = set()

    for classe_bateau in types_bateaux:
        possibilites = []
        for l in range(nb_lignes):
            for c in range(nb_colonnes):
                for vertical in (False, True):
                    candidat = classe_bateau(l, c, vertical=vertical)
                    positions = candidat.positions()
                    dans_grille = all(
                        0 <= pl < nb_lignes and 0 <= pc < nb_colonnes
                        for pl, pc in positions
                    )
                    if dans_grille and not (set(positions) & cases_occupees):
                        possibilites.append(candidat)

        choisi = random.choice(possibilites)
        bateaux.append(choisi)
        cases_occupees.update(choisi.positions())

    return bateaux


def demander_tir(nb_lignes, nb_colonnes):
    while True:
        try:
            ligne = int(input(f"Ligne (0 à {nb_lignes - 1}) : "))
            colonne = int(input(f"Colonne (0 à {nb_colonnes - 1}) : "))
            if 0 <= ligne < nb_lignes and 0 <= colonne < nb_colonnes:
                return ligne, colonne
            cprint("Coordonnées hors de la grille, réessaie.", "yellow")
        except ValueError:
            cprint("Entre uniquement des nombres entiers.", "yellow")


def jouer():
    nb_lignes, nb_colonnes = 8, 10
    grille = Grille(nb_lignes, nb_colonnes)
    bateaux_restants = placer_bateaux(nb_lignes, nb_colonnes)
    coups = 0

    cprint("=== BATAILLE NAVALE ===", "cyan", attrs=["bold"])

    while bateaux_restants:
        print("\n" + colored(str(grille), "blue"))
        cprint(f"Bateaux restants : {len(bateaux_restants)}", "cyan")

        ligne, colonne = demander_tir(nb_lignes, nb_colonnes)
        coups += 1

        touche_bateau = None
        for b in bateaux_restants:
            if (ligne, colonne) in b.positions():
                touche_bateau = b
                break

        if touche_bateau is not None:
            grille.tirer(ligne, colonne, touche="💣")
            cprint("Touché !", "red", attrs=["bold"])
            if touche_bateau.coulé(grille, touche="💣"):
                grille.ajoute(touche_bateau)
                cprint(MESSAGES_COULE[type(touche_bateau)], "green", attrs=["bold"])
                bateaux_restants.remove(touche_bateau)
        else:
            grille.tirer(ligne, colonne)
            cprint("Plouf dans l'eau...", "blue")

    print("\n" + colored(str(grille), "blue"))
    cprint(f"Bravo ! Tous les bateaux ont été coulés en {coups} coups.", "green", attrs=["bold"])


if __name__ == "__main__":
    jouer()