from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin

def test_init_defaut():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical is False


def test_positions():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]



def test_coule():
    g = Grille(3, 3)
    b = Bateau(1, 0, longueur=2, vertical=False)
    g.tirer(1, 0)
    assert b.coulé(g) is False
    g.tirer(1, 1)
    assert b.coulé(g) is True


def test_types_bateaux():
    assert PorteAvion(0, 0, False).longueur == 4
    assert Croiseur(0, 0, False).longueur == 3
    assert Torpilleur(0, 0, False).longueur == 2
    assert SousMarin(0, 0, False).longueur == 2