
def ligne (n , carract ):
    for i in range (0 , n ):
        print(carract, end=" ")

#ligne(5 , "**")


def carre( n ):
    for i in range (0,n):
        ligne(n, "**")
        print()


carre(5)


def carrev1( n , carract):
    for i in range (0,n):
        ligne(n, carract)
        print()







carrev1(5, "***")
