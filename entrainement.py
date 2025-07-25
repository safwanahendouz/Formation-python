# etudiants = [
#     {
#         'nom': "Mohamed",
#         'age': 29,
#         'note': 20,
#         'mention': 'Très Bien',
#         'ville': 'Casa',
#     },
#     {
#         'nom': "Fatima",
#         'age': 24,
#         'note': 18,
#         'mention': 'Très Bien',
#         'ville': 'Rabat',
#     },
#     {
#         'nom': "Youssef",
#         'age': 27,
#         'note': 15,
#         'mention': 'Bien',
#         'ville': 'Fès',
#     },
#     {
#         'nom': "Salma",
#         'age': 22,
#         'note': 13,
#         'mention': 'Assez Bien',
#         'ville': 'Agadir',
#     },
#     {
#         'nom': "Amine",
#         'age': 30,
#         'note': 17,
#         'mention': 'Bien',
#         'ville': 'Tanger',
#     },
#     {
#         'nom': "Khadija",
#         'age': 25,
#         'note': 19,
#         'mention': 'Très Bien',
#         'ville': 'Marrakech',
#     },
#     {
#         'nom': "Omar",
#         'age': 28,
#         'note': 12,
#         'mention': 'Passable',
#         'ville': 'Oujda',
#     },
#     {
#         'nom': "Sara",
#         'age': 23,
#         'note': 16,
#         'mention': 'Bien',
#         'ville': 'Kenitra',
#     },
#     {
#         'nom': "Anas",
#         'age': 26,
#         'note': 10,
#         'mention': 'Passable',
#         'ville': 'Tétouan',
#     },
#     {
#         'nom': "Imane",
#         'age': 21,
#         'note': 14,
#         'mention': 'Assez Bien',
#         'ville': 'El Jadida',
#     },
#              {
#             'nom': "safouan",
#             'age': 29,
#             'note': 20,
#             'mention': 'Tres Bien',
#             'ville': 'casa',
#         }]

# print('bonjour')

# etudiants=[]
# choix=1|2|3|4
# qt="oui"

# while qt.lower()== 'oui' :
#     print(f' pour ajauter : 1')
#     print(f' pour modifier :2')
#     print(f' pour supprimer: 3')
#     print(f' pour quitter : 4')

#     input("tapez un choix : ")

#     if choix ==1:
#         print(f'le choix est ajauter')

#         nom=input('tapez votre nom : ')
#         age =int(input('tapez votre age : '))
#         note =float(input('tapez votre note : '))
#         ville =input('tapez votre ville : ')
        
#         etudiants.append()
        
#         for indix,e in enumerate(etudiants) :
#             print(f'indix : {e} - {etudiants}')



#     elif choix ==2:
#         print(f'le choix est modifier') 
#         nom = input('tapez le nom d\'etudiant a modifier : ')
#         for index,e in enumerate(etudiants):
#             if e["nom"]== nom:
#                 print('etudiant a modifier : ')
#                 print(f'nom : {e["nom"]}')
#                 print(f'age : {e["age"]}')
#                 print(f'note : {e["note"]}')
#                 print(f'ville : {e["ville"]}')
#                 update_key=input(f'determinez la cle qui vous voulez modifiez \n \t tapez votre chiox: nom - age - note - ville : ').lower()
#                 new_value=input(f'l\'ancienne valeur de votre {update_key}:  {e[f"{update_key}"]} \n \t la nouvelle valeur de votre {update_key}est :  ') 

#     elif choix == 3 :
#         print(f'le choix est supprimer') 
#         nom=input(f'tapez le nom d\'etudiant qui vous voulez suppr')
        

#     elif choix == 4 :
#         print(f'le choix est quitter')  



#     input(f'voulez vous continuez ? oui ou non : ')           

        

# print('bonjour')
# a=5
# b=7
# print(a-b)

        
for number in range(1,19):
    if number ==8:
        continue
    print('mon message', number)
print('fin de programme')    















































