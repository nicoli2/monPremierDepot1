"""
# exemple 1
nom = input("Saisir votre nom svp.")
print("Bienvenu " + nom)


# Exemple 2
a = int (input("Saisir a "))
b = int (input("saisir b "))
print("Resultat de a + b = ", a+b)

# Exemple 3
a = int (input("Saisir a "))
b = int (input("saisir b "))
if a>b :
    print("Max = ", a )
else:
    print("Max = ", b)

# Exemple 5

a = int (input("Saisir votre nombre "))
b = a/2 - int(a/2)
if b == 0 :
    print("Le nombre saisie est PAIRE ")
else:
    print("Le nombre saisie est IMPAIRE ")

# Exemple 4

k=0
for i in range(10):
    for j  in range(10):
        print(k, end=" : ")
        k = k + 1
    print()


# Exemple 6


if x>=18:
    print("« vous êtes Majeur ! »")
else:
    print("« vous êtes mineur ! »")


# Exemple 7
x=[]
n = int(input("Combien des nombre vous voulez saisir "))
for i in range(n):
    print("Saisie x [", i, "] = ", end= "")
    x.insert(i, int(input()))
print("x[i] = ", x)
nmax =x[0]
for i in range(n):
    if x[i]>nmax:
        nmax = x[i]
print("Nombre max est ", nmax)
"""
# Exemple 8
n = int(input("Saisir un nombre  "))
sum = 0
for i in range(n):
    sum=sum + i
print("Sum = ", sum)

# Exemple 9

n = int(input("Saisir un nombre  "))
nFact = 1
for i in range(1, n):
    nFact=nFact * i
print("nFact = ", nFact )

r = int(input(" saisir le rayon d'un cercle "))
perimetr = 2*nombre