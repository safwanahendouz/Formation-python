
#affichage un message dans la console
#print('salam ait ali bekou')
 
#name = input('entrer votre nom: ')
#print('votre nom est: +name')




#la lecture avec python
#formaton=input('entrer le nom de la formation: ')
#year=input('entrer l'annee de formation : ')
#print(60 "=")
#print("formation: " "+formation+"+year)
#print(60 "")

###################################################################################les varables

#my price =99.99   #float/double reel
#number=6754 #int integer entier 
#status="safwan ahendouz"
#texte25=""je suis safwan ahendouz"
#    et je suis un developpeur python
#   ""#string

#print(my price)
#print(number)
#print(status)
#print(name)
#print(texte25)

# firstname= "mohamed"
# age= 22#
# phone= "06666665"
# active= True 
# print("je suis : ",firstname, " age : ",age," phone " ,phone, " active ",active)
# print(f" je suis {firstname} age : {age} phone : {phone} active : {active} "

# escape characters
print( "mohamed \" DEV" )
# 
# \n  #new ligne 
# \t  #tabulation
# \\  #backslash
# \ " double que
# \a  #bell cad bip sonore  

age = input("entrer votre age: ")

if age >=18 :
    print("vous etes majeur")
else:
    print("vous etes mineur")   
print("fin de programme")   
    
    ########################################################
############# PYTHON BASICS ############################
########################################################



#Affichage un message dans la console
# print('salam ait ali')

# name = input('Entrer Votre Nom : ')
# print("Votre nom est : "+name)




# la lecture avec python 
# formation = input('Entrer  le nom de la formation : ')
# year = input('Entrer  l\'année de formation : ')
# print(60*"=")
# print("Formation : "+ formation+ " " + year)
# print(60*"*")





########################################################
#les variables
# firstName= "Mohamed"
# age= "22"
# phone="07634567899"
# active = True


# print("je suis : "+ firstName+ " Age: "+age+" Phone : "+phone ," Active : " , active)
# print("je suis : ", firstName, " Age: ",age," Phone : ",phone ," Active : " , active)
# print(f"je suis : {firstName} Age: {age} Phone : {phone} Active : {active}")







# my_price = 99.99    #float / double  reel
# number = 6754  #int integer  entier
# status = True   #boolean
# name = "Mohamed Machlou" #String     chaine de carectere
# texte25 = """ Je suis Mohamed Machlou
#             et je suis un développeur Python
#           """ #String

# print( my_price)
# print(number)
# print(status)
# print(name) 
# print(texte25) 


########################################################
#String

# name = "MACHLOU DEV"

# print(len(name))  # Nommbre des caracteres
# print(name[0]) #Affiche le premier 
# print(name[1]) #Affiche le deuxieme 
# print(name[-1]) #Affiche le dernier 
# print(name[0:3]) #Affiche le premier 
# print(name[0:5]) #Affiche le premier 
# print(name[0:]) #Affiche le premier 
# print(name[:5]) #Affiche le premier 
# print(name[:]) #Affiche le premier 


########################################################
# Escape Characters

# print("Mohamed \v Machlou")


# \n  #new line
# \t  #tabulation
# \\  #backslash
# \'  #apostrophe
# \"  #double qu
# \a  #bell cad Bip Sonore
# \b  #backspace
# \f  #form feed
# \r  #carriage return
# \v  #vertical tabulation


# name = "Machlou \"Dev\"\a "
# print(name) 


########################################################
# String Format

# firstName = "Mohamed"
# lastName = "Machlou"
# salaire = 40000
# course = "python in ali ali"
# # title = firstName + " " + lastName + " " + course+ " " ,salaire, "$"
# title = f"{firstName} {lastName}  {course} {salaire}$"
# print(title)


########################################################
# Methods Strings

# fullName = "                    Mohamed;Machlou;Safaoun;jamal"


# result = len(fullName) #nombres des lettres
# result = fullName.upper() #upper case
# result = fullName.lower() #lower case
# result = fullName.capitalize() #capitalize 1ère lettre en majuscule
# result = fullName.title() #title case la premiere lettere en majiscule
# result = fullName.swapcase() #swap case
# result = fullName.isupper() #is upper case
# result = fullName.islower() #is lower case
# result = fullName.istitle() #is title case
# result = fullName.isalpha() #is alpha
# result = fullName.isalnum() #is alphanumeric
# result = fullName.isnumeric() #is numeric
# result = fullName.isdecimal() #is decimal
# result = fullName.isascii() #is ascii
# result = fullName.isspace() #is space         
# result = fullName.istitle() #is title 
# result = fullName.startswith("Mohi") #start with
# result = fullName.endswith("M") #end with
# result = fullName.find("Mac") #find
# result = fullName.index("M") #index
# result = fullName.count("M") #count
# result = fullName.replace("M", "A") #replace
# result = fullName.split(";") #split return list  
# result = fullName.strip() #strip supprimer les espaces debut/fin


# print(result)

########################################################
# Numbers

# n1 = 7
# n2 = 2

# print(n1) # integer
# print(n2) #float

# print(type(n1)) #type
# print(type(n2)) #type

# print(n1 + n2) #addition
# print(n1 - n2) #subtraction
# print(n1 * n2) #multiplication
# print(n1 / n2) #division
# print(n1 // n2) #division entiere
# print(n1 % n2) #modulo
# print(n1 ** n2) #exponentiation

########################################################
#  Methods Numbers

# n = 25.53


# n_round = round(n) #round
# print(n_round)

# n_abs = abs(n) #abs
# print(n_abs)

# n_pow = pow(n, 2) #pow
# print(n_pow)

# # python 3 math module
# import math

# n_sqrt = math.sqrt(n) #sqrt
# print(n_sqrt)

# n_ceil = math.ceil(n) #ceil
# print(n_ceil)

# n_floor = math.floor(n) #floor
# print(n_floor)




# n = int(input("Entrer un nombre : "))
# n = n + 2

# print(f"Le nombre est :  {n}")



########################################################
############# Structures Conditionnelles ###############
########################################################
########################################################
#  Comparaison Operators
# == egaux
# !=  deffrent
# >
# <
# >=
# <=
# and   et
# or   ou 
# not


#   If else and elif Statement
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# age = int(input("Entrer votre age : "))

# if age >= 18:
#     print("Vous êtes majeur")
# else:
#     print("Vous êtes mineur")
    
# print("fin du programme")



























