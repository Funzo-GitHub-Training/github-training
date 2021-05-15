# jeu de devinette
import random

n = random.randint(0,100)

appreciation = "?"

while True:
    var = input("Enter a number :")

    var = int(var)

    if var < n :

        appreciation = "wrong your number is lower than mine"
        print(var, appreciation)

    else :

        appreciation = "wrong your number is bigger than mine"
        print(var, appreciation)

    if var == n:

        appreciation = "you win !"

        print(var, appreciation)
        
        break
