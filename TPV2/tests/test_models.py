def test_creation_livre(livre):
    assert livre.titre == "Titre"
    assert livre.auteur == "Auteur"
    assert livre.isbn == "1234567890"


def test_creation_livre_numerique(livre_num):
    assert livre_num.taille_fichier == 3.5


def test_ajout_livre_bibliotheque(biblio):
    assert len(biblio.livres) == 2
    biblio.ajouter_livre(livre := type("FakeLivre", (), {"isbn": "333"})())
    assert any(l.isbn == "333" for l in biblio.livres)
