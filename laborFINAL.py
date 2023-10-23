# Programme qui demande à l’utilisateur de taper 10 entiers et qui affiche le plus
# petit de ces entiers et le max (sans utiliser d’algorithme de tri ou de librairies externes).
#

def exrcise1():
    tab = []
    taillTab = int(input("saisir la taille du tableau "))
    for i in range(0, taillTab):
        print("saisir element ", i, " de tableau ")
        tab.append(i)
        tab[i] = int(input())
    maxt = tab[0]
    mint = tab[0]
    for i in range(0, taillTab):
        if tab[i] > maxt:
            maxt = tab[i]
        if tab[i] < mint:
            mint = tab[i]
    print(tab)
    print(" Min = ", mint, ":  Max = ", maxt)


def exercise4():
    nomeleve = input("saisir le nom d'eleve si non saisir N  ")
    s= 0
    while nomeleve != "N" and nomeleve != "n" :
        i=0
        min = 20
        max = 0
        n = int(input("saisir les nombre des cours etudié "))
        while i < n:
            note = int(input("saisir les note des cours "))
            if note >= 0 and note<= 20:
                if note < min :
                    min = note
                if note > max :
                    max = note
                s = s + note
                i +=1
            else:
                print("saisir errone")
        print(nomeleve,"a la somme des note :", s)
        print(nomeleve, "a le note minimale:",min," ,a le note maximale:" ,max, "et le moyen:", s/n)
        if s/n >= 18:
            seuil = "Excelent"
        elif s/n >= 16:
            seuil = "Bon"
        elif s/n >= 12:
            seuil = "Moyen"
        else:
            seuil = "Insufisant"
        print(nomeleve, " a une note ---", seuil, " ---")
        nomeleve = input("saisir le nom d'eleve si non saisir N  ")



def saisir1():
    note = []
    for i in range(6):
        note.append(0)
    print(note)
    note = input("sasir les 6 note comprit intre 0 et 20 separe de virgule : ")
    print(note)

#saisir1()





class Eleves: #nomeleve,nomcours, notes
    def __init__(self,notes=0):
        self.notes = notes
    def saisirnote(self, n ):
        i, s= 0 , 0
        min = 20
        max=0
        while i <= n:
            print("saisir la note de cours N% ", i)
            notes = int(input())
            if notes >= 0 and notes <= 20:
                i +=1
                s=s+notes
                if notes < min :
                    min = notes
                if notes > max :
                    max = notes
        print( "eleve a la somme des note :", s)
        print("eleve a le note minimale:", min, " ,a le note maximale:", max, "et le moyen:", s / n)
        if s / n >= 18:
            seuil = "Excelent"
        elif s / n >= 16:
            seuil = "Bon"
        elif s / n >= 12:
            seuil = "Moyen"
        else:
            seuil = "Insufisant"
        print("eleve a une note ---", seuil, " ---")

    def resultat(self):
        pass

e1 = Eleves()
print(e1)
e1.saisirnote(6)

