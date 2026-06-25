workers = [
    {
        'name': 'mohamed',
        'id': 112233,
        'price': 2000,
        'quantity': 2.5,
    },
    {
        'name': 'safwan',
        'id': 332211,
        'price': 3000,
        'quantity': 3
    },
    {
        'name': 'ahmed',
        'id': 111111,
        'price': 6000,
        'quantity': 1.0
    }
]

print('hello')
products = []
cont = 'yes'

while cont.lower() == 'yes':
    name = input('enter your name: ')
    id_ = int(input('enter your id: '))
    price = float(input('enter your price:   $'))
    quantity = float(input('enter your quantity: '))
    print('*' * 20)

    print('add a product: 1')
    print('show all products: 2')
    print('search a product by name: 3')
    print('modify a product: 4')
    print('delete a product: 5')
    print('quit program: 6')
    choice = input('enter a choice: ')

    if choice == '1':
        print('choice is add')
        new_product = {
            'name': name,
            'id': id_,
            'price': price,
            'quantity': quantity,
        }
        products.append(new_product)

    if choice == '2':
        print('show all products')
        for product in products:
            print(product)

    if choice == '3':
        print('search a product')
        search_name = input('enter the product name to search: ')
        for product in products:
            if product['name'] == search_name:
                print(product)
                break

    if choice == '4':
        print('modify a product')
        mod_name = input('enter the product name to modify: ')
        for product in products:
            if product['name'] == mod_name:
                print(product)
                new_name = input('enter the new name: ')
                new_id = int(input('enter the new id: '))
                new_price = float(input('enter the new price: '))
                new_quantity = float(input('enter the new quantity: '))
                products.remove(product)
                products.append({
                    'name': new_name,
                    'id': new_id,
                    'price': new_price,
                    'quantity': new_quantity
                })
                break

    if choice == '5':
        print('delete a product')
        del_name = input('enter the product name to delete: ')
        for product in products:
            if product['name'] == del_name:
                products.remove(product)
                print(f'the product {del_name} has been deleted')
                break

    if choice == '6':
        print('quit program')
    cont = input('do you want to continue? yes/no: ')
