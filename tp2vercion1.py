'''
Traveau practique noumereau 2
Titre STM
'''
accueil = '''
=====================================================================
===================  Bienvenue a la STM   ===========================
=============  Categorie des Titre de transport : ===================
==                                                                 ==
==          P ----  passage                                        ==
==          S ---- Soirees : journees ou Fin de semaine            ==
==          C ---- abonnement :hebdo mensuel ou 4 mois             ==
==          G ---- Groupe                                          ==
==          A ---- Autre                                           ==
==          Q ---- Quitter                                         ==
=====================================================================
=============  Choisisser une categorie de titre  ===================
'''
print( accueil )

def saisir (mesage , caract):
    flag = 0
    i = 1
    saisirr = caract
    while flag == 0:
        titre = input( ).upper()
        for k in saisirr:
            if titre == k:
                flag = 1
        if flag == 0:
            print("Choix de catégorie erroné!",i,"-e essaye ")
            i = i + 1
        if i > 5:
            print(" nombre d'essai dépassé")
            flag = 1
            titre = "q"
    print(titre)

print(saisir("Choisissez le nombre de passages :" ,"123"))

"""
flag = 0
i = 1
saisir = "PSCGAQ"
while flag == 0:
    titre = input().upper()
    for k in saisir:
        if titre == k:
            flag = 1
    if flag == 0 :
        print( "Choix de catégorie erroné! ")
        i=i+1
    if i > 5 :
        print( " nombre d'essai dépassé" )
        flag = 1
        titre = "q"
print(titre)
"""