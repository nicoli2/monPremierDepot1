
def verificationSaisir (nombre, limitBas, limitHaut):
    """verifier si les element tableau saisi est compris entre limitBas et limitHaut
    et retun un tableau note1"""
    note = saisir2(nombre)
    while True:
        k, i = 0, 0
        while i < (len(note)):
            if note[i] < limitBas or note[i] > limitHaut:
                k=k+1
                note.pop(i)
            else:
                i = i + 1
        if k==0:
            note1 = note
            print("note corect = ", note1)
            return note1
        nombre = k
        note1 = note
        print("note = ", note1)
        note1 = note.extend(saisir2(nombre))

def saisir2(nombre):
    """ Saisi un tableaux de longeur 'nombre' """
    note = []
    for i in range(nombre):
        note.append("")
    print("sasir ", nombre , " note comprit intre 0 et 20 separe d'espace: ")
    i = 0
    k=1
    while True :
        note1 = input() + " "
        for x in note1:
            if x != " ":
                note[i] =note[i] + x
                k = 0
            else:
                if k == 0:
                    i = i + 1
                    k = 1
            if i >= nombre :
                break
        if i >= nombre:
            break
        else:
            print("sasir ", nombre - i , " note manquante ")
    for i in range(nombre):
        note[i] =int(note[i])
    return note

note1 = verificationSaisir(6 , 0 ,30)

