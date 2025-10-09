from src.models import Livre
from src.file_manager import BibliothequeAvecFichier

def test_sauvegarde_et_chargement(tmp_path):
    b = BibliothequeAvecFichier("Test")
    b.ajouter_livre(Livre("Titre", "Auteur", "123"))

    b.sauvegarder_json()

    b2 = BibliothequeAvecFichier.charger_json()

    assert len(b2.livres) == 1
    assert b2.livres[0].titre == "Titre"
    assert b2.livres[0].auteur == "Auteur"

#J'ai trouvé en lisant les erreurs une pas une.