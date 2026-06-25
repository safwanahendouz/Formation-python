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
    print('*'*20)

    print(f'ajauter un produit : 1')
    print(f'afficher tous les produits : 2')
    print(f'rechercher un produit par nom : 3')
    print(f'modifier un produit : 4')
    print(f'supprimer un produit : 5')
    print(f'quitter le programme : 6')
    choix=input(f'tapez un choix : ')

    if choix==1:
        print(f'le choix est ajauter')
        ajout = {
            'nom': nom,
            'id' : id,
            'prix': prix,
            'quantite' : quantite,
        }
        produits.append(ajout) 
        

    if choix==2:
        print(f'afficher tous les produits ')
        for produit in produits:
            print(produit)
    if choix==3:
        print(f'rechercher un produit')
        nom_recherche = input(f'tapez le nom du produit a rechercher : ')
        for produit in produits:
            if produit['nom'] == nom_recherche:
                print(produit)
                break

    if choix==4:
        print(f'modifier un produit')
        nom_modif = input(f'tapez le nom du produit a modifier : ')
        for produit in produits:
            if produit['nom'] == nom_modif:
                print(produit)
                nouveau_nom = input(f'tapez le nouveau nom : ')
                nouveau_id = int(input(f'tapez le nouveau id : '))
                nouveau_prix = float(input(f'tapez le nouveau prix : '))
                nouvelle_quantite = float(input(f'tapez la nouvelle quantite : '))
                produits.remove(produit)
                produits.append({
                    'nom': nouveau_nom,
                    'id': nouveau_id,
                    'prix': nouveau_prix,
                    'quantite': nouvelle_quantite
                })
                break

    if choix==5:
        print(f'supprimer un produit')
        nom_supprimer = input(f'tapez le nom du produit a supprimer : ')
        for produit in produits:
            if produit['nom'] == nom_supprimer:
                produits.remove(produit)
                print(f'le produit {nom_supprimer} a ete supprimer ')
                break

    if choix==6:
        print(f'quitter le programme ')
    qt=input(f'voulez vous continuer ? oui/non : ')




