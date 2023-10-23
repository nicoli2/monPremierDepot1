menuPrincipal = """
***************************************************
*        Bienvenue à la STM                       *
*      Catégorie des Titre de transport :         *
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
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type de titre :              *
***************************************************
*    1      1                               3$    *
*    2      2                               6$    *
*    3      10                              30$   *
*    Q      Quitter                               *
***************************************************
"""

menuSoiree = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type de titre :              *
***************************************************
*    1      1                           5.75$     *
*    Q      Quitter                               *
***************************************************
"""

menuAbonnement = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type d'abonnement :          *
***************************************************
*    1      1                            Hebdo    *
*    2      2                            Mensuel  *
*    Q      Quitter                               *
***************************************************
"""

menuGroupe = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type de titre :              *
***************************************************
*    1      Groupe (Adulte + 10 enfants) 19.00$   *
*    Q      Quitter                               *
***************************************************
"""

menuAutre = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type de titre :              *
***************************************************
*    1      YUL Aéroport Mtl-Trudeau     10.00$   *
*    2      Passage 747 Ouest            10.00$   *
*    Q      Quitter                               *
***************************************************
"""

menuHebdo = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type d'abonnement:           *
***************************************************
*    1      1                            28.00$   *
*    2      2                            16.75$   *
*    3      10                             8.5$   *
*    Q      Quitter                               *
***************************************************
"""

menuMensuel = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type d'abonnement :          *
***************************************************
*    1      1                            90.00$   *
*    2      2                            54.00$   *
*    3      10                           54.00$   *
*    3      10                           27.00$   *
*    Q      Quitter                               *
***************************************************
"""

menu4Mois = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez un type de titre :              *
***************************************************
*    1      6-11 ANS   12-17 ANS        212.00$   *
*    2      ÉTUDIANTS 18 ANS ET +       212.00$   *
*    3      65 ANS ET +                 106.00$   *
*    Q      Quitter                               *
***************************************************
"""

menuCategorie = """
***************************************************
*         Bienvenue à la STM                      *
*      Catégorie des Titre de transport :         *
*      Choisissez votre réduction :               *
***************************************************
*    1                           Enfant           *
*    2                           Étudiant         *
*    3                           +65 ans          *
*    Q   Quitter                                  *
***************************************************
"""

print(menuPrincipal)



flag = 1
while flag == 1:
    choix = input("Choisissez une catégorie d'abonnement : ").upper()
    if choix == "P":
        print(menuPassage)
        flag = 0
        nombreDePassage = input("Choisissez le nombre de passages :").upper()
        if nombreDePassage != "Q":
            reduction = input("Choisissez une catégorie de reduction : ").upper()
            if reduction != "Q":
                if reduction == "1":
                    if nombreDePassage == "1":
                        prix = 2.50
                    elif nombreDePassage == "2":
                        prix = 4.25
                    elif nombreDePassage == "3":
                        prix = 19.00
                    else:
                        prix = 0
                        print("Choix erroné!")
                elif reduction == "2":
                    if nombreDePassage == "1":
                        prix = 1.00
                    elif nombreDePassage == "2":
                        prix = 2.00
                    elif nombreDePassage == "3":
                        prix = 9.00
                    else:
                        prix = 0
                        print("Choix erroné!")
                elif reduction == "3":
                    if nombreDePassage == "1":
                        prix = 3.50
                    elif nombreDePassage == "2":
                        prix = 6.50
                    elif nombreDePassage == "3":
                        prix = 30.00
                    else:
                        prix = 0
                        print("Choix erroné!")
            else:
                prix = 0
        else:
            prix = 0
    elif choix == "S":
        print(menuSoiree)
        flag = 0
    elif choix == "C":
        print(menuAbonnement)
        flag = 0
    elif choix == "G":
        print(menuGroupe)
        flag = 0
    elif choix == "A":
        print(menuAutre)
        flag = 0
    elif choix == "Q":
        #print(quitter)
        flag = 0
    else:
        print("Choix de catégorie erroné!")
print("Votre prix = " , prix , " $ ")
print ("Fin du programme")




