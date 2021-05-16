# EXO RECTANGLE
import math

valeur1 = input("entrée la valeur de a: ")
valeur2 = input("entrée la valeut de b: ")
valeur3 = input("entrée la valeur de c: ")
valeur4 = input("entrée la valeur de d: ")
valeur5 = input("entrée la valeur de e: ")
print('votre liste est: ')
list = [valeur1, valeur2, valeur3, valeur4, valeur5]
list.sort()
print(list)
L = list[0:3]
print('votre nouvelle liste est : ')
print(L)
print('le couple valide est : ', (L[0],L[1]))
largeur = L[0]
longueur = L[1]
print('la largeur est : ', largeur)
print('la longueur est : ', longueur)
diagonale = math.sqrt((int(largeur)**2) + (int(longueur)**2))
print('la diagonale est : ', diagonale)
perimetre = (int(longueur)+int(largeur))*2
print('le perimetre est : ', perimetre)
Aire = int(longueur)*int(largeur)
print("l'aire est : ", Aire)


