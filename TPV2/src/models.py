class Livre:

    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"📘 {self.titre} — {self.auteur} (ISBN: {self.isbn})"


class LivreNumerique(Livre):

    def __init__(self, titre, auteur, isbn, taille_fichier):
        super().__init__(titre, auteur, isbn)
        self.taille_fichier = taille_fichier

    def __str__(self):
        return f"💻 {self.titre} — {self.auteur} (ISBN: {self.isbn}, {self.taille_fichier} Mo)"


class Bibliotheque:

    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]

    def rechercher_par_titre(self, titre):
        return [l for l in self.livres if titre.lower() in l.titre.lower()]

    def rechercher_par_auteur(self, auteur):
        return [l for l in self.livres if auteur.lower() in l.auteur.lower()]

    def __str__(self):
        if not self.livres:
            return f"📚 Bibliothèque '{self.nom}' — aucun livre"
        return f"📚 Bibliothèque '{self.nom}' contient {len(self.livres)} livre(s):\n" + \
               "\n".join(f" - {livre}" for livre in self.livres)
