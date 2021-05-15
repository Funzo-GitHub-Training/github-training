# conference

import random

participants = ['john', 'jean', 'paul', 'paulin', 'pauline', 'flore', 'germaine', 'parfaits', 'duck', 'tchana', 'tsale', 'corine', 'damiene', 'chantal', 'maeva',
                'victorine', 'chanelle', 'carrine', 'junior', 'maxime']


dict1 = {'resto1': [], 'resto2': [], 'resto3': [], 'resto4': [], 'resto5': []}

list_menu = []

menu_count = []

for i in range(1,6):#les 5 nombres de resto

    choice = random.sample(range(1,9),k=4) #choix de 4 nombre parmis 8

    menus = ['menu_' + str(x) for x in choice]

print(choice)

print(menus)


plats={}

list_plats_j=[]

for i in range(20):

    choix=random.choice(menus)

    list_plats_j.append(choix)

    dict1['resto' + str(j)].append({'name': participants[i], 'plat': choix})

print(list_plats_j)


list_menu.append(list_plats_j)

menu_count_j=[list_plats_j.count(x) for x in ['menu_' + str(k) for k in range(1,9)]]

menu_count.append(menu_count_j)

print(menu_count_j)

print(menu_count)

total_count = []

for k in range(8):
    total_count.append(menu_count[0][k] + menu_count[1][k] + menu_count[2][k] +
                       menu_count[3][k] + menu_count[4][k])

print(total_count)

top_choice = total_count.index(max(total_count))

print("Popular Menu Consumed :", max(total_count), "times and is Menu_", top_choice + 1)
