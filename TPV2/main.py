from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
sys.path.append(str(SRC_DIR))

from src.models import Livre, LivreNumerique
from src.file_manager import BibliothequeAvecFichier
from src.exceptions import ErreurSauvegardeJSON, ErreurChargementJSON, ErreurFichierBibliotheque, ErreurExportCSV


def main():
    bibliotheque = BibliothequeAvecFichier("Bibliothèque Municipale")

    livres = [
        Livre("Tron", "Charles Xavier", "978-0560139876"),
        LivreNumerique("1845", "Maxime Kiff", "788-0451524935", 2.5),
        Livre("Pirate des Caraïbes", "Salazar", "788-0156013987"),
        Livre("Harry Potter", "J.K. Rowling", "788-156013987"),
        Livre("B1B", "Sup de Vinci", "788-015601987"),
        Livre("Cours de Python", "Colin", "788-056013987"),
    ]

    for livre in livres:
        bibliotheque.ajouter_livre(livre)

    print("\n📚 Catalogue initial :")
    print(bibliotheque)

    print("\n🔎 Recherche par titre '1845' :")
    for l in bibliotheque.rechercher_par_titre("1845"):
        print("  ", l)

    bibliotheque.supprimer_livre("788-0156013987")
    print("\n🗑️ Livre supprimé :")
    print(bibliotheque)

    try:
        bibliotheque.sauvegarder_json()
    except ErreurSauvegardeJSON as e:
        print("Erreur sauvegarde JSON :", e)

    try:
        nouvelle_biblio = BibliothequeAvecFichier.charger_json()
        print("\n✅ Catalogue chargé depuis JSON :")
        print(nouvelle_biblio)
    except (ErreurFichierBibliotheque, ErreurChargementJSON) as e:
        print("Erreur chargement JSON :", e)

    try:
        bibliotheque.exporter_csv()
    except ErreurExportCSV as e:
        print("Erreur export CSV :", e)


if __name__ == "__main__":
    main()
