
# "<" et le symbole "supérieur à" est ">

# test des note
# n= 20
# if n >= 10:
#     print('ADMIS')
# elif n < 10:
#     print('NON ADMIS')

##############################################################
# age = 18
# sexe = "femme"


# if age >= 18:
    
#     if sexe == 'homme':
#         print('Accept')
#     else:
#         print('out !!!!')
        
# else:
#     print('out !!!!')

##############################################################

# salaire= 25000

# if salaire < 5000:
#     salaire = salaire + 1000
    
# elif salaire < 10000:
#     salaire = salaire + 2000
    
# elif salaire < 20000:
#     salaire = salaire + 5000

# else:
#     salaire = salaire + 10000
    
# print(salaire)
    
################################################################

# email = input("Tapez votre email : ")

# indice = email.find('@')
# nb_caractere = len(email)
# status = email.endswith('.com')


# if indice >= 0 and nb_caractere >= 15 and status == True:
#     print("It's a Valid Email")
# else:
#     print("It's not a Valid ")


############################################################

nombre = int(input("Tapez un nombre :  "))

reste = nombre % 2

if reste == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")

