# Ex2:
# 1.	Créer une classe Python nommée CompteBancaire qui représente un compte bancaire, ayant pour attributs : numeroCompte (type numérique ) , nom (nom du propriétaire du compte du type chaîne), & solde.
# 2.	Créer un constructeur ayant comme paramètres : numeroCompte, nom, solde.
# 3.	Créer une méthode Versement() qui gère les versements.
# 4.	Créer une méthode Retrait() qui gère les retraits.
# 5.	Créer une méthode Agios() permettant d’appliquer les agios à un pourcentage de 5 % du solde
# 6.	Créer une méthode afficher() permettant d’afficher les détails sur le compte
# 7.	Donner le code complet de la classe CompteBancaire.

class Comptebancaire :
    def __init__(self, n_compte , nom , solde, action):
        self.numero = n_compte
        self.nom = nom
        self.solde = solde
        self.action = action
    def affisage(self):
        print("Numero_compte", self.numero, "; Nom", self.nom, "; Solde=", self.solde)
    def versement (self, vers):
        self.solde = self.solde + vers
    def retrait (self , retr):
        self.solde = self.solde - retr
    def agios (self,):
        self.solde = self.solde + 0.05*self.solde

c1 = Comptebancaire(5555,"Iurie", 1000)
print("compte initiale")
c1.affisage()

print("retrait")
c1.retrait(100)
c1.affisage()

print("applique Agios de 5%")
c1.agios()
c1.agios()
c1.affisage()

print("Versement")
c1.versement(200)
c1.affisage()



