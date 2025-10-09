import json
import csv
from pathlib import Path
from src.models import Livre, LivreNumerique, Bibliotheque
from src.exceptions import (
    ErreurFichierBibliotheque,
    ErreurChargementJSON,
    ErreurSauvegardeJSON,
    ErreurExportCSV,
)


class BibliothequeAvecFichier(Bibliotheque):
    def __init__(self, nom):
        super().__init__(nom)
        self.dossier_donnee = Path(__file__).resolve().parent.parent / "donnée"
        self.dossier_donnee.mkdir(exist_ok=True)

    def _encode_livre(self, livre):
        d = {
            "type": livre.__class__.__name__,
            "titre": livre.titre,
            "auteur": livre.auteur,
            "isbn": livre.isbn,
        }
        if isinstance(livre, LivreNumerique):
            d["taille_fichier"] = livre.taille_fichier
        return d

    @staticmethod
    def _decode_livre(item):
        typ = item.get("type", "Livre")
        if typ == "LivreNumerique":
            return LivreNumerique(
                item["titre"], item["auteur"], item["isbn"], item.get("taille_fichier", 0.0)
            )
        return Livre(item["titre"], item["auteur"], item["isbn"])

    def sauvegarder_json(self):
        path = self.dossier_donnee / "catalogue.json"
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({
                    "nom": self.nom,
                    "livres": [self._encode_livre(l) for l in self.livres]
                }, f, ensure_ascii=False, indent=2)
            print(f"Sauvegarde JSON réussie dans {path}")
        except Exception as e:
            raise ErreurSauvegardeJSON(f"Erreur lors de la sauvegarde JSON : {e}") from e

    @classmethod
    def charger_json(cls):
        dossier_donnee = Path(__file__).resolve().parent.parent / "donnée"
        path = dossier_donnee / "catalogue.json"
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise ErreurFichierBibliotheque(f"Fichier introuvable : {path}") from e
        except json.JSONDecodeError as e:
            raise ErreurChargementJSON(f"Erreur de format JSON : {e}") from e

        biblio = cls(data.get("nom", "SansNom"))
        for item in data.get("livres", []):
            biblio.ajouter_livre(cls._decode_livre(item))
        return biblio

    def exporter_csv(self):
        path = self.dossier_donnee / "catalogue.csv"
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["type", "titre", "auteur", "isbn", "taille_fichier"]
                )
                writer.writeheader()
                for livre in self.livres:
                    row = self._encode_livre(livre)
                    row.setdefault("taille_fichier", "")
                    writer.writerow(row)
            print(f"📤 Export CSV réussi dans {path}")
        except OSError as e:
            raise ErreurExportCSV(f"Erreur lors de l'export CSV : {e}") from e
