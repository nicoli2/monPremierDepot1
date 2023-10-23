#           TP2   Titre STM
# Distributrice automatique de titre de transport

menuPrincipal = """
*      Choisissez une catégorie de titre :        *
***************************************************
*    P      passage                               *
*    S      Soirées : journées ou Fin de semaine  *
*    C      abonnement :  hebdo mensuel ou 4 mois *
*    G      Groupe                                *
*    A      Autre                                 *
*    Q      Quitter                               *
***************************************************
"""

menuPassage = """
*    1            1   passage                     *
*    2            2   passages                    *
*    3            10  passages                    *
*    Q            Quitter                         *
***************************************************
"""
menuPassageReduction = """
* reductio **            passage   1        2       10    *
*    1    Tarif Ordinaire         3.50$    6.50   30.00$  *
*    2    Ecolier 6-18 ANS        2.50$    4.25   19.00$  *
*    3    Etudiant 18 ANS +        --       --      --    *
*    4    65 ANS +                1.00$    2.00$   9.00$  *      
*    Q          Quitter                                   *
***********************************************************
"""

menuSoiree = """
***************************************************
*             Menu Soirée                         *
*      Choisissez un type de titre :              *
***************************************************
*    1      Soirée illimitée (18h à 5h)    5.75$  *
*    2      1 jour (24h)                  10.00$  *
*    3      Week-end illimité             14.50$  *
*    4      3 jours                       20.50$  *
*    Q      Quitter                               *
***************************************************
"""

menuAbonnement = """
***************************************************
*               Menu Abonnement                   *
*      Choisissez un type d'abonnement :          *
***************************************************
*    1                   Hebdo                    *
*    2                   Mensuel                  *
*    3                   4 Mois                   *
*    Q                   Quitter                  *
***************************************************
"""
menuAbonementReduction = """
* reductio ***** ***    Titre  hebdo   mensuel   4 Mois   *
*    1    Tarif Ordinaire      28.00$   90.50$     --     *
*    2    Ecolier 6-18 ANS     16.75$   54.00$   212.00$  *
*    3    Etudiant 18 ANS +      --     54.00$   212.00$  *
*    4    65 ANS +              8.50$   27.00$   106.00$  *      
*    Q          Quitter                                   *
***********************************************************
"""
menuGroupe = """
*    1      Groupe (Adulte + 10 enfants) 19.00$   *
*    Q      Quitter                               *
***************************************************
"""

menuAutre = """
*    1      YUL Aéroport Mtl-Trudeau     10.00$   *
*    2      Passage 747 Ouest            10.00$   *
*    Q      Quitter                               *
***************************************************
"""

menux = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *"""

menux1 = """
*      Choisissez un type de titre :              *
***************************************************"""

menuxr = """
***********************************************************
*                 Bienvenue à la STM                      *
*              Catégorie des Titre de transport :         *
*              Choisissez un reduction :                  *
***********************************************************"""



def ecuatie (pChoix1,pChoix2,pChoix3,pChoix4,choix ):
    if choix == "1":
        prix = pChoix1
    elif choix == "2":
        prix = pChoix2
    elif choix == "3":
        prix = pChoix3
    elif choix == "4":
        prix = pChoix4
    else:
        prix = -1
    return prix

def tarif (choix):
    if choix == "1":
        tar = "Tarif Ordinaire"
    elif choix == "2":
        tar = "Enfant  6-11 ANS   12-17 ANS  "
    elif choix == "3":
        tar = " ÉTUDIANTS 18 ANS ET +  "
    elif choix == "4":
        tar = " 65 ANS ET +   "
    return tar

def saisirCorect (mesage , caract):
    flag = 0
    saisirr = caract
    while flag == 0:
        titre = input(mesage).upper()
        for k in saisirr:
            if titre == k:
                flag = 1
        if flag == 0:
            print("Choix de catégorie erroné!")
    return titre

def typef (choix, type1, type2, type3, type4):
    if choix == "1":
        type = type1
    elif choix == "2":
        type = type2
    elif choix == "3":
        type = type3
    elif choix == "4":
        type = type4
    return type


tar = "Tarif Ordinaire"
print(menux + menuPrincipal)
prix = 0
flag = 1
while flag == 1:
    flag = 0
    choix = input("Choisissez une catégorie d'abonnement : ").upper()
 # Choix catégorie passages
    if choix == "P":
        print(menux + menux1 + menuPassage)
        nombreDePassage = saisirCorect("Choisissez le nombre de passages :", "123Q")
        if nombreDePassage != "Q":
            print(menuxr + menuPassageReduction)
            reduction = saisirCorect("Choisissez une catégorie de reduction :", "1234Q")
            tar = tarif(reduction)
            type = typef(nombreDePassage, "1 passage", "2 passages", "10 passages", " ")
            if reduction !="Q":
                if nombreDePassage == "1":
                    prix = ecuatie(3.5, 2.5, -1, 1, reduction)
                elif nombreDePassage == "2":
                    prix = ecuatie(6.5, 4.25, -1, 2, reduction)
                elif nombreDePassage == "3":
                    prix = ecuatie(30, 19, -1, 9, reduction)
# Choix catégorie de soire
    elif choix == "S":
        print(menuSoiree)
        soire = saisirCorect("Choisissez une catégorie de soire : ", "1234Q")
        if soire != "Q":
            prix = ecuatie(5.75, 10, 14.5, 20.5, soire)
            type = typef (soire,"Soirée illimitée (18h à 5h)", "1 jour (24h)"," Week-end illimité  ",
                         " 3 Jours " )
# Choix catégorie de abonement
    elif choix == "C":
        print(menuAbonnement)
        abonnement = saisirCorect("Choisissez une catégorie de abonement : ", "123Q")
        if abonnement != "Q":
            print(menuxr + menuAbonementReduction)
            reduction = saisirCorect("Choisissez une catégorie de reduction : ", "1234Q")
            tar = tarif(reduction)
            type = typef(abonnement, "Hebdo", "Mensuel", "4 Mois", " ")
            if reduction !="Q":
                if abonnement == "1":
                    prix = ecuatie(28, 16.75, -1, 8.5, reduction)
                elif abonnement == "2":
                    prix = ecuatie(90.5, 54, 54, 27, reduction)
                elif abonnement == "3":
                    prix = ecuatie( -1 , 212, 212, 106, reduction)
# Choix catégorie Groupe
    elif choix == "G":
        print(menux + menux1 + menuGroupe)
        type = " Groupe"
        prix = 19
# Choix catégorie Autre
    elif choix == "A":
        print(menux + menux1 + menuAutre)
        autre = saisirCorect("Choisissez une catégorie de titre : ", "12Q")
        if autre !="Q":
            prix = 10
            type = typef(autre, "YUL Aéroport Mtl-Trudeau", "Passage 747 Ouest ", " ", " ")
    elif choix == "Q":
        pass
    else:
        print("Choix de catégorie erroné!")
        flag = 1
#Affichage Prix
print("---------------------------------------------------")
print("***************************************************")
if prix > 0:
    print("*      Categorie : Titre ")
    print("*      Type : ", type)
    print("*      Tarif: ", tar)
    print("*")
    print("*      Prix avant taxes : ", prix * 0.85, " $ ")
    print("*      TPS              : ", prix * 0.05, " $ ")
    print("*      TVQ              : ", prix * 0.10, " $ ")
    print("*      Prix a payer     : ", prix ," $ ")
elif prix == 0:
    pass
else:
    print("*    Désolé, Nous n’avons pas ce type de choix!")
print("*")
print ("*    Merci d'avoir choisi STM ")
print("***************************************************")

