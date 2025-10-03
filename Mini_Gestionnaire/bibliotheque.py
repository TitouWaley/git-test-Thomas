import json
import csv

class Bibliotheque:
    def __init__(self):
        self.catalogue = []

    def ajouter_livre(self, titre, auteur, annee):
        if not titre or not auteur:
            print("Erreur : Titre et auteur obligatoires.")
            return
        self.catalogue.append({"titre": titre, "auteur": auteur, "annee": annee})
        print(f"Livre ajouté : {titre} - {auteur} ({annee})")

    def afficher_catalogue(self):
        if not self.catalogue:
            print("📚 Catalogue vide.")
            return
        print("\n--- Catalogue ---")
        for i, livre in enumerate(self.catalogue, 1):
            print(f"{i}. {livre['titre']} - {livre['auteur']} ({livre['annee']})")
        print("-----------------\n")

    def sauvegarder_json(self, fichier):
        try:
            with open(fichier, "w", encoding="utf-8") as f:
                json.dump(self.catalogue, f, indent=4, ensure_ascii=False)
            print(f"Sauvegarde réussie dans {fichier}")
        except PermissionError:
            print("Erreur : permissions insuffisantes pour écrire dans ce fichier.")
        except Exception as e:
            print(f"Erreur inattendue lors de la sauvegarde : {e}")

    def charger_json(self, fichier):
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                print("Erreur : format JSON invalide (liste attendue).")
                return
            self.catalogue = []
            for item in data:
                if isinstance(item, dict):
                    self.catalogue.append({
                        "titre": item.get("titre", ""),
                        "auteur": item.get("auteur", ""),
                        "annee": item.get("annee", None)
                    })
            print(f"Chargement réussi depuis {fichier}")
        except FileNotFoundError:
            print("Erreur : fichier inexistant.")
        except json.JSONDecodeError:
            print("Erreur : format JSON invalide (fichier corrompu).")
        except PermissionError:
            print("Erreur : permissions insuffisantes pour lire ce fichier.")
        except Exception as e:
            print(f"Erreur inattendue lors du chargement : {e}")

    def exporter_csv(self, fichier):
        try:
            with open(fichier, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["titre", "auteur", "annee"])
                writer.writeheader()
                writer.writerows(self.catalogue)
            print(f"Export CSV réussi dans {fichier}")
        except PermissionError:
            print("Erreur : permissions insuffisantes pour écrire dans ce fichier.")
        except Exception as e:
            print(f"Erreur inattendue lors de l'export CSV : {e}")


def menu():
    biblio = Bibliotheque()
    while True:
        print("\n=== Mini-gestionnaire de Bibliothèque ===")
        print("1. Ajouter un livre")
        print("2. Afficher le catalogue")
        print("3. Sauvegarder en JSON")
        print("4. Charger depuis JSON")
        print("5. Exporter en CSV")
        print("0. Quitter")
        choix = input("👉 Choix : ")

        if choix == "1":
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            annee = input("Année : ")
            biblio.ajouter_livre(titre, auteur, annee)
        elif choix == "2":
            biblio.afficher_catalogue()
        elif choix == "3":
            fichier = input("Nom du fichier JSON (ex: catalogue.json) : ")
            biblio.sauvegarder_json(fichier)
        elif choix == "4":
            fichier = input("Nom du fichier JSON à charger : ")
            biblio.charger_json(fichier)
        elif choix == "5":
            fichier = input("Nom du fichier CSV (ex: catalogue.csv) : ")
            biblio.exporter_csv(fichier)
        elif choix == "0":
            print("A plus!")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()
