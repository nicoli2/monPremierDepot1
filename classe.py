# paye

 #class Pays :
   # def __int__(self, pays , cont , capit , abit ):

s = 1

class Pays  : # pays / cont / capit / abit
    pays = ""
    cont = ""
    capit = ""
    abit = 0

p1 = Pays ()
p1.pays = "Italie"
p1.capit = "Roma"
p1.cont = "Europe"
p1.abit = 50

p2 = Pays()
p2.pays = "Inde"
p2.cont = "Asie"
p2.capit = "New Delhi"
p2.abit = 1430

# fonction (m/thdoe)
def afisaje(p) :
    print("Pays:" ,p.pays , ", Capitale: " ,p.capit , ", Condtinent: ", p.cont ,
          ", Nombre d'abitant:" ,p.abit ,"M")

afisaje(p1)
#print(afisaje(p2))

class PaysConstr:
    def __init__(self, a,b,c,d,):
        self.pays = a
        self.cont = b
        self.capit = c
        self.abit = d

    def afisConstr(self):
        print("Pays:", self.pays , ", Capitale: ", ", Condtinent: ",
              ", Nombre d'abitant:", self.abit, "M")


p1= PaysConstr("Italie", "Europe", "Roma", 50)


#def afisConstr(a):
 #   print("Pays:", a, ", Capitale: ", c, ", Condtinent: ", b,
  #        ", Nombre d'abitant:", d, "M")

p1.afisConstr()

objStr ="mot"
obj2 = str("alksfdjgh")
print(obj2.upper())
