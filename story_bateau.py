from bateau import Bateau


def se_chevauchent(b1, b2):
    return bool(set(b1.positions()) & set(b2.positions()))


# Cas 1 : deux bateaux qui se chevauchent en (2, 3)
b1 = Bateau(2, 2, longueur=3, vertical=False)  # (2, 2), (2, 3), (2, 4)
b2 = Bateau(1, 3, longueur=3, vertical=True)   # (1, 3), (2, 3), (3, 3)
print("Cas 1 (chevauchement attendu) :", se_chevauchent(b1, b2))

# Cas 2 : deux bateaux qui ne se chevauchent pas
b3 = Bateau(0, 0, longueur=2, vertical=False)  # (0, 0), (0, 1)
b4 = Bateau(3, 3, longueur=2, vertical=True)   # (3, 3), (4, 3)
print("Cas 2 (pas de chevauchement attendu) :", se_chevauchent(b3, b4))