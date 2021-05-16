#EXO LE PIC DANS UNE LISTE
list = []
enter = 10
while enter != '':
    enter = input('entrez un élément de la liste ')
    if enter == '' :
        break
    list.append(float(enter))
length = len(list)
if length >= 3:
    bool = 0 #l'observateur
    iter = 0 #l'itérateur
    for i in list:
        if iter >= 1 and iter <= (length - 2) :
            if list[iter] > list[iter-1] and list[iter] > list[iter+1] :
                bool = 1
                break
        iter = iter + 1
    if bool == 1 :
        print('il y a un pic')
    else :
        print('il y a pas de pîc')
else:
    print('la liste doit avoir au moins trois entrées')
