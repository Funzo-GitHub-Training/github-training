import random
cMagic = random.randint(0, 100) 

while True:
    Unumber = int(input("Entrer un nombre entre 0 et 100: "))
    if cMagic == Unumber:
        print("Youpi!!!!  You're the best!\n")
        break
    elif Unumber < cMagic :
        res= input("Oups!!!! Votre nombre est plus petit!\n Voulez vous continuer?y=Oui/autre=Non:")
        if (res != 'y'):
            print("Merci d'avoir joué avec moi, Byeeeeeeeeeeeeee!")
            break
    else:
        res= input("Oups!!!! Votre nombre est plus grand!\n Voulez vous continuer?y=Oui/autre=Non:")
        if (res != 'y'):
            print("Merci d'avoir joué avec moi, Byeeeeeeeeeeeeee!")
            break