    
#######################################################################

# Tuple

# notes_1 = (12, 14, 18,19, 19) #mode lecture | mais on ne peut pas faire : (l'ajout / modification /supprission )
# notes_2 = [1, 13, 16,20, 10]  # lecture  l'ajout   modification supprission 

# print(notes_1[1])
# print(notes_2[1])


# a, b, c, d, e = notes_2

# print(a, b, c, d, e)


#######################################################################

# cast tuple to list

# notes_1 = (12, 14, 18,19, 19)

# my_new_list = list(notes_1)

# print(my_new_list)


#######################################################################

# cast list to tuple

# notes_1 = [12, 14, 18,19, 19]

# my_new_tuple = tuple(notes_1)

# print(my_new_tuple)


#######################################################################

#  Lambda Function

# 1er Method
# users = [
#     ('Mohamed', 29),
#     ('Yassine', 59),
#     ('Hanan', 89),
#     ('Samir', 19),
# ]

# users.sort(key=lambda item: item[0])

# print("Tri avec lambda :")
# for nom, age in users:
#     print(f"{nom} - {age}")


# 2eme Method
# users = [
#     ('Mohamed', 29),
#     ('Yassine', 59),
#     ('Hanan', 89),
#     ('Samir', 19),
# ]

# def get_age(user):
#     return user[1]

# users.sort(key=get_age)

# print("\nTri avec fonction nommée :")
# for nom, age in users:
#     print(f"{nom} - {age}")



#######################################################################
# Map 
# users = [
#     ('Mohamed', 29),
#     ('Yassine', 59),
#     ('Hanan', 89),
#     ('Samir', 19),
# ]

# noms_majuscules = list(map(lambda user: user[0].upper(), users))

# print("Noms en majuscules :", noms_majuscules)


#######################################################################
# Filter
# users = [
#     ('Mohamed', 29),
#     ('Yassine', 59),
#     ('Hanan', 89),
#     ('Samir', 19),
# ]

# adults = list(filter(lambda user: user[1] >= 30, users))

# print("Utilisateurs de 30 ans ou plus :")
# for nom, age in adults:
#     print(f"{nom} - {age}")



#######################################################################
# Map + Filter

# users = [
#     ('Mohamed', 29),
#     ('Yassine', 59),
#     ('Hanan', 89),
#     ('Samir', 19),
# ]
# users_selected = filter(lambda user: user[1] > 30, users)

# adult_names = list(
#     map(lambda user: user[0].upper(), users_selected)
# )

# print("Noms en majuscules des +30 ans :", adult_names)



#######################################################################
# Zip 

# users = [
#     ('Mohamed', 29),
#     ('Yassine', 59),
#     ('Hanan', 89),
#     ('Samir', 19),
# ]

# # Séparer les noms et les âges avec zip()
# noms, ages = zip(*users)

# # print("Noms :", noms)
# # print("Âges :", ages)


# #######################################################################
# # Zip 

# # noms = ['Ali', 'Sara', 'Nora' ,'ahmed']
# # ages = [22, 34, 28, 50]

# # users = list(zip(noms, ages))

# # print("Liste users :", users)


# #######################################################################

# # Swapping

# #1 er
# # a = 10
# # b = 20

# # # Swapping
# # a, b = b, a

# # # # print("a :", a)
# # # # print("b :", b)


# # # # 2eme 
# # # # users = [
# # # #     ('Mohamed', 29),
# # # #     ('Yassine', 59),
# # # #     ('Hanan', 89),
# # # #     ('Samir', 19),
# # # # ]

# # # # # Échanger la 1re et la 3e position (index 0 et 2)
# # # # users[0], users[2] = users[2], users[0]

# # # # for nom, age in users:
# # # #     print(f"{nom} - {age}")

# # # #######################################################################
# # # # Set Structure

# # # notes = [12,18, 14, 18,19, 19]

# # # first = set(notes)

# # # print(first)

# # # # ##########
# # # first.add(20)
# # # print("Après add(20) :", first)

# # # ##########
# # # first.remove(18)
# # # print("Après remove(18) :", first)


# # # # ##########
# # # first.discard(20)  # Aucun effet
# # # print("Après discard(100) :", first)

# # # # ##########
# # # element = first.pop()
# # # print("Élément supprimé :", element)
# # # print("Après pop() :", first)


# # # # ##########
# # # first.clear()
# # # print("Après clear() :", first)  # Résultat : set()



# # # ##########
# # notes = [12, 18, 14, 18, 19, 19]
# # first = set(notes)
# # copie = first.copy()
# # print("Copie :", copie)



# # # ##########
# # first.update([15, 16])
# # print("Après update([15, 16]) :", first)


# # # ##########
# # second = {17, 18, 19}
# # resultat = first.union(second)
# # print("Union :", resultat)



# # # ##########
# # communs = first.intersection(second)
# # print("Intersection :", communs)


# # # ##########
# # diff = first.difference(second)
# # print("Différence :", diff)


# # # ##########
# # sym_diff = first.symmetric_difference(second)
# # print("Différence symétrique :", sym_diff)


# #####################################################################
# ###########
# # Déclaration d'un dictionnaire avec des paires clé:valeur
# etudiant = {
#     "nom": "Mohamed",
#     "age": 22,
#     "ville": "Casablanca"
# }

# # # Accès à une valeur via la clé
# print(etudiant["nom"])  # Mohamed

# # ############
# # # Créer un dictionnaire à partir de deux listes avec zip()
# # # zip() combine les deux listes en paires (clé, valeur)
# cles = ["nom", "age", "ville"]
# valeurs = ["Yassine", 30, "Rabat"]

# dico = dict(zip(cles, valeurs))
# print(dico)  # {'nom': 'Yassine', 'age': 30, 'ville': 'Rabat'}

# ############
# # Parcourir un dictionnaire et afficher chaque paire
# for cle in etudiant:
#     print(cle, "=>", etudiant[cle])

# ############
# # Accéder à une valeur de manière sécurisée avec get()
# print(etudiant.get("nom"))          # Mohamed
# print(etudiant.get("note", "N/A"))  # Retourne "N/A" si la clé "note" n'existe pas

# ############
# # Modifier une valeur existante et ajouter une nouvelle clé/valeur
# etudiant.update({"age": 23, "note": 18})
# print(etudiant)  # {'nom': 'Mohamed', 'age': 23, 'ville': 'Casablanca', 'note': 18}

# ############
# # Obtenir toutes les clés du dictionnaire
# print(etudiant.keys())  # dict_keys(['nom', 'age', 'ville', 'note'])

# ############
# # Obtenir toutes les valeurs du dictionnaire
# print(etudiant.values())  # dict_values(['Mohamed', 23, 'Casablanca', 18])

# ############
# # Afficher toutes les paires clé:valeur
# for cle, valeur in etudiant.items():
#     print(f"{cle} : {valeur}")

# ############
# # Supprimer une clé et récupérer sa valeur
# note = etudiant.pop("note")
# print("Note supprimée :", note)  # Note supprimée : 18

# ############
# # Supprimer une paire avec la clé
# del etudiant["ville"]

# ############
# # Vider complètement le dictionnaire
# etudiant.clear()
# print(etudiant)  # {}

############
############
############
############


