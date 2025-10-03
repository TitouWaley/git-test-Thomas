class Livre:
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"{self.titre} - {self.auteur} (ISBN: {self.isbn})"


class LivreNumerique(Livre):
    def __init__(self, titre: str, auteur: str, isbn: str, taille_fichier: float):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier  

    def __str__(self):
        return f"{super().__str__()} - Taille fichier: {self.taille_fichier} Mo"


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)

    def supprimer_par_isbn(self, isbn: str):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]
    
    def rechercher_par_titre(self, titre: str):
        return [livre for livre in self.livres if titre.lower() in livre.titre.lower()]

    def rechercher_par_auteur(self, auteur: str):
        return [livre for livre in self.livres if auteur.lower() in livre.auteur.lower()]

    def afficher_livres(self):
        for livre in self.livres:
            print(livre)
   
# Exemple d'utilisation
if __name__ == "__main__":
    b = Bibliotheque()

    livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "12345")
    livre2 = LivreNumerique("1984", "George Orwell", "67890", 2.5)

    b.ajouter_livre(livre1)
    b.ajouter_livre(livre2)

    print("📚 Tous les livres dans la bibliothèque :")
    b.afficher_livres()

    print("\n🔎 Recherche par titre '1984':")
    for l in b.rechercher_par_titre("1984"):
        print(l)

    print("\n🔎 Recherche par auteur 'Antoine':")
    for l in b.rechercher_par_auteur("Antoine"):
        print(l)

    print("\n❌ Suppression du livre ISBN 12345...")
    b.supprimer_par_isbn("12345")
    b.afficher_livres()
