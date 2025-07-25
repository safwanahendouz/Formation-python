workers = [
    {
        'nom': 'mohamed',
        'id' : 112233,
        'prix':2000,
        'quantite' : 2.5,
    },
    {
        'nom' : 'safwan',
        'id' : 332211,
        'prix' : 3000,
        'quantite' : 3
    },
    {
        'nom' : 'ahmed',
        'id' : 111111,
        'prix' : 6000,
        'quantite' : 1.
    }
]

print('bojour')
produits =[]
qt='oui'

while qt.lower()=='oui':
    nom=input(f'tapez votre nom : ')
    id=int(input(f'tapez votre id : '))
    prix=float(input(f'tapez votre prix : '))
    quantite=float(input(f'tapez votre quantite : '))

    print(f'ajauter un produit : 1')
    print(f'afficher tous les produits : 2')
    print(f'rechercher un produit par nom : 3')
    print(f'modifier un produit : 4')
    print(f'supprimer un produit : 5')
    print(f'quitter le programme : 6')
    choix=input(f'tapez un choix : ')

    if choix==1:
        print(f'le choix est ajauter')
        

    if choix==2:
        print(f'afficher tous les produits ')

    if choix==3:
        print(f'rechercher un produit')

    if choix==4:
        print(f'modifier un produit')
          
    if choix==5:
        print(f'supprimer un produit')

    if choix==6:
        print(f'quitter le programme ')




        