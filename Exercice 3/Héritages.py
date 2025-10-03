#Véhicule ->marque modele
#   Voiture ->nombre de porte
#   Moto ->type de moteur

class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def i(self):
        return f"Marque: {self.marque}, Modèle: {self.modele}"


class Voiture(Vehicule):
    def __init__(self, marque, modele, nb_portes):
        super().__init__(marque, modele)   
        self.nb_portes = nb_portes

    def infos(self):
        return f"{super().i()}, Portes: {self.nb_portes}"


class Moto(Vehicule):
    def __init__(self, marque, modele, type_moteur):
        super().__init__(marque, modele)
        self.type_moteur = type_moteur

    def infos(self):
        return f"{super().i()}, Moteur: {self.type_moteur}"


# Exemple
v = Voiture("Peugeot", "308", 5)
m = Moto("Yamaha", "R1", "4 temps")

print(v.infos())
print(m.infos())
