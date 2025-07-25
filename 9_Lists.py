#######################################################################
#######################   Lists
#######################################################################


#######################################################################

# names = ["Mohamed", "Ayoub", "Hassan", "Mourad", "Houda"]

# print(f"Names : {names}")


#######################################################################

# names = ["Mohamed", "Ayoub", "Hassan", "Mourad", "Houda"]

# for name in names:
#     print(f"Name  : {name}")
# print(f"longueur de la liste : {len(names)}")

# #######################################################################

# names = ["Mohamed", "Ayoub", "Hassan", "Mourad", "Houda"]

# for index,name in enumerate(names):
#     print(f"Name {index} : {name}")

# print(f"longueur de la liste : {len(names)}")



#######################################################################
### Append("element")  : permet d'ajouter un element a la fin de la liste
# names = ["Mohamed", "Ayoub", "Hassan", "Mourad", "Houda"]

# names.append("Khalid")

# print(f"Names : {names}")

# #######################################################################
# ### insert(index, "element")  : insère un élément à une position donnée
# names = ["Mohamed", "Ayoub", "Hassan", "Mourad", "Houda"]

# names.insert(2, "Yassine")

# print(f"Names : {names}")


# #######################################################################
# ### extend(["e1", "e2"])  : ajoute plusieurs éléments à la fin de la liste
# names = ["Mohamed", "Ayoub", "Hassan"]

# names.extend(["Imane", "Samir"])

# print(f"Names : {names}")


# #######################################################################
# ### remove("element")  : supprime la première occurrence de l’élément
# names = ["Mohamed", "Ayoub", "Hassan", "Ayoub"]

# names.remove("Ayoub")

# print(f"Names : {names}")


# #######################################################################
# ### pop()  : supprime et retourne le dernier élément de la liste
# names = ["Mohamed", "Ayoub", "Hassan"]

# last = names.pop()

# print(f"Dernier : {last}")
# print(f"Names : {names}")



# #######################################################################
# ### pop(index)  : supprime et retourne l’élément à l’index donné
# names = ["Mohamed", "Ayoub", "Hassan"]

# removed = names.pop(1)

# print(f"Supprimé : {removed}")
# print(f"Names : {names}")



# #######################################################################
# ### clear()  : supprime tous les éléments de la liste
# names = ["Mohamed", "Ayoub", "Hassan"]

# names.clear()

# print(f"Names : {names}")


# #######################################################################
# ### index("element")  : retourne l’index de la première occurrence
# names = ["Mohamed", "Ayoub", "Hassan"]

# i = names.index("Ayoub")

# print(f"Index de Ayoub : {i}")



#######################################################################
### count("element")  : compte le nombre d’occurrences de l’élément
# names = ["Mohamed", "Ayoub", "Hassan", "Ayoub"]

# c = names.count("Ayoub")

# print(f"Nombre de Ayoub : {c}")



#######################################################################
### sort()  : trie la liste en ordre croissant
# names = ["Mohamed", "Ayoub", "Hassan"]

# names.sort()

# print(f"Names triés : {names}")



#######################################################################
### sort(reverse=True)  : trie la liste en ordre décroissant
# names = ["Mohamed", "Ayoub", "Hassan"]

# names.sort(reverse=True)

# print(f"Names décroissants : {names}")


#######################################################################
### reverse()  : inverse l’ordre des éléments
# names = ["Mohamed", "Ayoub", "Hassan"]

# names.reverse()

# print(f"Names inversés : {names}")



#######################################################################
### copy()  : retourne une copie superficielle de la liste
# names = ["Mohamed", "Ayoub", "Hassan"]

# copie = names.copy()

# print(f"Copie : {copie}")




#######################################################################





#######################################################################

# qt = "oui"
# mht_list = []
# somme = 0

# nom = input('Tapez votre nom  :   ')

# # remplir la liste
# while qt == "oui":
#     mht = float(input('Saisir un Monant HT : '))
#     mht_list.append(mht)
#     qt = input('Voulez vous continuez ? oui/non :   ')


# print(f'Mon list est :  {mht_list}')

# for mt in mht_list:
#     somme = somme + mt

# print('Somme : ', somme)
# ttc = somme + somme*0.2

# nb = len(mht_list)
# print('len list : ', nb)
# moyenne = somme/(nb)

# print(50*'*')   
# print(f'Nom : {nom}')







# #######################################################################
names_list = []
niveau_list = []
math_list= []
pc_list = []
svt_list = []
mention_list = []
moy_list = []
condition_list = []

qt="oui"
while qt=='oui':
    name=input("tapez votre nom: ")
    names_list.append(name)

    niveau=input("tapez votre niveau : ")
    niveau_list.append(niveau)

    math=float(input("tapez votre note math : "))
    math_list.append(math)

    pc=float(input("tapez votre note pc : "))
    pc_list.append(pc)

    svt=float(input("tapez votre note svt : "))
    svt_list.append(svt)

    moyenne=(math + pc + svt)/3
    moy_list.append(moyenne)
    print(moy_list)
    
    if moyenne>=10 and moyenne <12 :
        mention='passable'
    if moyenne>=12 and moyenne<14:
        mention='A.Bien'
    if moyenne >=14 and moyenne<16:
        mention='Bien'
    if moyenne >=16 and moyenne <18:
        mention='Tres Bien'
    if moyenne>=18 and moyenne<20 :
        mention = 'excelent'
    mention_list.append(mention)

    if moyenne==12 :
        print("ISTA")
    elif moyenne==13:
        print("BTS")
    elif moyenne==14:
        print("EST")
    elif moyenne==15:
        print("FST")
    elif moyenne==16:
        print("ENSA")


    qt=input('voulez vous saisir les infos d\'un autre etidions ? oui/non : ')
    qt = qt.lower()
    
nb=len(names_list)
for i in range(0, nb):
    print(50*'*')
    print(20*'*','bultan',20*'*')
    print(f'nom est : {names_list[i]}')
    print(f'niveau est : {niveau_list[i]}')
    print(f'math : {math_list[i]}')
    print(f'pc : {pc_list[i]}')
    print(f'svt : {svt_list[i]}')
    moy = round(moy_list[i], 2)
    print(f'moyenne : {moy}')
    print(f'mention : {mention_list[i]}')
    print(50*'*')

    if moy>=12 :
        print("ISTA")
    elif moy>=13:
        print("BTS")
    elif moy>=14:
        print("EST")
    elif moy>=15:
        print("FST")
    elif moy>=16:
        print("ENSA")
    
    # condition=float(input(moyenne))
    # condition_list.append(mention)



























