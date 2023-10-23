# classe legume / fruite / cereales
"""
    n1 = "tomate" / "cerise" / "mais"
    n2 ="chou"/"pomme"/"avoine"
    n3 = "carotte"/"ananas"/"riz"
    n4 = "poivron"/"citron"/"ble"
       """
class Nuriture:
    legume = ""
    fruite = ""
    cereales = ""


n1 = Nuriture()
n1.legume = "tomate"
n1.fruite = "cerise"
n1.cereales = "mais"

n2 = Nuriture()
n2.legume = "carotte"
n2.fruite = "pomme"
n2.cereales = "avoine"
#n3 = Nuriture()

print (Nuriture)
print (n2.legume , n1.legume )
print (n2.legume + n1.legume )

# classe legume / fruite / cereales avec constructeur

class Nuriture1 :
     def __init__(self, nlegume, nfruit, ncereale, nquantite):
         self.legume = nlegume
         self.fruit = nfruit
         self.cereale = ncereale
         self.quantite = nquantite
     def printn(self,difer):
         print("cantite ", self.quantite, "fruit ",self.fruit, self.legume, difer)
     def calcule_d(self,difer,egal):
         #egal = difer + self.quantite
         for i in range (difer):
             self.quantite = self.quantite - egal
             n5.printn(difer)

n5 = Nuriture1("poivron","citron","ble",1000)
n5.printn(5)
n5.calcule_d(20,10)

n5.printn(333)
n5.printn(n5.quantite)
print(n5.quantite)
#x = calcule.self
#print(x)