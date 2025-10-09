import pytest
from src.models import Livre, LivreNumerique, Bibliotheque


@pytest.fixture
def livre():
    return Livre("Titre", "Auteur", "1234567890")


@pytest.fixture
def livre_num():
    return LivreNumerique("Titre N", "Auteur N", "0987654321", 3.5)


@pytest.fixture
def biblio():
    b = Bibliotheque("Test")
    b.ajouter_livre(Livre("Livre A", "Auteur A", "111"))
    b.ajouter_livre(LivreNumerique("Livre B", "Auteur B", "222", 5.0))
    return b
