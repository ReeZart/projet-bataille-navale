from grille import Grille
from bateau import Bateau, PorteAvion


def test_init():
    g = Grille(5, 8)
    assert g.nb_lignes == 5
    assert g.nb_colonnes == 8
    assert len(g.matrice) == 40
    assert g.matrice[0] == "∿"


def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3)
    assert g.matrice[2 * 8 + 3] == "x"


def test_str():
    g = Grille(2, 3)
    assert str(g) == "∿∿∿\n∿∿∿"
    g.tirer(1, 2)
    assert str(g) == "∿∿∿\n∿∿x"



def test_ajoute_valide():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]


def test_ajoute_hors_grille():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]


def test_ajoute_sous_classe():
    g = Grille(5, 5)
    g.ajoute(PorteAvion(0, 0, vertical=False))
    assert g.matrice[:4] == ["🚢", "🚢", "🚢", "🚢"]