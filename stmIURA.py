##########################################################
#  Ce programme traite la gestion des titre de passage   #
#             et d'abonnement de la STM                  #
#                 Réalisé Par :                          #
#                Hassan, BENSOUM                         #
#             Abdelmohssine, Almountacir                 #
#                  Iurie,  Nicolaev                      #
##########################################################


# Importer le module time pour utiliser la methode sleep()
import time

# Affichage des différentes options et Menus
menuPrincipal = """
***************************************************
*            Bienvenue à la STM                   *
*               Menu Principal                    *
*      Choisissez une catégorie de titre :        *
***************************************************
*    P    Passage                                 *
*    S    Soirées : Journées ou Fin de semaine    *
*    C    Abonnement : Hebdo, Mensuel ou 4 mois   *
*    G    Groupe                                  *
*    A    Autre   : YUL, Passage 747              *
*    Q    Quitter                                 *
***************************************************
"""

menuPassage = """
***************************************************
*         Bienvenue à la STM                      *
*             Menu Passage                        *
*      Choisissez un type de titre :              *
***************************************************
*    1    1 Passage                               *
*    2    2  Passages                             *
*    3    10  Passages                            *
*    Q    Quitter                                 *
***************************************************
"""

menuSoiree = """
***************************************************
*         Bienvenue à la STM                      *
*              Menu Soirée                        *
*      Choisissez un type de titre :              *
***************************************************
*    1      Soirée illimitée                      *
*    2      1 Journée                             *
*    3      Week-End illimité                     *
*    4      3 Jours                               *
*    Q      Quitter                               *
***************************************************
"""

menuAbonnement = """
***************************************************
*         Bienvenue à la STM                      *
*           Menu Abonnement                       *
*      Choisissez un type d'abonnement :          *
***************************************************
*    1      Hebdo                                 *
*    2      Mensuel                               *
*    3      4 Mois                                *
*    Q      Quitter                               *
***************************************************
"""

menuGroupe = """
***************************************************
*         Bienvenue à la STM                      *
*              Menu groupe                        *
*      Choisissez un type de titre :              *
***************************************************
*    1      Groupe (Adulte + 10 enfants)          *
*    Q      Quitter                               *
***************************************************
"""

menuAutre = """
***************************************************
*         Bienvenue à la STM                      * 
*              Menu Autre                         *
*      Choisissez un type de titre :              *
***************************************************
*    1      YUL Aéroport Mtl-Trudeau              *
*    2      Passage 747 Ouest                     *
*    Q      Quitter                               *
***************************************************
"""

menuCategorie = """
***************************************************
*         Bienvenue à la STM                      *
*            Menu catégorie                       *
*      Choisissez votre réduction :               *
***************************************************
*    1   Régulier                                 *
*    2   Enfant                                   *
*    3   Étudiant                                 *
*    4   +65 ans                                  *
*    Q   Quitter                                  *
***************************************************
"""

modepayment = """
***************************************************
*         Bienvenue à la STM                      *
*            Mode de paiement                     *
*      Choisissez un type de paiement :           *
***************************************************
*    1      Espece                                *
*    2      Carte                                 *
***************************************************
"""

# Messages d'erreure et remerciement
desole = """
***************************************************
*************          Désolé         *************
ce titre n'est pas disponible pour cette catégorie
***************************************************
"""

invalide = """
***************************************************
**********    Ce choix est invalide     ***********
***************    Réessayer    ********************
***************************************************
"""

merci = """
***************************************************
**********   M E R C I d'avoir choisi    **********
***************     S. T. M.   ********************
**************  Fin du programme    ***************
***************************************************
"""


# Vérification du mode de paiement
def paiement():
    while True:
        print(modepayment)
        pay = input("Choisissez un mode de paiment : ").upper()
        if pay == "1":
            print("")
            print("!!! Merci pour votre payment en Espece !!!")
            print("")
            print("        !!! Voici votre Titre !!!")
            time.sleep(3)
            break
        elif pay == "2":
            print("")
            print("!!! Merci pour votre paiment en carte de credit !!!")
            print("")
            print("        !!! Voici votre Titre !!!")
            time.sleep(3)
            break
        else:
            print(invalide)
            time.sleep(3)


# Calcule de la Facture à payer
def facture(prix):
    tps = prix * 0.07
    tvq = (prix + tps) * 0.15
    netapayer = prix + tps + tvq
    return prix, tps, tvq, netapayer


# Impression du titre acheter
def imprimepass(passe, cat, prix, tps, tvq, netapayer):
    print("")
    print("******************************************")
    print("******************************************")
    print("******          TITRE STM           ******")
    print("******************************************")
    print("******************************************")
    print("")
    print("         Type: ", passe )
    print("         Réduction : ", cat)
    print("")
    print("    Prix        : ", "%.2f" % prix, " $" )
    print("    TPS         : ", "%.2f"  % tps, "$")
    print("    TVQ         : ", "%.2f" % tvq, " $")
    print("    Net à payer : ", "%.2f" % netapayer, " $")
    print("")
    print("******************************************")
    print("******************************************")
    print("")
    print(merci)
    exit()


# Déterminer le type de réduction
def categorie(mesage):
    while True:
        print(menuCategorie)
        cat = input(mesage).upper()
        if cat == "1":
            return "1"
        elif cat == "2":
            return "2"
        elif cat == "3":
            return "3"
        elif cat == "4":
            return "4"
        elif cat == "Q":
            return "Q"
        else:
            print(invalide)
            time.sleep(3)


def categorie1(mesage):
    while True:
        cat = input(mesage).upper()
        if cat == "1":
            return "1"
        elif cat == "2":
            return "2"
        elif cat == "3":
            return "3"
        elif cat == "4":
            return "4"
        elif cat == "Q":
            return "Q"
        else:
            print(invalide)
            time.sleep(3)

def typef (choix, type1, type2, type3, type4):
    if choix == "1":
        type = type1
    elif choix == "2":
        type = type2
    elif choix == "3":
        type = type3
    elif choix == "4":
        type = type4
    else:
        type =1
    return type

def repete1(passe, cat, prix):
    cat = typef(cat, "Régulier", "Enfant", "", "+65 Ans")
    paiement()
    prix, tps, tvq, netapayer = facture(prix)
    imprimepass(passe, cat, prix, tps, tvq, netapayer)



# Traitement de l'option passage du menu principal
def passage():
    while True:
        print(menuPassage)
        passe = input("Choisissez une catégorie de Passage : ").upper()
        if passe == "1":
            passe = "1 Passage"
            cat = categorie("Choisissez votre categorie de réduction : ")
            prix = typef(cat, 3.50,2.50, "" ,1.00)
            if cat == "3":
                print(desole)
                time.sleep(3)
            elif cat == "Q":
                pass
            else:
                repete1(passe,cat,prix)
        elif passe == "2":
            passe = "2 Passages"
            cat = categorie("Choisissez votre categorie de réduction : ")
            prix = typef(cat, 6.50, 4.25, "", 2.00)
            if cat == "3":
                print(desole)
                time.sleep(3)
            elif cat == "Q":
                pass
            else:
                repete1(passe,cat,prix)
        elif passe == "3":
            passe = "10 Passages"
            cat = categorie("Choisissez votre categorie de réduction : ")
            prix = typef(cat, 30, 19, "", 9.00)
            if cat == "3":
                print(desole)
                time.sleep(3)
            elif cat == "Q":
                pass
            else:
                repete1(passe, cat, prix)
        elif passe == "Q":
            break
        else:
            print(invalide)
            time.sleep(3)


# Traitement de l'option menu Soirée du menu principal
def soiree():
    while True:
        print(menuSoiree)
        passe = categorie1("Choisissez une catégorie de Passage : ")
        prix = typef(passe,5.75, 10, 14.5, 20.5)
        if passe == "Q":
            break
        else:
            passe = typef(passe, "Soirée", "1 Jour", "Week-End", "3 Jours")
            paiement()
            prix, tps, tvq, netapayer = facture(prix)
            descrip = "--------"
            imprimepass(passe, descrip, prix, tps, tvq, netapayer)


# Traitement de l'option des abonnements du menu principal
def abonnement():
    while True:
        print(menuAbonnement)
        passe = input("Choisissez une catégorie de Passage : ").upper()
        if passe == "1":
            passe = "Hebdo"
            cat = categorie("Choisissez votre categorie de réduction : ")
            prix = typef(cat, 28, 16.75,0 , 8.5)
            if cat == "3":
                print(desole)
                time.sleep(3)
            elif cat == "Q":
                pass
            else:
                repete1(passe, cat, prix)
        elif passe == "2":
            passe = "Mensuel"
            cat = categorie("Choisissez votre categorie de réduction : ")
            prix = typef(cat, 90.5, 54, 54, 27)
            if cat == "Q":
                pass
            else:
                repete1(passe, cat, prix)
        elif passe == "3":
            passe = "4 Mois"
            cat = categorie("Choisissez votre categorie de réduction : ")
            prix = typef(cat, 0, 212, 212, 106)
            if cat == "1":
                print(desole)
                time.sleep(3)
            elif cat == "Q":
                pass
            else:
                repete1(passe, cat, prix)
        elif passe == "Q":
            break
        else:
            print(invalide)
            time.sleep(3)


# Traitement de l'option Autre du menu principal
def autre():
    while True:
        print(menuAutre)
        passe = input("Choisissez une catégorie de Passage : ").upper()
        if passe == "1":
            passe = "YUL Aéroport MTL-Trudeau"
            paiement()
            prix, tps, tvq, netapayer = facture(10)
            descrip = "--------"
            imprimepass(passe, descrip, prix, tps, tvq, netapayer)
        elif passe == "2":
            passe = "Passage 747 Ouest"
            paiement()
            prix, tps, tvq, netapayer = facture(10)
            descrip = "--------"
            imprimepass(passe, descrip, prix, tps, tvq, netapayer)
        elif passe == "Q":
            break
        else:
            print(invalide)
            time.sleep(3)


# Traitement de l'option groupe du menu principal
def groupe():
    while True:
        print(menuGroupe)
        passe = input("Choisissez une catégorie de Passage : ").upper()
        if passe == "1":
            passe = "Groupe"
        elif passe == "Q":
            break
        else:
            print(invalide)
            time.sleep(3)
        paiement()
        prix, tps, tvq, netapayer = facture(10)
        descrip = "--------"
        imprimepass(passe, descrip, prix, tps, tvq, netapayer)


# Traitement du menu principale
def principale():
    while True:
        print(menuPrincipal)
        choix = input("Choisissez une option du Menu Principal : ").upper()
        if choix == "P":
            passage()
        elif choix == "S":
            soiree()
        elif choix == "C":
            abonnement()
        elif choix == "A":
            autre()
        elif choix == "G":
            groupe()
        elif choix == "Q":
            break
        else:
            print(invalide)
            time.sleep(3)


# Programme principale
principale()
print("")
print(merci)
