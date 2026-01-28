
#########################################################################

def ajauter_etudiant():


    print(f'le choix est : Ajouter')
    nom = input('Taper votre nom : ')   
    age = int(input('Taper votre age : '))
    note = float(input('Taper votre note : '))
    ville = input('Taper votre ville : ')
        
    
    etudiants.append({
        'nom': nom,
        'age': age,
        'note': note,
        'mention': 'Tres Bien',
        'ville': ville,
    })

    for N,etudiant in enumerate(etudiants) :
        print(f'etudiant : {N}-{etudiant}') 
        
etudiants = [
    {
        'nom': "Mohamed",
        'age': 29,
        'note': 20,
        'mention': 'Très Bien',
        'ville': 'Casa',
    },
    {
        'nom': "Fatima",
        'age': 24,
        'note': 18,
        'mention': 'Très Bien',
        'ville': 'Rabat',
    },
    {
        'nom': "Youssef",
        'age': 27,
        'note': 15,
        'mention': 'Bien',
        'ville': 'Fès',
    },
    {
        'nom': "Salma",
        'age': 22,
        'note': 13,
        'mention': 'Assez Bien',
        'ville': 'Agadir',
    },
    {
        'nom': "Amine",
        'age': 30,
        'note': 17,
        'mention': 'Bien',
        'ville': 'Tanger',
    },
    {
        'nom': "Khadija",
        'age': 25,
        'note': 19,
        'mention': 'Très Bien',
        'ville': 'Marrakech',
    },
    {
        'nom': "Omar",
        'age': 28,
        'note': 12,
        'mention': 'Passable',
        'ville': 'Oujda',
    },
    {
        'nom': "Sara",
        'age': 23,
        'note': 16,
        'mention': 'Bien',
        'ville': 'Kenitra',
    },
    {
        'nom': "Anas",
        'age': 26,
        'note': 10,
        'mention': 'Passable',
        'ville': 'Tétouan',
    },
    {
        'nom': "Imane",
        'age': 21,
        'note': 14,
        'mention': 'Assez Bien',
        'ville': 'El Jadida',
    },
            {
            'nom': "safouan",
            'age': 29,
            'note': 20,
            'mention': 'Tres Bien',
            'ville': 'casa',
        }]

nom = 'safouan'




qt = "oui"

print('Bonjour')

while qt.lower() == "oui":
    print('Ajouter un etudiant   : 1')
    print('Modifier un etudiant  : 2')
    print('Supprimer un etudiant : 3')
    print('Quitter le programme  : 4')
    
    choix = int(input('Taper un choix :  '))
    
    # bloc l'Ajout
    if choix == 1:
        ajauter_etudiant()
        
    elif choix == 2:
        print(f'le choix est : Modifier')
        nom = input('tapez le nom d\' etudiant a modifier : ').lower()
        for index,e in enumerate(etudiants):
            if e['nom'] == nom:
                print('Etudiant à Modifier :')
                print(f'Nom : {e["nom"]}')
                print(f'Age : {e["age"]}')
                print(f'Note : {e["note"]}')
                print(f'Ville : {e["ville"]}')
                update_key = input(f'Determinez la cle que vous voulez Modifier : \n \t   Taper votre choix nom - age - note - ville :  ').lower()
                new_value = input(f"l\'ancienne valeur de votre {update_key} : {e[update_key]}  \nTaper la nouvelle valeur de votre {update_key} : ")

                
                e.update({update_key: new_value})
                
            elif e['nom'] != nom and len(etudiants) == (index +1):
                print('N\'exist pas !!!')
        
        print(f"Etudiants : {etudiants}")

        for N,etudiant in enumerate(etudiants) :
            print(f'etudiant : {N}-{etudiant}')   
        
    elif choix == 3:
        print(f'le choix est : Supprimer')
        for e in etudiants:
            print(e)
        nom= input('tapez un nom d\'etudiant qui vous voulez supprimer : ')

        for index,e in enumerate(etudiants): 

            if nom==str(e['nom']).lower() : 
                print("voulez vous vraiment supprimer l\'etudiant ")
                print(f'index: {index} - {e}')
                qt_sup=input("repond par oui ou non? : ")
                if qt_sup.lower()=='oui' :
                    etudiants.pop(index)    
                    print(f'etudiant {e["nom"]} ')

        for e in etudiants:
            print(e)

    elif choix == 4:
        print(f'le choix est : Quitter')
        qt="nom"
        break
    
    
    
    qt = input('Voulez vous countinuez? oui/non :  ')
    

for e in etudiants:
            print(e)

print(f'nbrs d\'etudiants : {len(etudiants)}')
























 

























