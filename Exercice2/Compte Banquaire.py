class CompteBanquaire:

    def __init__(self, titulaire: str, solde_initial: float = 0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant : float):
        if montant > 0 :
            self.solde += montant
            print("Le montant deposé est de :", montant)
        else:
            print ("Montant incorrect")
    
    def retirer(self, montant: float):
        if montant <= 0 or montant > self.solde :
            print("Retrait impossible, pour manque de fond")
        else :
            self.solde -= montant
            print(f"Retrait de {montant} effectué")

#Exemple
compte1 = CompteBanquaire("Alice", 100)
compte1.deposer(500)
compte1.retirer(94)
print(compte1.solde)