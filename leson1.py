# list4 = [10,20,30,40,50]
#
# #tri des element de la liste
# #inversion
# list4.reverse()
# print(list4)
#
# list1= [5,89,65,-6,55,64,-23,0,56,78,88]
# print(list1)
# list1.sort()
# print(list1)
#
# #list compreantion
#
# x1=  "vasile"
# print(x1)
#

#creer un list de nombre entier paire a partire du range (0,101)

x2 = [i for i in range(0, 101, 2)]
print(x2)
x=0
for i in range (0, len(x2)):
    x=x+1
    if x >= 10 :
        print("")
        x = 0
    print(x2[i], end=" ")

