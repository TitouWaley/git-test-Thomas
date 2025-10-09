import os
from src.file_manager import BibliothequeAvecFichier
from src.models import Livre


def test_sauvegarde_et_chargement(tmp_path):
    path = tmp_path / "catalogue.json"
    b = BibliothequeAvecFichier("Test")
    b.ajouter_livre(Livre("Titre", "Auteur", "123"))
    b.sauvegarder_json(path)
    assert path.exists()

    b2 = BibliothequeAvecFichier.charger_json(path)
    assert b2.nom == "Test"
    assert len(b2.livres) == 1
    assert b2.livres[0].titre == "Titre"
