menus = ['pistache', 'arachide', 'tomate', 'combo']
user_count = 5
resto_count = 5
resto_iter = 0

list = []

print(menus)

while resto_iter < resto_count :
    user_iter = 0
    lst = ['jour '+str(resto_iter+1), []]
    print('H1', 'jour '+str(resto_iter+1))
    while user_iter < user_count :
        u = 'user '+str(user_iter+1)
        l = [u]
        user_plat = input('entrez le numero du menu du user numero '+str(u)+'   ')
        l.append(int(user_plat))
        lst[1].append(l)
        user_iter = user_iter + 1
    list.append(lst)
    resto_iter = resto_iter + 1

print(list)